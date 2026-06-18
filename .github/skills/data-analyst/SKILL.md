---
name: data-analyst
description: Analista de Datos Senior especializado en análisis exploratorio, limpieza y validación de datasets de experiencias turísticas (TripAdvisor). Manejo de datos multiidioma, detección de patrones, visualización exploratoria y generación de reportes estadísticos. **Cuándo usar**: exploración de datos, calidad y limpieza de CSV, análisis estadístico, detección de anomalías, visualización de patrones, preparación de datasets para ML, y documentación de insights.
---

## Descripción General

Esta skill empodera al agente para actuar como **Analista de Datos Senior** en análisis de experiencias turísticas de TripAdvisor. Proporciona guía experta para:

- **Exploración de datos (EDA)**: análisis estadístico descriptivo, distribuciones, correlaciones
- **Limpieza y preprocesamiento**: detección de missing values, outliers, normalización, codificación
- **Validación de calidad**: integridad de datos, inconsistencias, valores duplicados
- **Análisis multiidioma**: manejo de texto en múltiples idiomas, detección de encoding
- **Visualización exploratoria**: gráficos informativos para identificar patrones y anomalías
- **Documentación de insights**: reportes reproducibles con narrativa y recomendaciones
- **Preparación para ML**: generación de features, balanceo de clases, split train/test

---

## Cuándo Invocar Esta Skill

Usa esta skill cuando el usuario o task pida:
- "Analiza el dataset de TripAdvisor y dame un resumen estadístico" → EDA completo
- "Limpia los datos CSV y detecta valores faltantes" → Data Cleaning
- "¿Cuál es la distribución de ratings y comentarios por idioma?" → Análisis descriptivo
- "Genera visualizaciones de los patrones principales en los comentarios" → EDA visualization
- "Prepara los datos para entrenar un modelo de clasificación" → Data Preparation
- "Encuentra anomalías y valores duplicados en los datos" → Data Quality Validation
- "Crea un reporte ejecutivo con los hallazgos principales" → Documentación e Insights

---

### Verificar Prerequisites (Comandos para el usuario)

```bash
# Comprobar Python
python3 --version

# Instalar librerías (si no las tienes)
pip install pandas numpy matplotlib seaborn scipy scikit-learn openpyxl

# Verificar instalación
python3 -c "import pandas; print('Pandas OK')"
```

---

## Flujo de Trabajo Fase por Fase

### Fase 1: Inspección Inicial del Dataset

Cuando se inicia una tarea de análisis:

1. **Cargar y revisar estructura:**
   ```python
   import pandas as pd
   df = pd.read_csv('data_analysis/data/Chile_all1_part1.csv')
   print(f"Shape: {df.shape}")  # Filas y columnas
   print(df.head())             # Primeras filas
   print(df.info())             # Tipos de datos
   print(df.columns)            # Nombres de columnas
   ```

2. **Verificar columnas principales:**
   - ¿Existen columnas: `rating`, `comment`, `language`, `date`, `reviewer`, `title`?
   - ¿Qué tipos de datos tiene cada columna?
   - ¿Cuáles son las columnas relevantes para el análisis?

3. **Detectar anomalías iniciales:**
   - Missing values: `df.isnull().sum()`
   - Duplicados: `df.duplicated().sum()`
   - Tamaño del dataset: `len(df)` registros
   - Rango de dates: `df['date'].min()` a `df['date'].max()`

### Fase 2: Análisis Exploratorio (EDA)

**Estadísticas Descriptivas:**

```python
# Resumen numérico
df.describe()

# Conteos por categoria
df['language'].value_counts()
df['rating'].value_counts().sort_index()

# Distribución de longitud de comentarios
df['comment'].str.len().describe()
```

**Análisis por Idioma:**

```python
# Detectar idiomas (si existe columna)
print(df['language'].unique())
print(df['language'].value_counts())

# Estadísticas por idioma
for lang in df['language'].unique():
    subset = df[df['language'] == lang]
    print(f"\n{lang}:")
    print(f"  Registros: {len(subset)}")
    print(f"  Rating promedio: {subset['rating'].mean():.2f}")
    print(f"  Comentarios con texto: {subset['comment'].notna().sum()}")
```

**Correlaciones y Relaciones:**

```python
# Correlación entre rating y longitud de comentario
df['comment_length'] = df['comment'].str.len()
correlation = df['rating'].corr(df['comment_length'])
print(f"Correlación rating ~ longitud: {correlation:.3f}")

# Ratings por idioma
df.groupby('language')['rating'].agg(['mean', 'std', 'count'])
```

### Fase 3: Detección de Calidad de Datos

**Missing Values:**

