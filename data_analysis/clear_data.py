from collections import Counter
import logging
from pathlib import Path
import re
import time

import pandas as pd
from langdetect import DetectorFactory, detect, detect_langs


DATA_DIR = Path("./data_analysis/data")
OUTPUT_FILE = DATA_DIR / "Chile_all1_clean.csv"
PART_FILE_PATTERN = "Chile_all1_part*.csv"

REQUIRED_COLUMNS = {
    "region_name",
    "attraction_name",
    "language",
    "username",
    "rating_review",
    "title",
    "review_text",
    "written_date",
    "visit_date",
    "companion_type",
    "contribution",
    "sentiment",
    "sentiment_score",
    "location",
}

FINAL_COLUMNS = [
    "review_text",
    "title",
    "language",
    "language_detected_context",
    "language_detected_full",
    "language_majority_lang",
    "language_majority_percentage",
]

SUPPORTED_CONTEXT_LANGS = {"es", "en"}


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
LOGGER = logging.getLogger("clear_data")


def log_progress(message: str, start_time: float | None = None) -> None:
    if start_time is None:
        LOGGER.info(message)
        return

    elapsed = time.perf_counter() - start_time
    LOGGER.info("%s | elapsed=%.1fs", message, elapsed)


def natural_part_key(path: Path) -> int:
    match = re.search(r"part(\d+)", path.stem)
    if not match:
        return 10**9
    return int(match.group(1))


def read_tripadvisor_data(path: str | Path) -> pd.DataFrame:
    data_path = Path(path)
    files = sorted(data_path.glob(PART_FILE_PATTERN), key=natural_part_key)
    if not files:
        raise FileNotFoundError(
            f"No se encontraron archivos con patron {PART_FILE_PATTERN} en {data_path}"
        )

    dataframes = [pd.read_csv(file_path, sep=";", encoding="utf-8") for file_path in files]
    return pd.concat(dataframes, ignore_index=True)


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def clean_text_column(series: pd.Series) -> pd.Series:
    return (
        series.fillna("")
        .astype(str)
        .map(normalize_whitespace)
    )


def normalize_source_language(value: object) -> str:
    if pd.isna(value):
        return "unknown"

    text = str(value).strip().lower()
    language_map = {
        "es": "es",
        "spanish": "es",
        "espanol": "es",
        "español": "es",
        "en": "en",
        "english": "en",
    }
    if text in language_map:
        return language_map[text]

    if len(text) == 2 and text.isalpha():
        return text

    return text if text else "unknown"


def safe_detect(text: object) -> str:
    if not isinstance(text, str):
        return "unknown"

    cleaned = normalize_whitespace(text)
    if not cleaned:
        return "unknown"

    try:
        return detect(cleaned)
    except Exception:
        return "unknown"


def safe_detect_probs(text: object, cache: dict[str, dict[str, float]] | None = None) -> dict[str, float]:
    if not isinstance(text, str):
        return {}

    cleaned = normalize_whitespace(text).lower()
    if not cleaned:
        return {}

    if cache is not None and cleaned in cache:
        return cache[cleaned]

    try:
        probs = {item.lang: item.prob for item in detect_langs(cleaned)}
    except Exception:
        probs = {}

    if cache is not None:
        cache[cleaned] = probs
    return probs


def tokenize_words(text: str) -> list[str]:
    return re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ']+", text)


def safe_detect_word(token: str, cache: dict[str, str]) -> str:
    key = token.lower()
    if key in cache:
        return cache[key]

    if len(key) <= 2:
        cache[key] = "unknown"
        return "unknown"

    detected = safe_detect(key)
    cache[key] = detected
    return detected


