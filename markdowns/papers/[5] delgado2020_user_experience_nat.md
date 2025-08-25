Heurísticas de Experiencia de Usuario para Sitios Web de Parques Nacionales

Dania Delgado, Daniela Zamora, Daniela Quiñones, Cristian Rusu, Silvana Roncagliolo, Virginica Rusu

Resumen

Un sitio web de un parque nacional extiende (en cierto sentido) un parque nacional físico; no tiene ubicación física, por lo que sus elementos e información pueden apreciarse desde cualquier parte del mundo. La usabilidad es un concepto conocido desde hace décadas. La Experiencia de Usuario (UX) es un concepto más amplio que engloba la usabilidad. Evaluar la usabilidad y la UX es una tarea importante al desarrollar cualquier tipo de sitio web: es necesario comprobar si un sitio web de parque nacional es intuitivo, fácil de usar y permite a los usuarios cumplir sus objetivos. Los sitios web de parques nacionales tienen características propias que los diferencian de otros sistemas, por lo que es necesario usar un conjunto apropiado de heurísticas para este tipo de sitios. Este artículo presenta un conjunto de 14 heurísticas para evaluar la UX de sitios web de parques nacionales. Las heurísticas fueron desarrolladas aplicando la metodología propuesta por Quiñones et al. Para validar y refinar las heurísticas se realizaron dos iteraciones: en la primera se validaron mediante evaluación heurística y juicio de expertos (encuesta); en la segunda, mediante pruebas con usuarios (co-discovery y focus group). Según los resultados de validación, concluimos que el conjunto propuesto es efectivo.

Palabras clave: Sitios web de parques nacionales · Experiencia de Usuario · Usabilidad · Heurísticas

1 Introducción

Un sitio web de parque nacional complementa, en cierto modo, a un parque nacional físico. No tiene una ubicación física, por lo que sus elementos e información pueden consultarse desde cualquier parte del mundo. Tras revisar la literatura, no encontramos una definición formal de "sitio web de parque nacional"; por tanto, lo definimos como una colección de páginas web que proveen información de un parque nacional físico mediante recursos multimedia. Dependiendo del tipo de parque, los sitios ofrecen información sobre flora y fauna, imágenes, actividades comunes, recomendaciones, mapas, entre otros.

La usabilidad y la UX deben evaluarse al desarrollar sitios web para garantizar que satisfacen las necesidades de los usuarios y encajan en el contexto físico, social y organizacional de uso. Es importante comprobar si el sitio es intuitivo, fácil de usar y permite completar objetivos. La UX debe considerarse explícitamente: la información, el contenido, la presentación y la estructura deben generar una experiencia amigable que motive a los usuarios a conocer el parque físico.

Los métodos para evaluar usabilidad/UX se clasifican básicamente en: (1) inspecciones (expertos) y (2) pruebas con usuarios. La evaluación heurística es una de las inspecciones más comunes: evaluadores expertos detectan problemas potenciales basados en heurísticas [1]. Las heurísticas generales (por ejemplo, las de Nielsen) permiten inspeccionar sitios en términos generales, pero no detectan bien problemas específicos del dominio.

Dado que los sitios de parques nacionales tienen rasgos propios, es necesario usar heurísticas específicas que también consideren aspectos de UX, no solo usabilidad. En este trabajo presentamos 14 heurísticas para evaluar la UX de estos sitios, desarrolladas con la metodología de Quiñones et al. [2]. Se realizaron dos iteraciones de validación: la primera con evaluación heurística y juicio experto; la segunda con pruebas de usuarios (co-discovery y focus group). Los resultados indican que las heurísticas propuestas son efectivas.

La estructura del artículo: Sección 2: marco teórico; Sección 3: metodología aplicada; Sección 4: heurísticas finales; Sección 5: validación; Sección 6: conclusiones y trabajos futuros.

2 Marco teórico

2.1 Usabilidad

Según ISO 9241‑210, la usabilidad es "la extensión en que un producto, sistema o servicio puede ser usado por usuarios específicos para lograr objetivos específicos con efectividad, eficiencia y satisfacción en un contexto de uso especificado" [4]. Nielsen presenta la usabilidad como multidimensional y propone cinco atributos: aprendibilidad, eficiencia, memorabilidad, errores y satisfacción. Para el desarrollo de las heurísticas para sitios de parques nacionales se consideraron todos estos atributos.

2.2 Experiencia de Usuario (UX)

