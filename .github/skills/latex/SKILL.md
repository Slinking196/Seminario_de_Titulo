---
name: latex
description: Experto en construcción, compilación y mantenimiento de proyectos LaTeX. Especializado en tesis académicas con TeX Live 2025, pdflatex, biblatex-apa, portadas personalizadas y compilación automática. **Cuándo usar**: redacción de capítulos, revisión de referencias, compilación de PDFs, resolución de errores LaTeX, gestión de bibliografía, y optimización de estructura de proyectos.
---

## Descripción General

Esta skill empodera al agente para actuar como **experto en LaTeX** en contextos de tesis académicas. Proporciona guía experta para:

- **Compilación robusta**: pdflatex + biblatex-apa + índices automáticos
- **Estructura de tesis**: portadas PUCV, capítulos organizados, references, glosario
- **Resolución de errores**: diagnóstico de fallos de compilación y conflictos de paquetes
- **Buenas prácticas**: normalización de código fuente, versionado limpio, integración con CI
- **Automatización**: latexmk, GitHub Actions, compilación reproducible en entornos diversos

---

## Cuándo Invocar Esta Skill

Usa esta skill cuando el usuario o task pida:
- "Compila la tesis y dime los errores" → Skill LaTeX ejecuta compilación
- "Revisa la bibliografía y resolve missing references" → Skill LaTeX inspecciona `referencias.bib` y `main.tex`
- "Crea un capítulo nuevo con la estructura correcta" → Skill LaTeX sugiere plantilla y validación
- "Genera un PDF limpio en `out/`" → Skill LaTeX garantiza compilación exitosa
- "¿Por qué el glosario no aparece?" → Skill LaTeX diagnostica y propone soluciones
- "Implementa GitHub Actions para compilar PDFs automáticamente" → Skill LaTeX crea workflow

---

## Prerequisites

- **TeX Live 2025 (basic)** instalado en la máquina
- **pdflatex**, **biber** (para biblatex), **makeindex** (para glosario)
- **VSCode** con extensión **LaTeX Workshop**
- Acceso al repositorio en `.github/skills/latex/` y `tesis/`

### Verificar Prerequisites (Comandos para el usuario)

```bash
# Comprobar TeX Live
pdflatex --version

# Comprobar biber
biber --version

# Comprobar makeindex
makeindex --version
```

---

## Flujo de Trabajo Fase por Fase

### Fase 1: Inspección Inicial

Cuando se inicia una tarea LaTeX:

1. **Leer la estructura del proyecto:**
   - `tesis/main.tex` (punto de entrada principal)
   - `tesis/pucv_inf_2024.sty` (estilos personalizados PUCV)
   - `tesis/front-page/portada_principal.tex` (portada)
   - `tesis/body/*.tex` (capítulos)
   - `tesis/referencias.bib` (bibliografía)
   - `tesis/glossary.tex` (glosario, si existe)

2. **Verificar configuración en `main.tex`:**
   - ¿Se carga `pucv_inf_2024.sty`?
   - ¿Está configurado `biblatex` con estilo APA?
   - ¿Se usan comandos personalizados de portada (`\membrete`, `\alumnos`, etc.)?
   - ¿Existen archivos de entrada (`\input` o `\include`)?

3. **Revisar `.vscode/settings.json`:**
   - ¿LaTeX Workshop está activado?
   - ¿El directorio de salida es `out/`?
   - ¿Las tareas de compilación están definidas?

### Fase 2: Validación del Entorno  

Confirmar que LaTeX y herramientas están disponibles:

```bash
# Test rápido de compilación (desde carpeta tesis/)
pdflatex --version 2>&1 | head -1
biber --version 2>&1 | head -1
```

Si falta alguna herramienta → sugerir instalación según SO del usuario (macOS: `brew install --cask mactex` o `macports` + `latexmk`).

### Fase 3: Compilación Segura

**Comando estándar recomendado:**

```bash
cd tesis/
latexmk -pdf -silent -outdir=out main.tex
```

**Si `latexmk` no está disponible, usar secuencia manual:**

```bash
cd tesis/
pdflatex -interaction=nonstopmode -output-directory=out main.tex
biber out/main
pdflatex -interaction=nonstopmode -output-directory=out main.tex
pdflatex -interaction=nonstopmode -output-directory=out main.tex
```

