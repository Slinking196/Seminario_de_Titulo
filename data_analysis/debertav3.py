import pandas as pd
import numpy as np
import nltk
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
    df = df.dropna(subset=["review_text"])
    df = df.drop_duplicates(subset=["review_text"])
    df = df[df["etiqueta"].isin(["NON-SUGGESTION", "SUGGESTION"])]

    df["review_text"] = df["review_text"].apply(process_text)
    df["label"] = df["etiqueta"].apply(process_label)
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

df_raw = read_tripadvisor_data(DATA_DIR)
df_raw = proccess_dataset(df_raw)

print(f"Dataset procesado con {len(df_raw)} filas.")
print(df_raw.head())

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_ID, 
    num_labels=len(LABEL2ID),
)

df = Dataset.from_pandas(df_raw[["review_text", "label"]])
tokenized_dataset = df.map(lambda x: preproccess_for_model(x, tokenizer), batched=True)
tokenized_dataset = tokenized_dataset.train_test_split(test_size=0.2, seed=42)

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

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["test"],
    compute_metrics=compute_metrics,
)

# 4. ¡Ejecutar el entrenamiento!
print("Iniciando el entrenamiento...")
trainer.train()

# 5. Evaluar los resultados finales en el test set
print("Evaluando el mejor modelo...")
resultados = trainer.evaluate()
print("Resultados de la validación:", resultados)

# 6. Guardar el modelo definitivo para inferencia futura
print("Guardando el modelo de producción...")
trainer.save_model("./modelo_turismo_final")
tokenizer.save_pretrained("./modelo_turismo_final")