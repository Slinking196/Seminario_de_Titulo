# Copilot Instructions - Seminario de Título

## Información del Proyecto

### Descripción del Proyecto
El proyecto "Análisis de la Experiencia del Turista" se centra en investigar cómo los turistas interactúan con aplicaciones web durante sus viajes y cómo estas plataformas afectan su experiencia general. El proyecto comprende:

- **Webscraping**: Recopilación automatizada de opiniones, reseñas y comentarios de turistas en diversas plataformas.
- **Análisis con IA**: Uso de modelos supervisados y no supervisados para etiquetar, categorizar y analizar datos de experiencias turísticas.
- **UX Research**: Investigación sobre técnicas para mejorar la experiencia del usuario en aplicaciones turísticas.
- **Optimización**: Desarrollo de recomendaciones para mejorar las plataformas digitales del sector turístico.

El objetivo principal es entender los factores que influyen en la satisfacción del turista con las herramientas digitales y proponer mejoras que beneficien tanto a los viajeros como a las empresas del sector.

### Estructura del Proyecto
- **Documento principal (Tesis)**: `tesis/main.tex`
- **Plantilla de estilo de la tesis**: `tesis/pucv_inf_2024.sty`
- **Portada de la tesis**: `tesis/Portadas/portada_principal.tex`
- **Contenido de la tesis**: `tesis/body/`
  - `abstract.tex`
  - `introduction.tex`
  - `theoretical_framework.tex`
  - `objectives.tex`
- **Referencias de la tesis**: `tesis/references.bib`
- **Glosario de la tesis**: `tesis/glossary.tex`
- **PDFs con reglas de seminario**: `pdfs/seminar_info` (contiene documentos PDF con las reglas del seminario de título)
- **PDFs de Papers de Referencia**: `pdfs/papers` o `markdowns/papers` (contiene documentos PDF de referencia para el seminario de título)
- **Análisis de Datos**: `data_analysis/` (notebooks y scripts para análisis de datos)

### Configuración de LaTeX
- **Distribución**: TeX Live 2025 (versión básica)
- **Compilador**: pdflatex
- **Bibliografía**: biblatex con estilo APA
- **Fuente**: Times New Roman
- **Tamaño de página**: Letter (12pt)

### Paquetes Instalados
- titlesec
- algorithms, algorithmicx
- makecell
- glossaries
- nomencl
- biblatex, biblatex-apa
- enumitem
- caption
- lipsum
- pdfpages

### Configuración VS Code
- **LaTeX Workshop**: Configurado para compilación automática
- **Live Share**: Listo para colaboración
- **Salida**: PDF en directorio `out/`

### Comandos de Portada Definidos
- `\membrete{}`: Encabezado de la universidad
- `\tituloPortada{}`: Título principal
- `\alumnos{}`: Lista de estudiantes
- `\datosPortada{}`: Contenedor de datos
- `\datoPortada{}{}: Par clave-valor
- `\fechaPortada{}`: Fecha del documento

### Autores del Proyecto
- Fabrizzio Andrés Mura Lavarello
- Matías Hernán Bugueño Bugueño

### Notas Importantes
- El documento usa la clase `report` para soporte de capítulos
- La numeración romana se usa para páginas preliminares
- Los índices están activados (contenido, figuras, tablas, glosario)
- La portada está optimizada para caber en una página
- **Proyecto dual**: 
  - Directorio raíz: Documento final del seminario de título
  - `registration_formulation/`: Bases temporales para la presentación inicial del seminario

### Tecnologías y Métodos de Investigación
- **Webscraping**: Python con BeautifulSoup, Scrapy
- **Procesamiento de Lenguaje Natural**: NLTK, spaCy, Transformers
- **Análisis de Sentimientos**: BERT, RoBERTa
- **Clustering y Clasificación**: Scikit-learn, TensorFlow
- **Visualización de Datos**: Matplotlib, Seaborn, Tableau

### Comandos de Compilación
```bash
pdflatex main.tex
biber main  # Para bibliografía
makeglossaries main  # Para glosario
pdflatex main.tex  # Segunda pasada
```

### Configuración para Live Share
- Audio habilitado
- Sin requerimiento de aprobación de invitados
- Compilación automática al cambiar archivos
- Visor PDF en pestaña de VS Code

---
*Última actualización: 6 de agosto de 2025*