**Capturar salida y clasificar errores:**
- **Error crítico** (PE): `! Undefined control sequence`, `! File not found`, `! Missing package`  
- **Warning**: `Overfull \hbox`, `Citation not found`, `Undefined reference`
- **Info**: `LaTeX Font Warning`, `Package info notices`

### Fase 4: Diagnóstico y Corrección

Si la compilación falla:

1. **Leer el archivo `.log` generado** (p.ej., `out/main.log`)
2. **Identificar línea del error**: "l.234 —" indica línea 234 donde ocurrió el error
3. **Proponer soluciones comunes:**
   - Paquete faltante → añadir `\usepackage{}`  en preámbulo
   - Referencia no resuelta → verificar etiqueta (`\label{}`) vs `\ref{}`
   - Comando no definido → buscar en `pucv_inf_2024.sty` o proponer definición
   - Encoding → cambiar `inputenc` si hay caracteres acentuados problemáticos

4. **Validar cambios:**
   - Re-compilar y verificar que los errores desaparecen
   - Revisar que todas las referencias se resuelven (`?` en PDF debe desaparecer)

### Fase 5: Optimización y Finalización

Una vez compilado sin errores críticos:

1. **Revisar el PDF generado:**
   - Portada se rinde correctamente
   - Numeración romana en páginas preliminares
   - Índices (contenido, figuras, tablas) están presentes y con números de página correctos
   - Glosario (si existe) está generado
   - Bibliografía en formato APA

2. **Limpiar artefactos temporales:**
   ```bash
   cd tesis/
   latexmk -c  # O: rm -f out/*.aux out/*.bbl out/*.blg out/*.log
   ```

3. **Verificar tamaño del PDF:**
   - Si > 100 MB → revisar incrustación de imágenes/PDFs de papers; optimizar con `gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSafer -dQuality=90 -r150x150 -sOutputFile=optimized.pdf original.pdf`

---

## Paquetes Esenciales y Verificación

El archivo `pucv_inf_2024.sty` debe cargar:

| Paquete | Función | Estado |
|---------|---------|--------|
| `titlesec` | Formato de títulos y capítulos | ✓ Requerido |
| `algorithms`, `algorithmicx` | Pseudocódigo | ✓ Requerido |
| `makecell` | Tablas avanzadas | ✓ Requerido |
| `glossaries` | Glosario | ✓ Requerido |
| `nomencl` | Nomenclatura | ✓ Requerido |
| `biblatex`, `biblatex-apa` | Bibliografía APA | ✓ Requerido |
| `enumitem` | Listas personalizadas | ✓ Requerido |
| `caption` | Subcaptions | ✓ Requerido |
| `lipsum` | Texto dummy (desarrollo) | ⊘ Opcional |
| `pdfpages` | Incrustar PDFs | ✓ Requerido |

**Verificación:** Leer `pucv_inf_2024.sty` y confirmar que todos los `\usepackage{}` están presentes.

---

## Comandos Personalizados de Portada

Estos comandos están definidos en `pucv_inf_2024.sty` y se usan en `portada_principal.tex`:

| Comando | Argumento | Ejemplo |
|---------|-----------|---------|
| `\membrete{}` | Encabezado PUCV | `\membrete{PONTIFICIA UNIVERSIDAD CATÓLICA DE VALPARAÍSO}` |
| `\tituloPortada{}` | Título del trabajo | `\tituloPortada{Detección de Sugerencias Automáticas...}` |
| `\alumnos{}` | Lista de estudiantes | `\alumnos{Fabrizzio Andrés Mura Lavarello \\ Matías Hernán Bugueño Bugueño}` |
| `\datosPortada{}` | Contenedor de datos (ambiente) | `\begin{datosPortada}...\end{datosPortada}` |
| `\datoPortada{}{}` | Par clave-valor | `\datoPortada{Carrera}{Ingeniería Civil Informática}` |
| `\fechaPortada{}` | Fecha final | `\fechaPortada{18 de Marzo de 2026}` |

