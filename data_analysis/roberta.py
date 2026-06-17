import pandas as pd
import numpy as np
import nltk
import time
import logging
import torch
from nltk.stem import WordNetLemmatizer
from pathlib import Path
import re
import evaluate
from datasets import Dataset
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments
from sklearn.utils.class_weight import compute_class_weight
import torch.nn as nn


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

MODEL_ID = "roberta-base"
MAX_LENGTH = 512
BATCH_SIZE = 32
EPOCHS = 5
LR = 2e-5

LABEL2VECTOR = {
    "NON-SUGGESTION": [1.0, 0.0],
    "SUGGESTION": [0.0, 1.0]
}
LABEL2ID = {"NON-SUGGESTION": 0, "SUGGESTION": 1}
ID2LABEL = {0: "NON-SUGGESTION", 1: "SUGGESTION"}

nltk.download("wordnet", quiet=True)

# ---------------------------------------------------------
# 2. DETECCIÓN DE HARDWARE (CUDA / MPS / CPU)
# ---------------------------------------------------------
if torch.cuda.is_available():
    device = torch.device("cuda")
    use_bf16 = True
    logger.info("Hardware detectado: CUDA (NVIDIA). Activando BF16.")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
    use_bf16 = False # Evita errores de compatibilidad de mixed precision en Apple Silicon
    logger.info("Hardware detectado: MPS (Apple Silicon).")
else:
    device = torch.device("cpu")
    use_bf16 = False
    logger.warning("Hardware detectado: CPU. El entrenamiento será muy lento.")

