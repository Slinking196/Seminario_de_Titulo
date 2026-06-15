import pandas as pd
import numpy as np
import nltk
import time
import logging
import torch
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from pathlib import Path
import re
import evaluate
from datasets import Dataset
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments

# ---------------------------------------------------------
# 1. CONFIGURACIÓN DE LOGS Y RUTAS
# ---------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

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

# ---------------------------------------------------------
# 2. DETECCIÓN DE HARDWARE (CUDA / MPS / CPU)
# ---------------------------------------------------------
if torch.cuda.is_available():
    device = torch.device("cuda")
    use_fp16 = True
    logger.info("Hardware detectado: CUDA (NVIDIA). Activando FP16.")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
    use_fp16 = False # Evita errores de compatibilidad de mixed precision en Apple Silicon
    logger.info("Hardware detectado: MPS (Apple Silicon).")
else:
    device = torch.device("cpu")
    use_fp16 = False
    logger.warning("Hardware detectado: CPU. El entrenamiento será muy lento.")

# ---------------------------------------------------------
# 3. FUNCIONES DE PROCESAMIENTO
# ---------------------------------------------------------
def natural_part_key(path: Path) -> int:
    match = re.search(r"part(\d+)", path.stem)
    if not match:
        return 10**9
    return int(match.group(1))

def read_tripadvisor_data(path: str | Path) -> pd.DataFrame:
    data_path = Path(path)
    files = sorted(data_path.glob(PART_FILE_PATTERN), key=natural_part_key)
    if not files:
        raise FileNotFoundError(f"No se encontraron archivos con patron {PART_FILE_PATTERN} en {data_path}")

    logger.info(f"Se encontraron {len(files)} archivos para cargar en {data_path}.")
    dataframes = []
    for index, file_path in enumerate(files, start=1):
        logger.info(f"Leyendo archivo {index}/{len(files)}: {file_path.name}")
        dataframes.append(pd.read_csv(file_path, sep=";", encoding="utf-8"))

    logger.info("Unión de archivos completada.")
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
    logger.info(f"Dataset original cargado con {len(df)} filas.")
    
    before_nulls = len(df)
    df = df.dropna(subset=["review_text"])
    logger.info(f"Filas con review_text nulo eliminadas: {before_nulls - len(df)}.")

    before_duplicates = len(df)
    df = df.drop_duplicates(subset=["review_text"])
    logger.info(f"Duplicados eliminados por review_text: {before_duplicates - len(df)}.")

    before_labels = len(df)
    df = df[df["etiqueta"].isin(["NON-SUGGESTION", "SUGGESTION"])]
    logger.info(f"Filas descartadas por etiqueta no válida: {before_labels - len(df)}.")

    logger.info("Aplicando limpieza y lematización del texto...")
    df["review_text"] = df["review_text"].apply(process_text)
    df["label"] = df["etiqueta"].apply(process_label)
    logger.info(f"Dataset procesado con {len(df)} filas listas para entrenamiento.")
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
    f1 = metric_f1.compute(predictions=predictions, references=labels, average="binary")["f1"]
    precision = metric_precision.compute(predictions=predictions, references=labels, average="binary")["precision"]
    recall = metric_recall.compute(predictions=predictions, references=labels, average="binary")["recall"]

    return {"accuracy": accuracy, "f1": f1, "precision": precision, "recall": recall}

# ---------------------------------------------------------
# 4. EJECUCIÓN PRINCIPAL
# ---------------------------------------------------------
if __name__ == "__main__":
    start_time = time.perf_counter()
    logger.info("Iniciando ejecución del script de entrenamiento.")
    
    df_raw = read_tripadvisor_data(DATA_DIR)
    df_raw = proccess_dataset(df_raw)

    logger.info("Cargando tokenizer y modelo base...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_ID, 
        num_labels=len(LABEL2ID),
    )
    model.to(device) # Enviamos el modelo al hardware detectado

    # --- INICIO DEL CONGELAMIENTO DE CAPAS ---
    logger.info("Configurando congelamiento de capas (Freezing)...")
    
    # 1. Congelamos todos los parámetros del modelo
    for param in model.parameters():
        param.requires_grad = False

    # 2. Descongelamos las últimas 2 capas del encoder para que se adapten a nuestro dominio
    capas_a_entrenar = 2
    for layer in model.deberta.encoder.layer[-capas_a_entrenar:]:
        for param in layer.parameters():
            param.requires_grad = True

    # 3. Descongelamos el cabezal de clasificación (pooler y classifier)
    for param in model.classifier.parameters():
        param.requires_grad = True
        
    if hasattr(model, "pooler") and model.pooler is not None:
        for param in model.pooler.parameters():
            param.requires_grad = True
            
    parametros_entrenables = sum(p.numel() for p in model.parameters() if p.requires_grad)
    logger.info(f"Capas congeladas. Parámetros entrenables: {parametros_entrenables:,}")
    # --- FIN DEL CONGELAMIENTO ---

    logger.info("Creando dataset de Hugging Face y tokenizando...")
    df = Dataset.from_pandas(df_raw[["review_text", "label"]])
    tokenized_dataset = df.map(lambda x: preproccess_for_model(x, tokenizer), batched=True)

    tokenized_dataset = tokenized_dataset.train_test_split(test_size=0.2, seed=42)
    logger.info(f"Split completado: train={len(tokenized_dataset['train'])}, test={len(tokenized_dataset['test'])}")

    logger.info("Configurando argumentos de entrenamiento...")
    training_args = TrainingArguments(
        output_dir="./resultados_nlu",
        evaluation_strategy="epoch",
        save_strategy="epoch",
        learning_rate=LR,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        gradient_accumulation_steps=4,
        num_train_epochs=EPOCHS,
        weight_decay=0.01,
        load_best_model_at_end=True,
        metric_for_best_model="f1",
        fp16=use_fp16, # Controlado dinámicamente por la detección de hardware
        logging_dir='./logs',
        logging_steps=10, # Mostramos métricas cada 10 steps
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset["train"],
        eval_dataset=tokenized_dataset["test"],
        compute_metrics=compute_metrics,
    )

    logger.info("Iniciando el entrenamiento...")
    trainer.train()
    logger.info(f"Entrenamiento finalizado en {time.perf_counter() - start_time:.2f} segundos.")

    logger.info("Evaluando el mejor modelo en el conjunto de prueba...")
    resultados = trainer.evaluate()
    logger.info(f"Resultados finales: {resultados}")
    
    logger.info("Guardando modelo final...")
    trainer.save_model("./modelo_turismo_final")
    tokenizer.save_pretrained("./modelo_turismo_final")
    logger.info("Proceso completado exitosamente.")