def resolve_uncertain_token_language(
    tokens: list[str],
    index: int,
    token_prob_cache: dict[str, dict[str, float]],
    global_lang: str,
    window_size: int = 3, # Aumentamos un poco el radio de visión
) -> str:
    votes: Counter[str] = Counter()
    start = max(0, index - window_size)
    end = min(len(tokens), index + window_size + 1)

    for position in range(start, end):
        if position == index:
            continue

        token = tokens[position].lower()
        # Ignoramos palabras demasiado cortas para ser anclas (ej. 'a', 'y')
        if len(token) <= 2:
            continue
            
        probs = safe_detect_probs(token, cache=token_prob_cache)
        if not probs:
            continue

        # LÓGICA DE PESOS:
        # Buscamos la probabilidad más alta de este vecino
        best_lang, best_prob = max(probs.items(), key=lambda x: x[1])
        
        # Si el vecino es muy seguro (>0.90), le damos mucho peso ("Ancla")
        # Si el vecino es dudoso, su peso es mínimo
        weight = (best_prob ** 2) * (1.0 / (abs(position - index)))

        for lang, prob in probs.items():
            if lang in SUPPORTED_CONTEXT_LANGS:
                votes[lang] += weight * prob

    # El idioma global del comentario actúa como "desempate" con un peso moderado
    if global_lang != "unknown":
        votes[global_lang] += 0.8 

    if votes:
        # Retornamos el idioma con más "gravedad" acumulada
        return votes.most_common(1)[0][0]

    return "unknown"


def detect_language_by_context(text: object, window_size: int = 2) -> str:
    if not isinstance(text, str):
        return "unknown"

    cleaned = normalize_whitespace(text)
    if not cleaned:
        return "unknown"

    tokens = tokenize_words(cleaned)
    if not tokens:
        return "unknown"

    global_lang = safe_detect(cleaned)
    token_prob_cache: dict[str, dict[str, float]] = {}
    counts: Counter[str] = Counter()
    uncertain_positions: list[int] = []

    for idx, token in enumerate(tokens):
        token_norm = token.lower()
        if len(token_norm) <= 2:
            uncertain_positions.append(idx)
            continue

        probs = safe_detect_probs(token_norm, cache=token_prob_cache)
        if not probs:
            uncertain_positions.append(idx)
            continue

        top_lang, top_prob = max(probs.items(), key=lambda item: item[1])
        sorted_probs = sorted(probs.values(), reverse=True)
        second_prob = sorted_probs[1] if len(sorted_probs) > 1 else 0.0
        margin = top_prob - second_prob

        if top_prob >= 0.90 and margin >= 0.25:
            counts[top_lang] += 1
        else:
            uncertain_positions.append(idx)

    for idx in uncertain_positions:
        lang = resolve_uncertain_token_language(
            tokens=tokens,
            index=idx,
            token_prob_cache=token_prob_cache,
            global_lang=global_lang,
            window_size=window_size,
        )
        if lang != "unknown":
            counts[lang] += 1

    if counts:
        most_common_count = counts.most_common()
        top_lang, top_freq = most_common_count[0]
        tied = [lang for lang, freq in most_common_count if freq == top_freq]

        if len(tied) == 1:
            return top_lang
        if global_lang in tied:
            return global_lang
        return tied[0]

    return global_lang


def detect_language_by_context_with_cache(
    text: object,
    token_prob_cache: dict[str, dict[str, float]],
    window_size: int = 2,
    full_comment_lang: str | None = None,
) -> str:
    if not isinstance(text, str):
        return "unknown"

    cleaned = normalize_whitespace(text)
    if not cleaned:
        return "unknown"

    tokens = tokenize_words(cleaned)
    if not tokens:
        return "unknown"

    global_lang = full_comment_lang if full_comment_lang else safe_detect(cleaned)
    if not isinstance(global_lang, str) or not global_lang:
        global_lang = "unknown"

    counts: Counter[str] = Counter()
    uncertain_positions: list[int] = []

    for idx, token in enumerate(tokens):
        token_norm = token.lower()
        if len(token_norm) <= 2:
            uncertain_positions.append(idx)
            continue

        probs = safe_detect_probs(token_norm, cache=token_prob_cache)
        if not probs:
            uncertain_positions.append(idx)
            continue

        top_lang, top_prob = max(probs.items(), key=lambda item: item[1])
        sorted_probs = sorted(probs.values(), reverse=True)
        second_prob = sorted_probs[1] if len(sorted_probs) > 1 else 0.0
        margin = top_prob - second_prob

        if top_prob >= 0.90 and margin >= 0.25:
            counts[top_lang] += 1
        else:
            uncertain_positions.append(idx)

    for idx in uncertain_positions:
        lang = resolve_uncertain_token_language(
            tokens=tokens,
            index=idx,
            token_prob_cache=token_prob_cache,
            global_lang=global_lang,
            window_size=window_size,
        )
        if lang != "unknown":
            counts[lang] += 1

    if counts:
        most_common_count = counts.most_common()
        top_lang, top_freq = most_common_count[0]
        tied = [lang for lang, freq in most_common_count if freq == top_freq]

        if len(tied) == 1:
            return top_lang
        if global_lang in tied:
            return global_lang
        return tied[0]

    return global_lang