```python
# Detectar y visualizar
missing = df.isnull().sum()
print(missing[missing > 0])

# Porcentaje de missing por columna
missing_pct = (df.isnull().sum() / len(df)) * 100
print(missing_pct[missing_pct > 0])

# Decisión: eliminar o imputar según criticidad
# Si rating ausente → descartar fila
# Si comment ausente → marcar como 'NO_TEXT'
```

**Duplicados:**

```python
# Detectar filas idénticas
duplicates = df.duplicated(subset=['reviewer', 'date', 'comment'], keep=False)
print(f"Duplicados detectados: {duplicates.sum()}")

# Revisar los duplicados
print(df[duplicates].sort_values(['reviewer', 'date']))
```

**Outliers y Anomalías:**

```python
# Ratings fuera de rango esperado (1-5)
invalid_ratings = df[(df['rating'] < 1) | (df['rating'] > 5)]
print(f"Ratings inválidos: {len(invalid_ratings)}")

# Comentarios muy cortos o muy largos
df['comment_length'] = df['comment'].str.len()
short = df[df['comment_length'] < 10]
long = df[df['comment_length'] > 5000]
print(f"Comentarios muy cortos: {len(short)}, muy largos: {len(long)}")
```

**Encoding y Caracteres Especiales:**

```python
# Detectar problemas de encoding
def check_encoding_issues(s):
    try:
        s.encode('utf-8').decode('utf-8')
        return False
    except:
        return True

encoding_issues = df['comment'].apply(check_encoding_issues).sum()
print(f"Posibles problemas de encoding: {encoding_issues}")
```

### Fase 4: Limpieza y Normalización

**Script de Limpieza Estándar:**

```python
def clean_dataframe(df):
    # 1. Eliminar filas sin rating
    df = df[df['rating'].notna()]
    
    # 2. Eliminar duplicados exactos
    df = df.drop_duplicates(subset=['reviewer', 'date', 'comment'], keep='first')
    
    # 3. Validar ratings (1-5)
    df = df[(df['rating'] >= 1) & (df['rating'] <= 5)]
    
    # 4. Normalizar comentarios vacíos
    df['comment'] = df['comment'].fillna('').str.strip()
    
    # 5. Normalizar espacios en blanco
    df['comment'] = df['comment'].str.replace(r'\s+', ' ', regex=True)
    
    # 6. Normalizar dates a datetime
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    # 7. Eliminar filas con dates inválidas
    if 'date' in df.columns:
        df = df[df['date'].notna()]
    
    return df

df_clean = clean_dataframe(df)
print(f"Registros originales: {len(df)}, tras limpieza: {len(df_clean)}")
```

### Fase 5: Visualización Exploratoria

**Gráficos Esenciales:**

```python
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Distribución de ratings
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
df_clean['rating'].hist(ax=axes[0], bins=5, edgecolor='black')
axes[0].set_title('Distribución de Ratings')
axes[0].set_xlabel('Rating')
axes[0].set_ylabel('Frecuencia')

# 2. Ratings por idioma
df_clean.groupby('language')['rating'].mean().sort_values().plot(
    kind='barh', ax=axes[1], color='steelblue'
)
axes[1].set_title('Rating Promedio por Idioma')
axes[1].set_xlabel('Rating Promedio')

plt.tight_layout()
plt.savefig('data_analysis/exploratory_plots.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Longitud de comentarios
fig, ax = plt.subplots(figsize=(10, 4))
df_clean['comment_length'] = df_clean['comment'].str.len()
df_clean['comment_length'].hist(ax=ax, bins=50, edgecolor='black')
ax.set_title('Distribución de Longitud de Comentarios')
ax.set_xlabel('Caracteres')
ax.set_ylabel('Frecuencia')
plt.savefig('data_analysis/comment_length_dist.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Box plot de ratings por idioma
fig, ax = plt.subplots(figsize=(10, 5))
df_clean.boxplot(column='rating', by='language', ax=ax)
ax.set_title('Distribución de Ratings por Idioma')
ax.set_xlabel('Idioma')
ax.set_ylabel('Rating')
plt.suptitle('')  # Eliminar título automático
plt.savefig('data_analysis/rating_by_language_boxplot.png', dpi=300, bbox_inches='tight')
plt.close()
```

### Fase 6: Documentación y Reporte

**Generar Reporte Ejecutivo:**

