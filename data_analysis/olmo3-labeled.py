from mlx_lm import load, generate
import logging
import time
import json
import re
import os
import ast
from pathlib import Path

import pandas as pd
from nltk.corpus import stopwords
from nltk import download as nltk_download
from simplemma import lemmatize
from tqdm.auto import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
LOGGER = logging.getLogger("olmo3-labeled")

SYSTEM_PROMPT = """You are a writer specializing in travel reviews in Spanish or English.
Classify ONLY the tourist review text as SUGGESTION or NON-SUGGESTION.
IMPORTANT: If the text includes a management response (e.g., "Dear traveler...", "Thank you for your visit..."), ignore only these sections, focus on the remaining review text.

## DEFINITIONS
1. **SUGGESTION**:
    - Must be an **EXPLICIT** request for change, addition, or removal of a feature of the product/service offered.
    - The recipient is the **MANAGEMENT/ADMINISTRATION**.
    - It is a concrete, actionable request to improve the TOURIST EXPERIENCE.
2. **NON-SUGGESTION**:
    - **Descriptive complaints**: "The bed was hard" or "Service was slow" (Past facts, not requests for change).
    - **Compliments**: "Everything was excellent."
    - **Advice to third parties (CRITICAL)**: "Go early," "Ask for table 4," "I don't recommend it for families." This is NOT a suggestion to management; it is advice for other tourists.
3. SPECULATIVE INFERENCES vs. SUGGESTIONS: Phrases expressing high probability or assumptions about the place's beauty (e.g., "It must be beautiful at night," "It must be spectacular in the evening") are INFERENCES, not suggestions. These are compliments based on potential, not requests for management action. A suggestion requires a "gap" between the current state and a desired future state.

## DECISION TREE

STEP 1 — WHO IS THE TOURIST TALKING TO?
Read the fragment and ask: is the tourist addressing other visitors,
or expressing something toward the service itself?
- Describing the place or experience for other readers → NON-SUGGESTION.
- Describing personal feelings or reactions without addressing management → NON-SUGGESTION.
- Advising other tourists what to do, bring, or expect → NON-SUGGESTION.
- Expressing how the service could or should be different → continue to Step 2.
- Feelings, experiences, or suggestions to other tourists about other attractions or products → NON-SUGGESTION.
- ⚠️ "You" in English reviews is usually impersonal (= "one" / "a visitor"),
  not a direct address to management. "You would enjoy it more if..." or
  "Perhaps you could..." are tourist-facing observations, not management requests.

STEP 2 — IS THERE A DESIRED FUTURE STATE?
Does the tourist express a gap between how the service IS and how they WANT it to be?
- Only describes what happened (past facts, complaints) → NON-SUGGESTION.
- Expresses praise, satisfaction, or intent to return → NON-SUGGESTION.
- Expresses a wish, desire or expectation for something different → continue to Step 3.
- ⚠️ Speculative or hypothetical framing ("perhaps", "maybe", "might", "could",
  "quizás", "tal vez") signals an observation, not a request. A genuine desire
  for change uses direct framing: "they should", "I wish they had", "it would
  help if", "falta", "sería bueno que", "deberían".
- Expresses a concrete wish or expectation for something different → continue to Step 3.

STEP 3 — CAN MANAGEMENT ACT ON IT?
Could the service's management implement a concrete change based on this?
- Vague feeling or emotional reaction without actionable content → NON-SUGGESTION.
- Concrete change in offering, communication, pricing policy, or operations → SUGGESTION.

## RESPONSE
Reply ONLY with this JSON, no additional text:
{
  "razonamiento_corto": "Step 1: [tourists/management]. Step 2: [future gap/no]. Step 3: [actionable/no]. [1 sentence conclusion]",
  "etiqueta": "SUGGESTION" or "NON-SUGGESTION"
}"""

INPUT_CSV = Path("data_analysis/data/Chile_all1_clean.csv")
OUTPUT_CSV = Path("data_analysis/data/Chile_all1_clean_labeled2.csv")
CHECKPOINT_EVERY = 100