def get_comment_majority_language_with_cache(
    text: object,
    token_prob_cache: dict[str, dict[str, float]],
) -> tuple[str, float]:
    if not isinstance(text, str):
        return "unknown", 0.0

    cleaned = normalize_whitespace(text)
    if not cleaned:
        return "unknown", 0.0

    tokens = tokenize_words(cleaned)
    if not tokens:
        return "unknown", 0.0

    language_scores: Counter[str] = Counter()
    for token in tokens:
        token_norm = token.lower()
        if len(token_norm) <= 2:
            continue

        probs = safe_detect_probs(token_norm, cache=token_prob_cache)
        if not probs:
            continue

        for lang, prob in probs.items():
            if lang in SUPPORTED_CONTEXT_LANGS:
                language_scores[lang] += prob

    if not language_scores:
        return "unknown", 0.0

    majority_lang, majority_score = language_scores.most_common(1)[0]
    total_score = sum(language_scores.values())
    if total_score <= 0:
        return "unknown", 0.0

    return majority_lang, majority_score / total_score


def clean_and_detect_languages(df: pd.DataFrame) -> pd.DataFrame:
    start_time = time.perf_counter()
    missing_columns = REQUIRED_COLUMNS.difference(df.columns)
    if missing_columns:
        raise ValueError(
            "Faltan columnas requeridas en el dataset: "
            + ", ".join(sorted(missing_columns))
        )

    cleaned_df = df.copy()
    cleaned_df["language"] = cleaned_df["language"].map(normalize_source_language)
    cleaned_df["review_text"] = clean_text_column(cleaned_df["review_text"])
    cleaned_df["title"] = clean_text_column(cleaned_df["title"])
    log_progress("Columnas review_text/title/language normalizadas", start_time)

    # Se eliminan filas sin comentario util para el analisis de texto.
    initial_rows = len(cleaned_df)
    cleaned_df = cleaned_df[cleaned_df["review_text"] != ""].copy()
    log_progress(
        f"Filas sin review_text removidas: {initial_rows - len(cleaned_df)}",
        start_time,
    )

    # Eliminacion de duplicados de contenido textual para evitar sesgo por repeticion.
    before_dedup = len(cleaned_df)
    cleaned_df = cleaned_df.drop_duplicates(subset=["title", "review_text"]).copy()
    log_progress(
        f"Duplicados eliminados por title+review_text: {before_dedup - len(cleaned_df)}",
        start_time,
    )

    unique_reviews = list(cleaned_df["review_text"].unique())
    log_progress(f"Reviews unicas para analizar: {len(unique_reviews)}", start_time)

    token_prob_cache: dict[str, dict[str, float]] = {}
    full_lang_map: dict[str, str] = {}
    context_lang_map: dict[str, str] = {}
    majority_lang_map: dict[str, str] = {}
    majority_pct_map: dict[str, float] = {}

    total_unique = len(unique_reviews)
    progress_step = 20000
    for idx, review in enumerate(unique_reviews, start=1):
        full_lang = safe_detect(review)
        full_lang_map[review] = full_lang

        context_lang_map[review] = detect_language_by_context_with_cache(
            text=review,
            token_prob_cache=token_prob_cache,
            window_size=2,
            full_comment_lang=full_lang,
        )

        majority_lang, majority_pct = get_comment_majority_language_with_cache(
            text=review,
            token_prob_cache=token_prob_cache,
        )
        majority_lang_map[review] = majority_lang
        majority_pct_map[review] = majority_pct

        if idx % progress_step == 0 or idx == total_unique:
            rate = idx / max(time.perf_counter() - start_time, 1e-9)
            LOGGER.info(
                "Procesadas %d/%d reviews unicas | %.1f reviews/s",
                idx,
                total_unique,
                rate,
            )

    cleaned_df["language_detected_full"] = cleaned_df["review_text"].map(full_lang_map)
    cleaned_df["language_detected_context"] = cleaned_df["review_text"].map(context_lang_map)
    cleaned_df["language_majority_lang"] = cleaned_df["review_text"].map(majority_lang_map)
    cleaned_df["language_majority_percentage"] = cleaned_df["review_text"].map(majority_pct_map)

    log_progress("Deteccion de idiomas completada para reviews unicas", start_time)
    log_progress(f"Filas aprobadas finales: {len(cleaned_df)}", start_time)
    criterion_2 = (
        (cleaned_df["language_majority_lang"] == cleaned_df["language_detected_full"])
        & (cleaned_df["language_majority_percentage"] >= 0.50)
    )

    before_filter = len(cleaned_df)
    discarded_comments = cleaned_df[~criterion_2].copy()

    # Exportar comentarios descartados antes de aplicar el filtro final.
    discarded_file = DATA_DIR / "discarded_comments.csv"
    discarded_comments.to_csv(discarded_file, index=False, sep=";", encoding="utf-8")
    log_progress(
        f"Archivo de comentarios descartados generado en: {discarded_file} | filas={len(discarded_comments)}",
        start_time,
    )

    cleaned_df = cleaned_df[criterion_2].copy()
    log_progress(
        f"Filas descartadas por criterio final: {before_filter - len(cleaned_df)}",
        start_time,
    )
    log_progress(f"Filas aprobadas finales: {len(cleaned_df)}", start_time)

    return cleaned_df[FINAL_COLUMNS].copy()


