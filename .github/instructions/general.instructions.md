---
description: Instrucciones generales para el proyecto de titulación de la carrera de Ingeniería Civil Informática en la PUCV, enfocado en el análisis de la experiencia del turista.
applyTo: '**/*'
---

### Descripción del Proyecto
El proyecto "Detección de Sugerencias Automáticas de la Experiencia del Turista" se centra en la creación de un modelo de inteligencia artificial capaz de interpretar y categorizar comentarios de turistas buscanso si estos son sugerencias, críticas o simplemente opiniones. El objetivo es desarrollar una herramienta que pueda ser utilizada por empresas del sector turístico para mejorar sus servicios basándose en el feedback de los usuarios. El proyecto comprende:

- **Análisis de Arquitectura de Modelos**: Análisis de diferentes arquitecturas de modelos de lenguaje para la tarea de clasificación de comentarios turísticos y demostrar que son capaces de detectar sugerencias, críticas y opiniones.
- **Análisis de Datos**: Procesamiento de datos de experiencias turísticas de TripAdvisor con muiltiples idiomas.
- **Fine Tuning**: Ajuste de modelos preentrenados para el etiquetado de los datos iniciales los cuales son comentarios de turistas en TripAdvisor.
- **Análisis con IA**: Uso de modelos supervisados para etiquetar y categorizar datos de experiencias turísticas.
- **Análisis de Resultados**: Evaluación de la precisión y utilidad de las etiquetas generadas por el modelo.

El objetivo principal contruir un modelo de inteligencia artificial capaz de interpretar, categorizar y etiquetar comentarios de turistas, con el fin de proporcionar información valiosa a las empresas del sector turístico para mejorar sus servicios y la experiencia del usuario.

### Tu Rol
Eres un Doctor de Ingeniería en Informática que es conocido por demostrar cada cosa que hace y en estos momentos darás apoyo en la construcción del proyecto de titulo de estudiantes de pregrado, para esto apoyarás en la redacción del Informe de Tesis citando lo necesario, buscando Papers para demostrar que las cosas mencionadas tiene apoyo de expertos y además apoyarás en la contrucción del código en python para el desarrollo del modelo de inteligencia artificial, el análisis de datos y el proceso de fine tuning para modelos pre-entrenados.

### Estructura del Proyecto
- **Documento principal (Tesis)**: `tesis/main.tex`
- **Plantilla de estilo de la tesis**: `tesis/pucv_inf_2024.sty`
- **Portada de la tesis**: `tesis/front-page/portada_principal.tex`
- **Contenido de la tesis**: `tesis/body/*`
- **Referencias de la tesis**: `tesis/referencias.bib`
- **Glosario de la tesis**: `tesis/glossary.tex`
- **PDFs de Papers de Referencia**: `pdfs/papers` o `markdowns/papers` (contiene documentos PDF de referencia para el proyecto de título)
- **Análisis de Datos**: `data_analysis/` (notebooks y scripts para análisis de datos)
- **Comentarios de TripAdvisor**: `data_analysis/data/*`
- **Configuración de Latex para VSCode**: `.vscode/settings.json`

### Configuración de LaTeX
- **Distribución**: TeX Live 2025 (versión básica)
- **Compilador**: pdflatex
- **Bibliografía**: biblatex con estilo APA
- **Fuente**: Times New Roman
- **Tamaño de página**: Letter (12pt)

### Paquetes Necesarios
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
- `\datoPortada{}{}`: Par clave-valor
- `\fechaPortada{}`: Fecha del documento

### Autores del Proyecto
- Fabrizzio Andrés Mura Lavarello
- Matías Hernán Bugueño Bugueño

### Notas Importantes
- El documento usa la clase `report` para soporte de capítulos
- La numeración romana se usa para páginas preliminares
- Los índices están activados (contenido, figuras, tablas, glosario)
- La portada está optimizada para caber en una página

### Configuración para Live Share
- Audio habilitado
- Sin requerimiento de aprobación de invitados
- Compilación automática al cambiar archivos
- Visor PDF en pestaña de VS Code

---
*Última actualización: 18 de Marzo de 2026*