# Interruptores de preprocesamiento para pruebas A/B.
# Tambien se pueden controlar con variables de entorno:
#   ENABLE_LEMMATIZATION=true/false
#   ENABLE_STOPWORD_REMOVAL=true/false
ENABLE_LEMMATIZATION = os.getenv("ENABLE_LEMMATIZATION", "true").strip().lower() in {
    "1", "true", "yes", "y", "on"
}
ENABLE_STOPWORD_REMOVAL = os.getenv("ENABLE_STOPWORD_REMOVAL", "true").strip().lower() in {
    "1", "true", "yes", "y", "on"
}

def log_progress(message: str, start_time: float | None = None) -> None:
    if start_time is None:
        LOGGER.info(message)
        return

    elapsed = time.perf_counter() - start_time
    LOGGER.info("%s | elapsed=%.1fs", message, elapsed)


def ensure_nltk_resources() -> None:
    try:
        _ = stopwords.words("english")
    except LookupError:
        log_progress("Descargando recurso NLTK: stopwords")
        nltk_download("stopwords", quiet=True)


def build_stopword_sets() -> dict[str, set[str]]:
    ensure_nltk_resources()
    return {
        "en": set(stopwords.words("english")),
        "es": set(stopwords.words("spanish")),
    }


def normalize_lang(lang: str | None) -> str:
    if not lang:
        return "en"
    short = str(lang).strip().lower()[:2]
    return short if short in {"en", "es"} else "en"


def preprocess_comment(
    text: str,
    lang: str,
    stopword_sets: dict[str, set[str]],
    enable_lemmatization: bool,
    enable_stopword_removal: bool,
) -> str:
    return text
    tokens = re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ']+", str(text).lower())
    active_lang = normalize_lang(lang)
    lang_stopwords = stopword_sets.get(active_lang, set())

    if not enable_lemmatization and not enable_stopword_removal:
        return " ".join(tokens)

    processed_tokens = []
    for token in tokens:
        if enable_stopword_removal and token in lang_stopwords:
            continue
        normalized = lemmatize(token, lang=active_lang) if enable_lemmatization else token
        if not normalized:
            continue
        if enable_stopword_removal and normalized in lang_stopwords:
            continue
        processed_tokens.append(normalized)

    return " ".join(processed_tokens)

def _clean_model_response(text: str) -> str:
    cleaned = str(text)
    cleaned = re.sub(r"<think>.*?</think>", "", cleaned, flags=re.DOTALL | re.IGNORECASE)
    cleaned = cleaned.replace("</think>", "")
    cleaned = cleaned.replace("<think>", "")
    cleaned = re.sub(r"```(?:json)?", "", cleaned, flags=re.IGNORECASE)
    cleaned = cleaned.replace("```", "")
    return cleaned.strip()


def _normalize_label(raw_label: str | None) -> str | None:
    if not raw_label:
        return None
    normalized = str(raw_label).strip().upper()
    # Normaliza variantes de guion frecuentes en respuestas LLM.
    normalized = re.sub(r"[\u2010\u2011\u2012\u2013\u2014\u2212_]", "-", normalized)
    normalized = re.sub(r"\s+", "", normalized)
    if normalized == "NON-SUGGESTION":
        return "NON-SUGGESTION"
    if normalized == "SUGGESTION":
        return "SUGGESTION"
    return None


def _extract_braced_blocks(text: str) -> list[str]:
    blocks: list[str] = []
    depth = 0
    start_idx = None

    for idx, char in enumerate(text):
        if char == "{":
            if depth == 0:
                start_idx = idx
            depth += 1
        elif char == "}" and depth > 0:
            depth -= 1
            if depth == 0 and start_idx is not None:
                blocks.append(text[start_idx : idx + 1])
                start_idx = None

    return blocks


def _coerce_to_dict(candidate: str) -> dict | None:
    # 1) JSON estricto
    try:
        parsed = json.loads(candidate)
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        pass

    # 2) Dict estilo Python (comillas simples, etc.)
    try:
        parsed = ast.literal_eval(candidate)
        if isinstance(parsed, dict):
            return parsed
    except (ValueError, SyntaxError):
        pass

    return None