La UX carece de una única definición; se aborda desde múltiples perspectivas. ISO 9241‑210 define la UX como "las percepciones y respuestas de la persona resultantes del uso y/o uso anticipado de un producto, sistema o servicio". Morville propone un modelo de siete factores (útil, usable, deseable, valioso, encontrable, accesible, creíble). Para este trabajo se consideraron seis de esos factores: útil, valioso, creíble, usable, deseable y encontrable —no se incluyó "accesible" porque existen reglas y herramientas claras (W3C) para evaluarla.

2.3 Evaluación por heurísticas

La evaluación heurística es un método de inspección donde expertos (típicamente 3–5) identifican problemas de usabilidad/UX usando un conjunto de heurísticas. Las heurísticas pueden ser genéricas (p. ej. Nielsen) o específicas del dominio. Inicialmente, los evaluadores trabajan de forma independiente, luego consolidan los problemas detectados y puntúan cada problema en frecuencia, severidad y criticidad, lo que permite priorizar correcciones.

2.4 Sitios web de parques nacionales

CONAF define un parque nacional físico como un área extensa con ambientes representativos de la biodiversidad, relativamente no alterada por la acción humana, de interés educativo, científico o recreativo [11]. Otros autores amplían el concepto a áreas terrestres o marinas protegidas gestionadas para conservación.

Aunque no existe una definición formal de "sitio web de parque nacional", lo entendemos como una colección de páginas que proporcionan información sobre el parque físico por medio de recursos multimedia (flora, fauna, actividades, recomendaciones, mapas, etc.). Se identificaron las siguientes características propias de estos sitios:

1. Información actualizada
2. Experiencia virtual (visita sin desplazamiento)
3. Recursos multimedia (texto, imágenes, audio, video)
4. Permisos, restricciones y recomendaciones claras
5. Credibilidad de la información
6. Interacción asincrónica (foros, blogs)
7. Contenido útil e interesante
8. Contenido multilenguaje

Estas características se tuvieron en cuenta en el desarrollo de las heurísticas.

3 Metodología

Se aplicó la metodología de Quiñones et al. [2,3], compuesta por 8 etapas (exploratoria, experimental, descriptiva, correlacional, selección, especificación, validación y refinamiento) que pueden aplicarse de forma iterativa. La Tabla 1 del artículo original resume esas etapas.

3.1 Proceso de desarrollo de las heurísticas

Se tomó como base el conjunto de heurísticas específicas para museos virtuales propuesto por Aguirre [15], por su cercanía al dominio. En la primera iteración se realizó revisión bibliográfica, selección de atributos de usabilidad y UX, y se utilizó la plantilla de especificación propuesta por la metodología (13 elementos: id, prioridad, nombre, definición, explicación, característica de la aplicación, ejemplos, beneficios, problemas, checklist, atributos de usabilidad, factores UX y heurísticas relacionadas). A partir de ello se propusieron 18 heurísticas.

Tras la validación de la primera iteración se detectaron redundancias y solapamientos; por ello se iteró, fusionando y refinando heurísticas hasta llegar a la versión final de 14 heurísticas.

4 Heurísticas de Experiencia de Usuario para Sitios Web de Parques Nacionales

A continuación se presenta el conjunto final de 14 heurísticas (ID, nombre y definición resumida):

- NPH1 — Visibilidad del sistema: el sitio debe mantener informado al usuario sobre procesos y cambios de estado en un tiempo razonable.
- NPH2 — Recursos multimedia: el sitio debe atraer al usuario ofreciendo una experiencia virtual mediante imágenes, videos y audios.
- NPH3 — Información de interés: el sitio debe proporcionar información visible y útil (actividades permitidas, recomendaciones, restricciones).
- NPH4 — Coincidencia entre el sistema y el mundo real: el sitio debe ofrecer opciones de idioma y usar términos familiares al usuario.
- NPH5 — Control y libertad del usuario: permitir navegación libre y opciones de deshacer/rehacer acciones.
- NPH6 — Consistencia y estándares: el sitio debe ser coherente en todas sus páginas y seguir una estructura lógica.
- NPH7 — Credibilidad de la información: la información presentada debe generar confianza en el usuario.
- NPH8 — Prevención de errores: el sitio debe prevenir o advertir sobre situaciones que puedan causar errores.
- NPH9 — Minimizar la carga de memoria del usuario: la información necesaria debe estar disponible para no forzar la memoria del usuario.
- NPH10 — Flexibilidad y eficiencia de uso: el sitio debe permitir que usuarios novatos y expertos logren sus objetivos.
- NPH11 — Diseño estético y minimalista: mostrar elementos relevantes con diseño agradable y estructura lógica sin redundancias.
- NPH12 — Ayuda para recuperarse de errores: mostrar mensajes claros indicando el origen y soluciones ante errores.
- NPH13 — Ayuda y documentación: ofrecer ayuda y documentación orientada a las tareas específicas del usuario.
- NPH14 — Interacción asincrónica: permitir la comunicación asincrónica (foros, blogs, comentarios) que enriquezca la información.