class CustomTrainer(Trainer):
    def __init__(self, class_weights, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.class_weights = torch.tensor(class_weights, dtype=torch.float32).to(self.model.device)

    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
        labels = inputs.pop("labels")
        outputs = model(**inputs)
        logits = outputs.get("logits")
        
        # Forzamos a que las etiquetas sean float32 para que CrossEntropyLoss entienda que es One-Hot
        labels_one_hot = labels.to(torch.float32)
        
        # Pasamos ambos tensores que ahora tienen la misma forma [Batch_Size, 2]
        loss_fct = nn.BCEWithLogitsLoss()
        loss = loss_fct(logits, labels_one_hot)
        
        return (loss, outputs) if return_outputs else loss

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
    lemmatizer = WordNetLemmatizer()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    tokens = text.lower().split()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return " ".join(tokens)

def process_label(label: str) -> list:
    return LABEL2VECTOR.get(label, [0.0, 0.0])

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
    df = pd.concat([df[df["etiqueta"] == "NON-SUGGESTION"].head(5000), df[df["etiqueta"] == "SUGGESTION"]], ignore_index=True) # Oversampling de la clase minoritaria
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
    true_labels = np.argmax(labels, axis=-1)
    
    accuracy = metric_acc.compute(predictions=predictions, references=true_labels)["accuracy"]
    f1 = metric_f1.compute(predictions=predictions, references=true_labels, average="binary")["f1"]
    precision = metric_precision.compute(predictions=predictions, references=true_labels, average="binary")["precision"]
    recall = metric_recall.compute(predictions=predictions, references=true_labels, average="binary")["recall"]

    return {"accuracy": accuracy, "f1": f1, "precision": precision, "recall": recall}

def probar_ejemplos(textos: list, model_test, tokenizer_test):
    logger.info("Iniciando prueba de inferencia con ejemplos manuales...")
    
    # Enviar el modelo al hardware correcto (GPU/MPS/CPU)
    model_test.to(device)
    
    # IMPORTANTE: Poner el modelo en modo evaluación. 
    # Esto desactiva capas como Dropout que solo se usan en entrenamiento.
    model_test.eval()

    print("\n" + "="*60)
    print("🎯 RESULTADOS DE LA PRUEBA MANUAL")
    print("="*60)

    # torch.no_grad() le dice a PyTorch que no calcule gradientes. 
    # Acelera el proceso y ahorra mucha memoria porque ya no estamos entrenando.
    with torch.no_grad(): 
        for texto_original in textos:
            # A. Aplicar la misma limpieza que en el dataset original
            texto_limpio = process_text(texto_original)
            
            # B. Tokenizar el texto y convertirlo a tensores de PyTorch ("pt")
            inputs = tokenizer_test(
                texto_limpio, 
                return_tensors="pt", 
                truncation=True, 
                padding=True, 
                max_length=MAX_LENGTH
            )
            
            # Enviar los tensores al mismo dispositivo que el modelo
            inputs = {k: v.to(device) for k, v in inputs.items()}
            
            # C. Pasar los tensores por el modelo
            outputs = model_test(**inputs)
            logits = outputs.logits
            
            # D. Aplicar Softmax para convertir los logits puros en probabilidades (0 a 1)
            probs = torch.nn.functional.softmax(logits, dim=-1)
            
            # Obtener el ID de la clase con mayor probabilidad y su valor
            pred_id = torch.argmax(probs, dim=-1).item()
            confianza = probs[0][pred_id].item()
            
            # Mapear el ID de vuelta a texto usando tu diccionario ID2LABEL
            etiqueta = ID2LABEL[pred_id]
            
            # Imprimir resultados
            print(f"📝 Texto original: '{texto_original}'")
            print(f"🤖 Predicción:     {etiqueta} (Confianza: {confianza:.2%})\n")

# ---------------------------------------------------------
# 4. EJECUCIÓN PRINCIPAL
# ---------------------------------------------------------
if __name__ == "__main__":
    start_time = time.perf_counter()
    logger.info("Iniciando ejecución del script de entrenamiento.")
    
    df_raw = read_tripadvisor_data(DATA_DIR)
    df_raw = proccess_dataset(df_raw)

    logger.info(f"Dataset final listo para entrenamiento: {len(df_raw)} filas. Distribución de clases:\n{df_raw['label'].value_counts()}")
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
    for layer in model.roberta.encoder.layer[-capas_a_entrenar:]:
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
        eval_strategy="epoch",
        save_strategy="epoch",
        learning_rate=LR,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        gradient_accumulation_steps=4,
        num_train_epochs=EPOCHS,
        weight_decay=0.01,
        load_best_model_at_end=True,
        metric_for_best_model="f1",
        bf16=use_bf16, # Controlado dinámicamente por la detección de hardware
        logging_dir='./logs',
        logging_steps=10, # Mostramos métricas cada 10 steps
    )

    logger.info("Calculando pesos de clase para combatir el desbalance...")
    # Creamos una lista de enteros temporal solo para calcular los pesos
    temp_labels = df_raw["etiqueta"].map({"NON-SUGGESTION": 0, "SUGGESTION": 1}).tolist()
    
    weights = compute_class_weight("balanced", classes=np.unique(temp_labels), y=temp_labels)
    logger.info(f"Pesos calculados: NON-SUGGESTION={weights[0]:.4f}, SUGGESTION={weights[1]:.4f}")

    logger.info("Inicializando CustomTrainer con pesos balanceados...")
    trainer = CustomTrainer(
        class_weights=weights,
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
    trainer.save_model("./matusalem")
    tokenizer.save_pretrained("./matusalem")
    logger.info("Proceso completado exitosamente.")

    # Lista de ejemplos representativos para poner a prueba tu NLU
    ejemplos_prueba = [
        # 1. Debería ser SUGGESTION
        "The hotel was nice but it would be great if you could add more vegan options to the breakfast.", 
        
        # 2. Debería ser NON-SUGGESTION (Es un simple cumplido)
        "I loved the location, the bed was very comfortable and the staff was friendly.", 
        
        # 3. Debería ser NON-SUGGESTION (Es una queja sin propuesta de mejora)
        "Terrible experience, the AC was broken all night and nobody helped us.", 
        
        # 4. Debería ser SUGGESTION (Proponiendo una acción concreta)
        "You should consider putting a mini fridge in the rooms, it gets very hot in the summer.",

        # 5. Debería ser NON-SUGGESTION 
        "The visit was lovely, the music at the night was great, and the boat trips were fantastic. I would recommend bringing snacks, as the trip is long, and my family and I got hungry along the way.",

        # 6. Debería ser SUGGESTION (Propuesta de mejora concreta)
        "I liked Camila, she was a very guide but the trip was very long, bring food and battery on your cell phone for everyone"
    ]

    # Ejecutar la prueba
    probar_ejemplos(ejemplos_prueba, model, tokenizer)