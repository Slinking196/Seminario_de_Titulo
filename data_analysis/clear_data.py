from langdetect import detect, DetectorFactory
import pandas as pd
import os

def read_tripadvisor_data(path: str) -> pd.DataFrame:
    df = pd.DataFrame()
    size = len(os.listdir(path))

    for i in range(1, size + 1):
        file_path = os.path.join(path, f"Chile_all1_part{i}.csv")
        df = pd.concat([df, pd.read_csv(file_path, sep=';')], ignore_index=True)

    return df

def safe_detect(text):
    if not isinstance(text, str) or not text.strip():
        return 'unknown'
    try:
        return detect(text)
    except Exception:
        return 'unknown'

def filter_language_reviews(
        df: pd.DataFrame, 
        languages: tuple = ('es',), 
        text_col: str | None = None
) -> pd.DataFrame:
    """
    Filtra reseñas por uno o varios idiomas usando langdetect.
    - df: DataFrame original
    - languages: iterable de códigos de idioma (p. ej., ('es', 'en')); también acepta string único
    - text_col: nombre de la columna de texto (si None, intenta 'review_text' y luego 'Review')

    Retorna un nuevo DataFrame filtrado (copia).
    """
    # Reproducibilidad
    DetectorFactory.seed = 0

    # Selección de columna de texto
    if text_col is None:
        if 'review_text' in df.columns:
            text_col = 'review_text'
        elif 'Review' in df.columns:
            text_col = 'Review'
        else:
            raise ValueError("No se encontró la columna de reviews")
        
    lang_set = set(languages)

    tmp_lang = df[text_col].apply(safe_detect)
    mask = tmp_lang.isin(lang_set)
    filtered_df = df[mask].copy()
    return filtered_df

if __name__ == "__main__":
    DetectorFactory.seed = 0

    print('Leyendo datos...')
    df = read_tripadvisor_data('./data_analysis/data')
    print('Datos leídos.')

    # Asegurar existencia de la columna
    if 'review_text' not in df.columns:
        raise ValueError("La columna 'review_text' no existe en el DataFrame.")

    print('Primer filtrado de lenguaje...')
    df['language'] = df['review_text'].apply(safe_detect)
    filtered_df = df[df['language'].isin(['es', 'en'])].copy()
    print('Total original:', len(df))
    print('Filtrados (es/en):', len(filtered_df))
    print(filtered_df['language'].value_counts())
    print('Primer filtrado de lenguaje completado.')

    print('\nSegundo filtrado de lenguaje usando función...')
    df_2 = read_tripadvisor_data('./data_analysis/data')
    filtered_df_2 = filter_language_reviews(df_2, languages=('es', 'en'), text_col='review_text')
    print('Total original:', len(df_2))
    print('Filtrados (es/en):', len(filtered_df_2))
    print(filtered_df_2['language'].value_counts())
    print('Segundo filtrado de lenguaje completado.')