```python
# Crear reporte en formato texto
reporte = f"""
=== REPORTE DE ANÁLISIS EXPLORATORIO (EDA) ===
Proyecto: Detección de Sugerencias en Experiencias Turísticas
Fecha: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}

1. RESUMEN GENERAL
---
Total de registros: {len(df_clean)}
Registros eliminados en limpieza: {len(df) - len(df_clean)}
Período de datos: {df_clean['date'].min()} a {df_clean['date'].max()}

2. ESTADÍSTICAS DE RATINGS
---
Rating promedio: {df_clean['rating'].mean():.2f}
Desviación estándar: {df_clean['rating'].std():.2f}
Rating mín/máx: {df_clean['rating'].min()}/{df_clean['rating'].max()}
Distribución:
{df_clean['rating'].value_counts().sort_index().to_string()}

3. ANÁLISIS POR IDIOMA
---
"""

for lang in sorted(df_clean['language'].unique()):
    subset = df_clean[df_clean['language'] == lang]
    reporte += f"""
{lang}:
  - Registros: {len(subset)}
  - Rating promedio: {subset['rating'].mean():.2f}
  - Comentarios con texto: {(subset['comment'] != '').sum()}
  - Longitud promedio: {subset['comment'].str.len().mean():.0f} caracteres
"""

reporte += f"""

4. CALIDAD DE DATOS
---
Missing values: {df_clean.isnull().sum().sum()}
Duplicados: {df_clean.duplicated().sum()}
Comentarios vacíos: {(df_clean['comment'] == '').sum()}

5. RECOMENDACIONES
---
- Revisar comentarios muy cortos (< 10 caracteres)
- Validar encoding en comentarios con caracteres especiales
- Considerar balanceo de clases si hay desproporción en ratings
"""

with open('data_analysis/EDA_reporte.txt', 'w', encoding='utf-8') as f:
    f.write(reporte)

print(reporte)
```

### Fase 7: Preparación para Modelado

**Feature Engineering Básico:**

```python
def prepare_for_modeling(df):
    df_model = df.copy()
    
    # 1. Agregar features de texto
    df_model['comment_length'] = df_model['comment'].str.len()
    df_model['word_count'] = df_model['comment'].str.split().str.len()
    df_model['sentence_count'] = df_model['comment'].str.count(r'[.!?]')
    
    # 2. One-hot encoding de idioma
    language_dummies = pd.get_dummies(df_model['language'], prefix='lang')
    df_model = pd.concat([df_model, language_dummies], axis=1)
    
    # 3. Normalizar features numéricos
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    numeric_cols = ['comment_length', 'word_count', 'sentence_count']
    df_model[numeric_cols] = scaler.fit_transform(df_model[numeric_cols])
    
    # 4. Seleccionar columnas para modelo
    model_cols = ['rating'] + numeric_cols + list(language_dummies.columns)
    df_model = df_model[model_cols + ['comment', 'date']]  # Mantener comment para referencia
    
    return df_model, scaler

df_model, scaler = prepare_for_modeling(df_clean)
print(f"Dataset preparado para modelado: {df_model.shape}")
print(df_model.head())
```

---

## Estructura Esperada de Datos (TripAdvisor)

La mayoría de datasets de TripAdvisor tienen esta estructura:

| Columna | Tipo | Descripción | Ejemplo |
|---------|------|-------------|---------|
| `reviewer` | str | Nombre del revisor | "John D." |
| `rating` | int | Calificación (1-5) | 4 |
| `date` | datetime | Fecha de la reseña | 2023-05-15 |
| `title` | str | Título de la reseña | "Great experience!" |
| `comment` | str | Texto completo de la reseña | "Loved the service and..." |
| `language` | str | Idioma detectado o especificado | "en", "es", "fr" |
| `location` | str | Lugar/atracción (opcional) | "Hotel Valparaíso" |
| `visited_date` | datetime | Fecha de la visita (opcional) | 2023-05-10 |

**Archivos esperados en `data_analysis/data/`:**
- `Chile_all1_part1.csv` a `Chile_all1_part12.csv` (o similar)
- Posibilidad de múltiples idiomas en una sola columna o separados

---

## Checklist de Análisis Completado

Antes de marcar una tarea de análisis como completada:

- [ ] Dataset cargado y estructura verificada
- [ ] Estadísticas descriptivas generadas (min, max, mean, std)
- [ ] Missing values y duplicados detectados y reportados
- [ ] Outliers identificados y clasificados
- [ ] Limpiezadeejecutada (sin valores faltantes críticos, sin duplicados)
- [ ] Análisis por idioma completado (si aplica)
- [ ] Visualizaciones generadas (al menos 4: distribution, by-language, length, anomalies)
- [ ] Reporte ejecutivo creado (con insights y recomendaciones)
- [ ] Datos preparados para siguiente fase (ML o fine-tuning)
- [ ] Documentación guardada en `data_analysis/` con extensión `.md` o `.txt`

---

## Solución de Problemas Comunes