(En el artículo original cada heurística se especifica con más detalle, checklist y ejemplos.)

5 Validación de las heurísticas

Se validó el conjunto en dos iteraciones:

Primera iteración — evaluación heurística y juicio de expertos

Se comparó el nuevo conjunto (NPH) frente a heurísticas para museos virtuales (VMH) evaluando el sitio del Yellowstone National Park. Se realizaron evaluaciones con dos grupos de 3 evaluadores cada uno (grupo control: VMH; grupo experimental: NPH). Se aplicaron cinco criterios de efectividad: asociaciones correctas/incorrectas de problemas a heurísticas; número total de problemas encontrados; número de problemas específicos identificados; número de problemas con severidad alta; número de problemas con criticidad alta.

Resultados: NPH obtuvo mejores resultados que VMH en las métricas de asociaciones correctas (mayor porcentaje), identificación de problemas específicos, y detección de problemas más severos y críticos. En la métrica de número total de problemas identificados NPH no superó a VMH, por lo que se realizó una segunda iteración para mejorarla.

Además, se aplicó una encuesta a 3 expertos (dimensiones: utilidad, claridad, facilidad de uso, necesidad de checklist; y preguntas sobre facilidad de uso, intención de uso y completitud). Con base en los comentarios se eliminaron 4 heurísticas por solapamientos y se refinó la especificación de otras.

Segunda iteración — pruebas con usuarios (Co-discovery y Focus Group)

Se diseñaron tareas basadas en problemas detectados en la evaluación heurística que no fueron encontrados por el grupo experimental (p. ej. dificultad por idioma, información estática, opciones confusas en el buscador, icono de calendario poco representativo, tamaño pequeño de imágenes).

Participaron 16 estudiantes (8 parejas) del programa de Administración Multilingüe del Turismo (20–26 años). En la prueba co-discovery la mayoría quedó satisfecha con la información y los resultados fueron, en general, efectivos. En el focus group (dos grupos) se recogieron percepciones cualitativas: la presencia de recursos multimedia fue valorada positivamente (apoyando NPH2); hubo comentarios negativos sobre exceso de información en una sola página, ligado a NPH11; se destacó la presencia de información de interés y credibilidad (NPH3, NPH7); se señaló la importancia del soporte multilingüe (NPH4); se valoró la facilidad del buscador (NPH10) y la utilidad de secciones con comentarios de otros visitantes (NPH14).

Conclusión de la validación: las percepciones y problemas discutidos por los usuarios fueron cubiertos por las heurísticas propuestas.

6 Conclusiones

La UX es crucial al diseñar productos y servicios; su evaluación ayuda a detectar fuentes de frustración y mejora la interacción. Los sitios de parques nacionales buscan informar y complementar la visita física, ofreciendo acceso virtual a quienes no pueden desplazarse. No pretenden reemplazar la visita real.

Se propuso un conjunto de 14 heurísticas para evaluar la UX en sitios de parques nacionales, validadas y refinadas en dos iteraciones mediante métodos de evaluación heurística, juicio experto y pruebas con usuarios. Los resultados muestran que las heurísticas permiten detectar problemas específicos del dominio.

Trabajo futuro: validar más ampliamente las heurísticas en otros estudios de caso y con distintos perfiles de usuarios.

Referencias

(Se mantienen las referencias tal como aparecen en el documento original.)

[1] Nielsen, J., Molich, R.: Heuristic evaluation of user interfaces. CHI 1990.
[2] Quiñones, D., Rusu, C., Rusu, V.: A methodology to develop usability/user experience heuristics. Comput. Stand. Interfaces 59, 109–129 (2018).
[3] Quiñones, D., Rusu, C.: Applying a methodology to develop user experience heuristics. Comput. Stand. Interfaces 66, 103345 (2019).
[4] ISO 9241-210. Ergonomics of Human-system Interaction—Part 210: Human-centred Design for Interactive Systems. ISO (2010).
[15] Aguirre, N.: Experiencia de Usuario en Museos Virtuales. Tesis de pregrado, PUCV (2015).

---
Archivo generado automáticamente: `markdowns/papers/delgado2020_user_experience_nat.md`.