def print_summary(df_final: pd.DataFrame) -> None:
    LOGGER.info("Resumen limpieza y deteccion")
    LOGGER.info("Total filas finales: %d", len(df_final))
    LOGGER.info(
        "Distribucion language (origen) top 20:\n%s",
        df_final["language"].value_counts(dropna=False).head(20),
    )
    LOGGER.info(
        "Distribucion language_detected_full top 20:\n%s",
        df_final["language_detected_full"].value_counts(dropna=False).head(20),
    )
    LOGGER.info(
        "Distribucion language_detected_context top 20:\n%s",
        df_final["language_detected_context"].value_counts(dropna=False).head(20),
    )
    LOGGER.info(
        "Promedio language_majority_percentage: %.4f",
        df_final["language_majority_percentage"].mean(),
    )

    agreement = (
        df_final["language_detected_full"]
        == df_final["language_detected_context"]
    ).mean()
    LOGGER.info("Tasa de acuerdo entre detectores: %.2f%%", agreement * 100)


if __name__ == "__main__":
    DetectorFactory.seed = 0
    pipeline_start = time.perf_counter()

    log_progress("Inicio pipeline de limpieza")
    log_progress("Leyendo datos de TripAdvisor...", pipeline_start)
    df_raw = read_tripadvisor_data(DATA_DIR)
    log_progress(f"Filas leidas: {len(df_raw)}", pipeline_start)

    log_progress("Aplicando limpieza y deteccion de idiomas...", pipeline_start)
    df_clean = clean_and_detect_languages(df_raw)

    log_progress("Desordenando filas para exportacion final...", pipeline_start)
    df_clean = df_clean.sample(frac=1, random_state=42).reset_index(drop=True)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df_clean.to_csv(OUTPUT_FILE, index=False, sep=";", encoding="utf-8")
    log_progress(f"Archivo limpio generado en: {OUTPUT_FILE}", pipeline_start)

    print_summary(df_clean)
    log_progress("Pipeline completado", pipeline_start)