| Problema | Causa | Solución |
|----------|-------|----------|
| `UnicodeDecodeError` al cargar CSV | Encoding no es UTF-8 | Probar `encoding='latin-1'` o `encoding='iso-8859-1'` |
| `MemoryError` con archivos muy grandes | Dataset supera memoria RAM | Usar `chunksize=10000` en `pd.read_csv()` para procesar en bloques |
| NaN infinitos en cálculos | Division por cero o valores missing | Usar `df.fillna(0)` o `df.dropna()` antes de cálculos |
| Gráficos no se guardan | Ruta incorrecta o carpeta no existe | Crear carpeta con `os.makedirs('data_analysis', exist_ok=True)` primero |
| Fechas mal interpretadas | Formato de fecha no reconocido | Especificar `format='%d/%m/%Y'` en `pd.to_datetime()` |
| Idioma no detectado automáticamente | Necesita librería externa | Usar `langdetect` o `textblob` (`pip install langdetect`) |
| Caracteres acentuados corruptos | Encoding del archivo vs Python | Verificar encoding con `file -i filename.csv`; abrir en editor y resguardar UTF-8 |

---

## Herramientas y Librerías Recomendadas

| Librería | Función | Comando Instalación |
|----------|---------|-------------------|
| `pandas` | Manipulación de datos | `pip install pandas` |
| `numpy` | Operaciones numéricas | `pip install numpy` |
| `matplotlib` | Gráficos estáticos | `pip install matplotlib` |
| `seaborn` | Gráficos estadísticos | `pip install seaborn` |
| `scipy` | Estadística avanzada | `pip install scipy` |
| `scikit-learn` | ML y validación | `pip install scikit-learn` |
| `langdetect` | Detección de idioma | `pip install langdetect` |
| `openpyxl` | Exportar a Excel | `pip install openpyxl` |

---

## Ejemplos de Uso

### Ejemplo 1: Exploración Rápida de Un CSV

**Prompt para el agente:**
> "Analiza el archivo `Chile_all1_part1.csv` y dame un resumen: cantidad de registros, rating promedio, idiomas presentes y missing values."

**Acciones esperadas:**
1. Cargar CSV con pandas
2. Generar `df.info()`, `df.describe()`, `df.isnull().sum()`
3. Listar valores únicos de `language`
4. Reportar findings en formato tabla

### Ejemplo 2: Detectar y Limpiar Duplicados

**Prompt:**
> "Encuentra duplicados en el dataset de TripAdvisor y proporciona un script limpio para eliminarlos sin perder datos importantes."

**Acciones esperadas:**
1. Ejecutar `df.duplicated()` con combinaciones de columnas relevantes
2. Mostrar muestras de duplicados encontrados
3. Proporcionar script de limpieza reproducible
4. Validar que após limpieza, no hay duplicados

### Ejemplo 3: Visualizaciones para Reporte

**Prompt:**
> "Crea 4 visualizaciones para el reporte EDA: ratings, distribución por idioma, longitud de comentarios y análisis de anomalías."

**Acciones esperadas:**
1. Generar `distribution_ratings.png`
2. Generar `rating_by_language.png`
3. Generar `comment_length_distribution.png`
4. Generar `anomalies_heatmap.png`
5. Guardar en `data_analysis/plots/`

---

## Scripts Reutilizables

### Script 1: Cargar y Explorar Múltiples CSVs

```python
import os
import pandas as pd

data_dir = 'data_analysis/data/'
all_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]

for file in sorted(all_files):
    df = pd.read_csv(os.path.join(data_dir, file))
    print(f"\n{file}: {df.shape[0]} registros, missing: {df.isnull().sum().sum()}")
```

### Script 2: Consolidar Múltiples CSVs

```python
import os
import pandas as pd

data_dir = 'data_analysis/data/'
dfs = []

for file in sorted(os.listdir(data_dir)):
    if file.endswith('.csv'):
        df = pd.read_csv(os.path.join(data_dir, file))
        dfs.append(df)

df_consolidated = pd.concat(dfs, ignore_index=True)
df_consolidated.to_csv('data_analysis/consolidated_data.csv', index=False)
print(f"Datos consolidados: {df_consolidated.shape}")
```

---

## Referencias y Contexto del Proyecto

- **Datos**: `data_analysis/data/` (múltiples CSVs de TripAdvisor)
- **Scripts disponibles**: `data_analysis/preprocesing_data.ipynb`, `data_analysis/clear_data.py`
- **Notebook de análisis**: `data_analysis/tx_experience_analysis.ipynb`
- **Objetivo final**: Preparar datos para fine-tuning de modelos de clasificación de sugerencias/críticas

---

## Versión y Mantenimiento

- **Versión**: 0.1 → Basada en pandas, numpy, matplotlib, scikit-learn
- **Última actualización**: 18 de Marzo de 2026
- **Autores del proyecto**: Fabrizzio Andrés Mura Lavarello, Matías Hernán Bugueño Bugueño

**Mejoras futuras:**
- Integración con herramientas de perfilamiento automático (pandas-profiling)
- Detección automática de idioma con modelos preentrenados
- Análisis de sentimiento preliminary antes del modelado
- Exportación automática de reportes en formato HTML