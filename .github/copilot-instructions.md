# Co### Estructura del Proyecto
- **Documento principal**: `main.tex`
- **Plantilla de estilo**: `pucv_inf_2024.sty`
- **Portada**: `common/portada.tex`
- **Contenido**: `content/` (abstract.tex, introduction.tex)
- **Referencias**: `referencias.bib`
- **Glosario**: `glosario.tex`
- **Proyecto secundario**: `registration_formulation/` - Bases temporales para presentación de seminario de títulonstructions - Seminario de Título

## Información del Proyecto

### Estructura del Proyecto
- **Documento principal**: `main.tex`
- **Plantilla de estilo**: `pucv_inf_2024.sty`
- **Portada**: `common/front-page.tex`
- **Contenido**: `content/` (abstract.tex, introduction.tex)
- **Referencias**: `references.bib`
- **Glosario**: `glossary.tex`

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