**Uso en portada:**
```latex
\membrete{PONTIFICIA UNIVERSIDAD CATÓLICA DE VALPARAÍSO}
\tituloPortada{Detección de Sugerencias Automáticas de la Experiencia del Turista}
\alumnos{Fabrizzio Andrés Mura Lavarello \\ Matías Hernán Bugueño Bugueño}
\begin{datosPortada}
  \datoPortada{Carrera}{Ingeniería Civil Informática}
  % ... más datos
\end{datosPortada}
\fechaPortada{18 de Marzo de 2026}
```

---

## Gestión de Bibliografía (biblatex + APA)

### Configuración en `main.tex`:

```latex
% Preámbulo
\usepackage[style=apa, backend=biber, language=spanish]{biblatex}
\addbibresource{referencias.bib}  % Ruta del archivo .bib
```

### Estructura del archivo `referencias.bib`:

```bibtex
@article{Rusu2022,
  author = {Rusu, Cristian and Roncagliolo, Silvana},
  title = {Evaluating Post-pandemic Tourist Experience},
  journal = {Journal of Travel Research},
  year = {2022},
  volume = {61},
  number = {2},
  pages = {123--145}
}

@book{Nielsen1990,
  author = {Nielsen, Jakob},
  title = {Usability Engineering},
  publisher = {Academic Press},
  year = {1990}
}

@inproceedings{Smith2021,
  author = {Smith, John and Doe, Jane},
  title = {Machine Learning for Sentiment Analysis},
  booktitle = {Proceedings of ACM Conference},
  year = {2021},
  pages = {234--245}
}
```

### Compilación correcta:

```bash
pdflatex main.tex
biber main  # Procesa referencias.bib
pdflatex main.tex
pdflatex main.tex  # Resuelve referencias cruzadas
```

### Inspección y Diagnóstico:

- **Referencia no encontrada** → Revisar que los `\cite{}` en `.tex` coinciden con las claves (`{Rusu2022}`) en `.bib`
- **Estilo mal formateado** → Verificar que `biblatex-apa` está instalado (`tlmgr install biblatex-apa` en TeX Live)
- **Caracteres especiales** → En `.bib`, usar `{\'a}` para acentos o `"á"` si se ha configurado UTF-8

---

## Estructura de Capítulos

### Plantilla de capítulo nuevo (`tesis/body/nuevo_capitulo.tex`):

```latex
\chapter{Nombre del Capítulo}
\label{cap:nombredelcapitulo}

\section{Introducción}
Texto introductorio con cita \cite{Rusu2022}.

\section{Contenido Principal}
Párrafo con referencia cruzada (véase Sección~\ref{sec:subseccion}).

\subsection{Subsección}
\label{sec:subseccion}
Texto de subsección.

\begin{figure}[!h]
  \centering
  \includegraphics[width=0.6\textwidth]{path/to/image.pdf}
  \caption{Descripción de la figura.}
  \label{fig:nombredelafigura}
\end{figure}

\section{Conclusión}
Resumen del capítulo.
```

### Incluir en `main.tex`:

```latex
\include{body/nuevo_capitulo}
```

---

## Checklist de Compilación Exitosa

Antes de marcar una tarea como completada:

- [ ] `pdflatex` y `biber` compilan sin errores **críticos**
- [ ] El archivo `out/main.pdf` existe y se puede abrir
- [ ] Portada renderiza correctamente (encabezado, títulos, datos, fecha)
- [ ] Numeración romana en páginas preliminares (portada, abstract, índices)
- [ ] Índices generados: Tabla de Contenidos, Lista de Figuras, Lista de Tablas
- [ ] Glosario (si existe) listedoproperly con referencias
- [ ] Todas las citas resueltas (sin `[?]` en el PDF)
- [ ] Bibliografía en orden alfabético y formato APA
- [ ] No hay `Overfull \hbox` críticos (warnings < 3 sobre márgenes)
- [ ] Tamaño del PDF razonable (< 100 MB por defecto)

---

## Solución de Problemas Comunes

