import pandas as pd
import numpy as np
import nltk
import time
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from pathlib import Path
import re
import evaluate
from datasets import Dataset
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments

DATA_DIR = Path("./data_analysis/data/labeled")
OUTPUT_FILE = DATA_DIR / "Chile_all1_clean.csv"
PART_FILE_PATTERN = "Chile_all1_clean_labeled_*.csv"

MODEL_ID = "microsoft/deberta-v3-base"
MAX_LENGTH = 512
BATCH_SIZE = 32
EPOCHS = 5
LR = 2e-5

LABEL2ID = {"NON-SUGGESTION": 0, "SUGGESTION": 1}
ID2LABEL = {0: "NON-SUGGESTION", 1: "SUGGESTION"}

nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)


def log_step(message: str) -> None:
    print(f"[INFO] {message}", flush=True)

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

    log_step(f"Se encontraron {len(files)} archivos para cargar en {data_path}.")
    dataframes = []
    for index, file_path in enumerate(files, start=1):
        log_step(f"Leyendo archivo {index}/{len(files)}: {file_path.name}")
        dataframes.append(pd.read_csv(file_path, sep=";", encoding="utf-8"))

    log_step("Union de archivos completada.")
    return pd.concat(dataframes, ignore_index=True)

def process_text(text: str) -> str:
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    tokens = text.lower().split()
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return " ".join(tokens)

def process_label(label: str) -> int:
    return LABEL2ID.get(label, -1)

def proccess_dataset(df: pd.DataFrame) -> pd.DataFrame:
    log_step(f"Dataset original cargado con {len(df)} filas.")
    before_nulls = len(df)
    df = df.dropna(subset=["review_text"])
    log_step(f"Filas con review_text nulo eliminadas: {before_nulls - len(df)}.")

    before_duplicates = len(df)
    df = df.drop_duplicates(subset=["review_text"])
    log_step(f"Duplicados eliminados por review_text: {before_duplicates - len(df)}.")

    before_labels = len(df)
    df = df[df["etiqueta"].isin(["NON-SUGGESTION", "SUGGESTION"])]
    log_step(f"Filas descartadas por etiqueta no valida: {before_labels - len(df)}.")

    log_step("Aplicando limpieza y lematizacion del texto.")
    df["review_text"] = df["review_text"].apply(process_text)
    df["label"] = df["etiqueta"].apply(process_label)
    log_step(f"Dataset procesado con {len(df)} filas listas para entrenamiento.")
    return df

def preproccess_for_model(examples, tokenizer):
    return tokenizer(
        examples["review_text"],
        truncation=True,
        padding="max_length",
        max_length=MAX_LENGTH,
    )

def compute_metrics(eval_pred):
    metric_acc = evaluate.load("accuracy")
    metric_f1 = evaluate.load("f1")
    metric_precision = evaluate.load("precision")
    metric_recall = evaluate.load("recall")

    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    
    accuracy = metric_acc.compute(predictions=predictions, references=labels)["accuracy"]
    # Usamos average="binary" porque es una clasificación binaria
    f1 = metric_f1.compute(predictions=predictions, references=labels, average="binary")["f1"]
    precision = metric_precision.compute(predictions=predictions, references=labels, average="binary")["precision"]
    recall = metric_recall.compute(predictions=predictions, references=labels, average="binary")["recall"]

    return {"accuracy": accuracy, "f1": f1, "precision": precision, "recall": recall}

start_time = time.perf_counter()
log_step("Iniciando ejecucion del script de entrenamiento.")
log_step("Paso 1: carga de datos de TripAdvisor.")
df_raw = read_tripadvisor_data(DATA_DIR)
log_step("Paso 2: limpieza y preparacion del dataset.")
df_raw = proccess_dataset(df_raw)

log_step(f"Vista previa del dataset procesado: {len(df_raw)} filas y {len(df_raw.columns)} columnas.")
print(df_raw.head())

log_step(f"Paso 3: cargando tokenizer y modelo base '{MODEL_ID}'.")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_ID, 
    num_labels=len(LABEL2ID),
)
log_step("Tokenizer y modelo cargados correctamente.")

log_step("Paso 4: creando dataset de Hugging Face.")
df = Dataset.from_pandas(df_raw[["review_text", "label"]])
log_step("Paso 5: tokenizando textos.")
tokenized_dataset = df.map(lambda x: preproccess_for_model(x, tokenizer), batched=True)
log_step("Tokenizacion completada.")

log_step("Paso 6: dividiendo en entrenamiento y prueba.")
tokenized_dataset = tokenized_dataset.train_test_split(test_size=0.2, seed=42)
log_step(
    f"Split completado: train={len(tokenized_dataset['train'])} ejemplos, "
    f"test={len(tokenized_dataset['test'])} ejemplos."
)

log_step("Paso 7: configurando argumentos de entrenamiento.")
training_args = TrainingArguments(
    output_dir="./resultados_nlu",
    evaluation_strategy="epoch",       # Evaluar al final de cada epoch
    save_strategy="epoch",             # Guardar un checkpoint por epoch
    learning_rate=LR,
    per_device_train_batch_size=8,     # Reducido a 8 para evitar OOM
    per_device_eval_batch_size=8,
    gradient_accumulation_steps=4,     # 8 * 4 = 32 (Tu BATCH_SIZE objetivo)
    num_train_epochs=EPOCHS,
    weight_decay=0.01,
    load_best_model_at_end=True,       # Al final, cargar el modelo que rindió mejor
    metric_for_best_model="f1",        # Usar F1 para decidir cuál checkpoint es el mejor
    fp16=True,                         # Activar precision mixta para acelerar en GPU
)
log_step("Argumentos de entrenamiento configurados.")

log_step("Paso 8: inicializando Trainer.")
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["test"],
    compute_metrics=compute_metrics,
)
log_step("Trainer inicializado correctamente.")

# 4. ¡Ejecutar el entrenamiento!
log_step("Paso 9: iniciando el entrenamiento.")
trainer.train()
log_step(f"Entrenamiento finalizado en {time.perf_counter() - start_time:.2f} segundos.")

# 5. Evaluar los resultados finales en el test set
log_step("Paso 10: evaluando el mejor modelo en el conjunto de prueba.")
resultados = trainer.evaluate()
log_step("Evaluacion finalizada.")
print("Resultados de la validación:", resultados)