def _extract_fields_without_json(cleaned_text: str) -> dict | None:
    label_match = re.search(
        r'["\']?etiqueta["\']?\s*:\s*["\']?(SUGGESTION|NON[-_\u2010\u2011\u2012\u2013\u2014\u2212]SUGGESTION)["\']?',
        cleaned_text,
        flags=re.IGNORECASE,
    )
    reason_match = re.search(
        r'["\']?razonamiento_corto["\']?\s*:\s*["\'](.+?)["\']\s*(?:,|\}|$)',
        cleaned_text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    label = _normalize_label(label_match.group(1) if label_match else None)
    reason = reason_match.group(1).strip() if reason_match else None

    if not label:
        # Fallback: buscar veredicto textual al final de la respuesta.
        verdict_match = re.search(
            r"(?:therefore|final(?:\s+label)?|clas(?:sification|ificacion)|etiqueta)\W+"
            r"(SUGGESTION|NON[-_\u2010\u2011\u2012\u2013\u2014\u2212]SUGGESTION)",
            cleaned_text,
            flags=re.IGNORECASE,
        )
        label = _normalize_label(verdict_match.group(1) if verdict_match else None)

    if label:
        if not reason:
            sentence = cleaned_text.split("\n")[0].strip()
            reason = sentence[:280] if sentence else "Etiqueta inferida desde respuesta parcial"
        return {
            "razonamiento_corto": reason,
            "etiqueta": label,
        }

    return None


def extract_json_from_olmo(text: str) -> dict | None:
    try:
        cleaned = _clean_model_response(text)

        # Intento 1: extraer todos los bloques {...} balanceados y evaluar desde el final.
        # En este caso, normalmente el ultimo bloque contiene la respuesta final.
        for candidate in reversed(_extract_braced_blocks(cleaned)):
            parsed = _coerce_to_dict(candidate)
            if not isinstance(parsed, dict):
                continue

            label = _normalize_label(parsed.get("etiqueta"))
            reason = str(parsed.get("razonamiento_corto", "")).strip()
            if label:
                return {
                    "razonamiento_corto": reason,
                    "etiqueta": label,
                }

        # Intento 2: JSON truncado al final por limite de tokens.
        first_open = cleaned.rfind("{")
        if first_open != -1:
            candidate = cleaned[first_open:]
            open_count = candidate.count("{")
            close_count = candidate.count("}")
            if open_count > close_count:
                candidate += "}" * (open_count - close_count)

            parsed = _coerce_to_dict(candidate)
            if isinstance(parsed, dict):
                label = _normalize_label(parsed.get("etiqueta"))
                reason = str(parsed.get("razonamiento_corto", "")).strip()
                if label:
                    return {
                        "razonamiento_corto": reason,
                        "etiqueta": label,
                    }

        # Intento 3: extraer campos aunque el JSON no sea parseable.
        salvaged = _extract_fields_without_json(cleaned)
        if salvaged:
            log_progress("Advertencia: JSON no parseable, se recuperaron campos por fallback")
            return salvaged

        preview = cleaned.replace("\n", " ")[:220]
        log_progress(
            "Error: No se encontró JSON válido en la respuesta. "
            f"Preview respuesta='{preview}'"
        )
        return None

    except Exception as e:
        log_progress(f"Error inesperado al extraer JSON: {e}")
        return None

def analyze_data(data, model, tokenizer):
    message = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": f"""Analiza la siguiente reseña:
            ---
            {data}
            ---
            Respuesta en JSON:"""
        }
    ]

    prompt = tokenizer.apply_chat_template(
        message,
        tokenize=False,
        add_generation_prompt=True
    )

    response = generate(
        model,
        tokenizer,
        prompt= prompt,
        max_tokens=2500,
        verbose=False,
    )

    extracted_json = extract_json_from_olmo(response)
    if extracted_json is None:    
        log_progress(f"-" * 100) 
        log_progress(f"Comentario enviado a OLMo3: {data}")
        log_progress(f"Respuesta OLMo3: {response}")
        log_progress(f"-" * 100)

    return extracted_json


def label_reviews() -> None:
    total_start = time.perf_counter()
    log_progress("Iniciando pipeline de etiquetado")

    if not INPUT_CSV.exists():
        raise FileNotFoundError(f"No se encontró el archivo de entrada: {INPUT_CSV}")

    stopword_sets = build_stopword_sets() if ENABLE_STOPWORD_REMOVAL else {"en": set(), "es": set()}

    log_progress(
        "Configuracion preprocesamiento | "
        f"lemmatization={ENABLE_LEMMATIZATION} | stopword_removal={ENABLE_STOPWORD_REMOVAL}"
    )

    log_progress(f"Leyendo dataset desde {INPUT_CSV}", total_start)
    df = pd.read_csv(INPUT_CSV, sep=";", encoding="utf-8-sig")
    df = df[df["language_detected_full"] == "en"]  # Filtrar solo reseñas en inglés
    df = df[10000:15000]  # Limitar a 10000 filas para pruebas iniciales
    required_columns = {"review_text", "language_majority_lang"}
    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas requeridas en el CSV: {sorted(missing)}")

    log_progress("Cargando modelo OLMo3 en memoria", total_start)
    model_id = "mlx-community/olmo-3-7b-think-4bit"
    model, tokenizer = load(model_id)

    text_cache: dict[str, dict | None] = {}

    output_df = df.copy()
    output_df["review_text_preprocessed"] = ""
    output_df["razonamiento_corto"] = None
    output_df["etiqueta"] = None
    output_df["estado_etiquetado"] = "pending"
    ok_count = 0
    parse_error_count = 0
    empty_after_preprocess_count = 0

    total_rows = len(df)
    log_progress(f"Comenzando inferencia para {total_rows} comentarios", total_start)

    with logging_redirect_tqdm(loggers=[LOGGER]):
        with tqdm(
            total=total_rows,
            desc="Etiquetando reseñas",
            unit="reseña",
            dynamic_ncols=True,
        ) as progress_bar:
            for processed_count, (idx, review_text, lang_value) in enumerate(
                df[["review_text", "language_majority_lang"]].itertuples(index=True, name=None),
                start=1,
            ):
                raw_text = "" if pd.isna(review_text) else str(review_text)
                lang = normalize_lang(None if pd.isna(lang_value) else str(lang_value))

                cleaned_text = preprocess_comment(
                    raw_text,
                    lang,
                    stopword_sets,
                    enable_lemmatization=ENABLE_LEMMATIZATION,
                    enable_stopword_removal=ENABLE_STOPWORD_REMOVAL,
                )
                output_df.at[idx, "review_text_preprocessed"] = cleaned_text

                if not cleaned_text:
                    output_df.at[idx, "razonamiento_corto"] = "Texto vacío tras preprocesamiento"
                    output_df.at[idx, "etiqueta"] = "NON-SUGGESTION"
                    output_df.at[idx, "estado_etiquetado"] = "empty_after_preprocess"
                    empty_after_preprocess_count += 1
                else:
                    if cleaned_text in text_cache:
                        parsed = text_cache[cleaned_text]
                    else:
                        parsed = analyze_data(cleaned_text, model, tokenizer)
                        text_cache[cleaned_text] = parsed

                    if parsed and isinstance(parsed, dict):
                        output_df.at[idx, "razonamiento_corto"] = str(parsed.get("razonamiento_corto", ""))
                        output_df.at[idx, "etiqueta"] = str(parsed.get("etiqueta", ""))
                        output_df.at[idx, "estado_etiquetado"] = "ok"
                        ok_count += 1
                    else:
                        output_df.at[idx, "estado_etiquetado"] = "parse_error"
                        parse_error_count += 1

                progress_bar.set_postfix(
                    ok=ok_count,
                    parse_error=parse_error_count,
                    empty=empty_after_preprocess_count,
                    refresh=False,
                )
                progress_bar.update(1)

                if processed_count % CHECKPOINT_EVERY == 0 or processed_count == total_rows:
                    output_df.to_csv(OUTPUT_CSV, sep=";", index=False, encoding="utf-8-sig")
                    log_progress(
                        f"Checkpoint guardado ({processed_count}/{total_rows}) en {OUTPUT_CSV}",
                        total_start,
                    )

    log_progress("Etiquetado completado", total_start)


if __name__ == "__main__":
    label_reviews()