| Problema | Causa | Solución |
|----------|-------|----------|
| `! Undefined control sequence \membrete` | Comando no definido en `.sty` | Verificar que `pucv_inf_2024.sty` está cargado con `\usepackage{pucv_inf_2024}` |
| `Citation not found (key)` | Clave en `.bib` no coincide con `\cite{}` | Buscar clave exacta en `referencias.bib`; revisar case-sensitive |
| `! Missing package` | Paquete no instalado | Instalar: `tlmgr install <paquete>` (TeX Live) o `mpm --admin install <paquete>` (MikTeX) |
| `! File not found input/body/capitulo.tex` | Ruta incorrecta en `\input` o `\include` | Revisar nombres de archivos y directorios; asegurarse que existen |
| `Overfull \hbox` (warnings) | Línea muy larga o saltos de línea deficientes | Revisar párrafos con `\hyphenation{}` o dividir en líneas más cortas |
| Glosario vacío | `\makeglossaries` no ejecutado | Ejecutar `makeindex main.glo -s main.ist -o main.gls` o re-compilar con `latexmk` |
| PDF no se actualiza | Cache del visor | Cerrar y abrir visor; en VSCode, hacer clic en el ícono de "Refresh" |

---

## Integración con VSCode y LaTeX Workshop

### Archivo `.vscode/settings.json`:

```json
{
  "latex-workshop.latex.tools": [
    {
      "name": "pdflatex",
      "command": "pdflatex",
      "args": ["-interaction=nonstopmode", "-output-directory=out", "%DOC%"]
    },
    {
      "name": "biber",
      "command": "biber",
      "args": ["%DIR%/out/%DOCFILE%"]
    }
  ],
  "latex-workshop.latex.recipes": [
    {
      "name": "pdflatex + biber + pdflatex",
      "tools": ["pdflatex", "biber", "pdflatex"]
    }
  ],
  "latex-workshop.view.pdf.viewer": "tab",
  "latex-workshop.synctex.afterBuild.enabled": true
}
```

### Uso en desarrollo:

- **Guardar archivo** → VSCode compila automáticamente si está activada la opción `autoSave`
- **Ver visor PDF** → Pestaña "LaTeX Workshop" > icono de visor
- **Log de compilación** → Panel "OUTPUT" > seleccionar "LaTeX Workshop"

---

## Ejemplos de Uso

### Ejemplo 1: Compilar y reportar errores

**Prompt para el agente:**
> "Compila `tesis/main.tex` y dame un resumen de errores y warnings."

**Acciones esperadas:**
1. Ejecutar `latexmk -pdf -silent -outdir=out main.tex` en carpeta `tesis/`
2. Leer `out/main.log` si hay errores
3. Extraer líneas críticas y proponer soluciones
4. Confirmar que `out/main.pdf` se generó exitosamente

### Ejemplo 2: Añadir una nueva sección a la bibliografía

**Prompt:**
> "Añade una referencia nueva al capítulo de Metodología: Rusu et al. (2022), Journal of Tourism Research, vol. 61, pp. 123–145."

**Acciones esperadas:**
1. Crear entrada bibtex en `referencias.bib`
2. Verificar que la clave es única
3. Compilar y confirmar que la referencia aparece en el PDF
4. Proporcionar comando `\cite{...}` para usar en el documento

### Ejemplo 3: Resolver referencias no resueltas

**Prompt:**
> "El glosario no aparece en el PDF. ¿Qué falta?"

**Acciones esperadas:**
1. Revisar `main.tex` para verificar `\printglossaries` o similar
2. Buscar comando `\makeglossaries`
3. Si falta, sugerir agregar antes de `\end{document}`: `\printglossaries`
4. Ejecutar `makeindex` (incluido en `latexmk`)
5. Re-compilar y verificar en PDF

---

## Referencias y Recursos Internos

- **Estilos PUCV**: `tesis/pucv_inf_2024.sty`
- **Instructiones generales**: `.github/instructions/general.instructions.md`
- **Portadas**: `tesis/front-page/`
- **Capítulos**: `tesis/body/`
- **Bibliografía**: `tesis/referencias.bib`

---

## Versión y Mantenimiento

- **Versión**: 0.1 → Basada en TeX Live 2025, pdflatex, biblatex-apa
- **Última actualización**: 18 de Marzo de 2026
- **Autores**: Fabrizzio Andrés Mura Lavarello, Matías Hernán Bugueño Bugueño

**Mejoras futuras:**
- Integración con CI (GitHub Actions para PDFs automáticos)
- Validación de estilo APA automática
- Checklist interactivo pre-entrega