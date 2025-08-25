Computer Standards & Interfaces 59 (2018) 109–129


Contenido disponible en ScienceDirect

Computer Standards & Interfaces

A methodology to develop usability/user experience heuristics

Daniela Quiñones, Cristian Rusu, Virginica Rusu

Pontificia Universidad Católica de Valparaíso, Valparaíso, Chile
Universidad de Playa Ancha, Valparaíso, Chile

Resumen

Palabras clave: Usabilidad · Experiencia de usuario · Evaluación heurística · Heurísticas de usabilidad · Metodología

La tecnología, los sistemas de software y los paradigmas de interacción humano‑computador están evolucionando. Las heurísticas tradicionales de usabilidad no cubren todos los aspectos de las interacciones usuario‑sistema. Se han propuesto muchos conjuntos de heurísticas con el objetivo de evaluar dominios de aplicación específicos y sus características relacionadas con la usabilidad. Además, varios conjuntos de heurísticas se emplean para evaluar aspectos distintos de la usabilidad pero relacionados con la experiencia de usuario (UX). Sin embargo, la mayoría de los autores usan un proceso informal para desarrollar heurísticas de usabilidad/UX; no existe un protocolo claro para la validación de heurísticas. Esto puede producir conjuntos de heurísticas difíciles de entender o usar; además, las heurísticas resultantes pueden no ser herramientas de evaluación efectivas o eficientes. En este artículo presentamos una metodología formal para desarrollar heurísticas de usabilidad/experiencia de usuario. La metodología se aplicó en la práctica en varios estudios de caso y fue validada mediante opiniones de expertos.

1. Introducción

La usabilidad se define típicamente como la "capacidad de ser usado", es decir, la capacidad de una entidad para ser utilizada [1]. La usabilidad puede ser diseñada en el producto y evaluada mediante inspecciones de usabilidad o pruebas de usabilidad. La usabilidad forma parte de la Experiencia de Usuario (UX). La UX incluye todas las emociones, creencias, preferencias, percepciones, respuestas, comportamientos y logros de los usuarios que ocurren antes, durante y después del uso de un producto [2]. Además de la usabilidad, existen varios aspectos de la UX que son importantes de evaluar en una aplicación de software.

La evaluación heurística es un método de inspección de usabilidad ampliamente utilizado para identificar problemas de usabilidad [3]. Un conjunto de evaluadores juzga la interfaz del producto para determinar si satisface principios de usabilidad [4]. Este método utiliza "principios heurísticos" o "heurísticas de usabilidad" para evaluar la usabilidad.

Varios autores han propuesto muchos conjuntos de heurísticas para evaluar dominios de aplicación específicos y sus características particulares. Esto se debe a que las heurísticas tradicionales no evalúan características específicas de aplicaciones concretas. Los numerosos trabajos de investigación centrados en diseñar nuevos conjuntos de heurísticas indican el interés e importancia de crear heurísticas para problemas de usabilidad concretos en dominios de aplicación específicos. Además, varios conjuntos de heurísticas se usan para evaluar no solo la usabilidad, sino también otros aspectos importantes relacionados con la UX, como la aprendibilidad, jugabilidad y adaptabilidad.

Sin embargo, en la mayoría de los estudios revisados no existe evidencia de que se haya usado un proceso formal o una metodología para desarrollar heurísticas de usabilidad/UX [5]. Esto se debe a que no hay teorías o modelos apropiados para establecer heurísticas para dominios específicos o para evaluar heurísticas en términos de su aplicabilidad a un tipo concreto de aplicación. La mayoría de las heurísticas existentes se han desarrollado basándose en la experiencia de los investigadores o usando métodos que generalmente se emplean para otros propósitos pero adaptados para crear heurísticas [6].

Se puede resumir el proceso de desarrollo de heurísticas de usabilidad/UX en dos etapas: (1) extracción de información y (2) transformación de la información extraída en heurísticas [7]. Sin embargo, no hay consenso sobre el proceso más efectivo para desarrollar heurísticas para dominios de aplicación concretos [8].

Muchos trabajos proponen extensiones o adaptaciones de heurísticas existentes (por ejemplo, las heurísticas de Nielsen). Los estudios no documentan ni explican en detalle el proceso seguido para crear el nuevo conjunto de heurísticas. La mayoría de los estudios no especifica si el proceso es formal o informal, o si los autores emplearon una metodología para desarrollar heurísticas.

Aunque existen metodologías que apoyan el proceso de desarrollo de heurísticas de usabilidad [9–14], actualmente no hay un protocolo claro para la validación de heurísticas. Todo el proceso de desarrollo de heurísticas de usabilidad aún debe formalizarse [15]. En conclusión, no existe un proceso formal para formular, especificar, validar y refinar heurísticas de usabilidad/UX. Para facilitar el proceso de desarrollo de heurísticas, proponemos una metodología formal con varias etapas para establecer heurísticas de usabilidad/UX.

Este documento está organizado como sigue: la Sección 2 explora los antecedentes teóricos; la Sección 3 explica la necesidad de una metodología formal para desarrollar heurísticas de usabilidad/UX; la Sección 4 muestra el proceso seguido para crear la metodología; la Sección 5 presenta la especificación formal de la metodología para desarrollar heurísticas de usabilidad/UX; la Sección 6 explica brevemente cada etapa de la metodología, incluyendo ejemplos para el dominio de sitios web de parques nacionales; la Sección 7 presenta la validación de la metodología y resultados; y la Sección 8 presenta las conclusiones y trabajos futuros.

2. Antecedentes teóricos

Se presentan brevemente los conceptos de usabilidad, experiencia de usuario, evaluación heurística y métodos de evaluación. Además se describen trabajos relacionados.

2.1. Usabilidad

Según la norma ISO 9241‑11, la usabilidad se puede definir como: "el grado en que un producto puede ser usado por usuarios específicos para alcanzar objetivos especificados con efectividad, eficiencia y satisfacción en un contexto de uso especificado" [16]. La norma explica cómo identificar la información necesaria a considerar al especificar o evaluar la usabilidad en términos de rendimiento y satisfacción del usuario [17]. La norma fue actualizada y está en revisión [1].

2.2. Métodos de evaluación de usabilidad

Como resaltan Fernández et al., "un método de evaluación de usabilidad es un procedimiento compuesto por una serie de actividades bien definidas para la recolección de datos relacionados con la interacción del usuario final con un producto de software y/o cómo una característica específica de ese producto contribuye a lograr cierto grado de usabilidad" [18]. Las evaluaciones de usabilidad se clasifican en dos categorías:

1. Inspecciones de usabilidad: revisiones realizadas por evaluadores – generalmente expertos – basadas en su propio juicio, sin la participación de usuarios.
2. Pruebas de usabilidad: exámenes que incluyen usuarios reales, que evalúan un producto de software en funcionamiento.

Las inspecciones de usabilidad se basan en la participación de evaluadores inspeccionando interfaces [19], mientras que las pruebas de usabilidad implican que usuarios ejecuten un prototipo para recolectar información para mejorar la usabilidad del producto [19].

2.3. Evaluación heurística

La evaluación heurística es un método común de inspección de usabilidad que identifica problemas y "mide" el grado de usabilidad según principios o heurísticas de usabilidad. Fue propuesta por Nielsen y Molich [20]. Expertos en usabilidad inspeccionan una interfaz basándose en heurísticas para identificar problemas, que se clasifican y valoran en severidad, frecuencia y criticidad.

2.4. Heurísticas de usabilidad

La evaluación heurística se realiza en base a un conjunto de heurísticas. Se les llama "heurísticas" porque son más reglas empíricas que directrices específicas [21]. Las 10 heurísticas de Nielsen [21] son ampliamente usadas; se muestran a continuación:

- Visibilidad del estado del sistema
- Coincidencia entre el sistema y el mundo real
- Control y libertad del usuario
- Consistencia y estándares
- Prevención de errores
- Reconocimiento en lugar de recuerdo
- Flexibilidad y eficiencia de uso
- Diseño estético y minimalista
- Ayudar a los usuarios a reconocer, diagnosticar y recuperarse de errores
- Ayuda y documentación

Cada sistema o aplicación tiene características que lo diferencian de otros tipos de aplicaciones. Por esta razón, las heurísticas tradicionales pueden no evaluar características únicas de dominios específicos, omitiendo elementos importantes. Para evaluar un dominio de manera efectiva, varios autores han diseñado nuevos conjuntos de heurísticas, adaptando y ampliando las heurísticas tradicionales para cubrir aspectos concretos.

2.5. Experiencia de Usuario (UX)

La UX extiende el concepto de usabilidad más allá de efectividad, eficiencia y satisfacción. Según la norma ISO 9241‑210, la UX puede definirse como: "las percepciones y respuestas de una persona resultantes del uso y/o uso anticipado de un producto, sistema o servicio" [2]. Incluye todas las emociones, creencias, preferencias, percepciones, respuestas físicas y psicológicas, comportamientos y logros que ocurren antes, durante y después del uso. La norma indica que la UX es una consecuencia de la imagen de marca, presentación, funcionalidad, rendimiento del sistema, comportamiento interactivo y capacidades de asistencia del sistema interactivo, el estado interno y físico del usuario derivado de experiencias previas, actitudes, habilidades y personalidad, y el contexto de uso [2].

2.6. Métodos de evaluación de UX

Los métodos de evaluación de UX se centran en determinar cómo se siente el usuario respecto al sistema objetivo [22]. Permiten a los diseñadores entender y valorar productos para lograr una UX positiva [23]. Dependiendo de lo que se quiera evaluar, los métodos de UX pueden clasificarse en: (1) estudios de campo, (2) estudios de laboratorio, (3) estudios online y (4) cuestionarios y escalas [24]. Dado que la UX extiende el concepto de usabilidad, ciertos aspectos de UX pueden evaluarse mediante evaluaciones heurísticas si las heurísticas cubren esas dimensiones; sin embargo, evaluar todos los aspectos de UX es más desafiante y las pruebas con usuarios son críticas.

2.7. Trabajos relacionados

Rusu et al. [9] proponen una metodología con seis etapas para desarrollar heurísticas de usabilidad. Esta metodología ha sido utilizada por varios autores para crear nuevos conjuntos de heurísticas para dominios específicos [25–38]. Esos autores destacan que la metodología facilita el diseño y especificación de heurísticas al recomendar etapas que soportan el proceso. Además, la metodología sugiere una plantilla para especificar heurísticas e incluye una etapa de validación y refinamiento. Sin embargo, algunas etapas no explican claramente las actividades a realizar (especialmente las etapas descriptiva y correlacional); no se explica cómo, cuándo ni en qué circunstancias iterar las etapas.

Van Greunen et al. [10] proponen un proceso en tres fases para crear heurísticas para dominios específicos. Cada etapa se explica en detalle y las actividades a realizar están claramente descritas. Sin embargo, la metodología carece de una explicación específica sobre cómo especificar heurísticas (no propone plantilla), la etapa de validación no explica claramente cómo usar la herramienta propuesta y la experiencia previa en el uso de heurísticas no se considera al seleccionar evaluadores para la validación.

Hub y Čapková [11] propusieron una metodología para crear un conjunto adecuado de heurísticas para administración pública. Consideran roles distintos: (1) expertos para especificación y revisión y (2) usuarios finales para evaluación. Presentan una estructura interesante pero no ofrecen una validación formal.

Franklin et al. [12] proponen una metodología para heurísticas de sistemas de realidad aumentada colaborativos remotos; su propuesta está basada principalmente en adaptar heurísticas existentes y proponen validación mediante grupos focales de especialistas HCI, pero no detallan cómo especificar nuevas heurísticas.

Lechner et al. [13] presentan una metodología que incluye usuarios en la validación pero no expertos. Hermawati y Lawson [14] sugieren cómo ampliar conjuntos de heurísticas e incluir usuarios, pero faltan detalles sobre actividades y especificaciones.

En resumen, las metodologías revisadas presentan enfoques útiles pero carecen de especificaciones formales y procedimientos claros de validación. Por tanto, proponemos una metodología formal y sistemática para especificar y validar heurísticas de usabilidad/UX.

3. Necesidad de una metodología formal

Varios autores han señalado la necesidad de crear nuevas heurísticas para evaluar aplicaciones específicas. Por ejemplo, en [40] se concluye que las heurísticas existentes son demasiado generales para evaluar la usabilidad de aplicaciones de mapas móviles. En [41], se observó que los LMS (Learning Management Systems) no se evaluaban adecuadamente con conjuntos existentes. En consecuencia, es necesario desarrollar nuevos conjuntos que evalúen características específicas de cada dominio.

Cuando se usan heurísticas genéricas para dominios concretos, su aplicabilidad puede ser limitada y perjudicar la evaluación [42]. Por ello, continuamente se desarrollan conjuntos especializados de heurísticas [43].

Como indican Hermawati y Lawson [7], las heurísticas de Nielsen pueden usarse en varios dominios, pero deben ajustarse para no omitir problemas de usabilidad específicos. Tras evaluaciones experimentales (por ejemplo [45]), se ha observado que las heurísticas de Nielsen no cubren todos los aspectos de aplicaciones transaccionales.

Al crear nuevas heurísticas, los autores siguen distintos enfoques pero no documentan procesos en detalle [5]. Un proceso formal es crucial para desarrollar conjuntos efectivos y eficientes de heurísticas.

Aunque existen metodologías que apoyan el desarrollo de heurísticas [9–14], no hay un protocolo claro de validación. Por ello proponemos una metodología formal que permita crear conjuntos de heurísticas enfocados en aspectos, factores o atributos a evaluar.

4. Proceso de creación de la metodología

Usamos varios insumos para crear la metodología y realizamos dos iteraciones para formalizar, validar y refinarla. Los insumos usados fueron:

1) Revisión sistemática de literatura sobre procesos y metodologías para desarrollar heurísticas [5].
2) Resultados experimentales: entrevistas y encuestas para determinar la percepción de evaluadores al usar las heurísticas de Nielsen [46].
3) Aplicación práctica: aplicar la metodología propuesta por Rusu et al. [9] para desarrollar heurísticas para sitios web transaccionales y analizar el proceso [47].

La metodología fue formalizada mediante descripciones, tablas y diagramas BPMN. Se añadieron diagramas BPMN (Apéndices A–K) y tablas resumen para cada paso (insumos, salidas y actividades).

4.2 Iteraciones

Realizamos dos iteraciones para formalizar, validar y refinar la metodología, dividida en 7 fases:

4.2.1 Primera iteración

En la primera iteración se llevaron a cabo las 7 fases. Se definió el problema, preguntas de investigación y objetivos; se realizaron experimentos para validar la necesidad de heurísticas específicas; se aplicó la metodología de Rusu et al. [9] para desarrollar heurísticas para sitios web transaccionales; se llevó a cabo una revisión sistemática; se formalizó una metodología; se realizó una validación preliminar con expertos y se refinó la metodología según el feedback.

4.2.2 Segunda iteración

En la segunda iteración se repitieron las fases de formalización, validación y refinamiento. Se aplicaron los cambios propuestos, y se realizó una encuesta a 9 expertos que aplicaron la metodología para desarrollar heurísticas en dominios específicos. Los expertos evaluaron cada paso en 4 dimensiones y respondieron preguntas globales y abiertas. Tras el análisis, se refinaron los pasos.

5. Especificación formal de la metodología para desarrollar heurísticas de usabilidad/UX

Creamos una metodología que incluye 8 etapas (Fig. 4) modeladas con BPMN. Aunque las etapas se muestran de forma secuencial, el desarrollo puede ser iterativo y algunas etapas pueden ser opcionales, superponerse o requerir retorno a etapas previas. Recomendamos aplicar la metodología de forma iterativa.

A continuación se presenta un resumen de cada etapa (tablas 3–10 en el documento original contienen detalles):

- Paso 1: Etapa exploratoria: revisión de literatura para recoger información sobre el dominio de aplicación, atributos de usabilidad/UX y conjuntos de heurísticas existentes.
- Paso 2: Etapa experimental: analizar datos obtenidos en experimentos previos (opcional) o realizar experimentos si hay tiempo y evaluadores.
- Paso 3: Etapa descriptiva: seleccionar y priorizar la información recolectada. Agrupar información por temas: definición del dominio, características, atributos de usabilidad/UX, conjuntos de heurísticas relevantes y problemas detectados.
- Paso 4: Etapa correlacional: relacionar características del dominio con atributos de usabilidad/UX y heurísticas existentes; crear categorías si procede.
- Paso 5: Etapa de selección: mantener, adaptar, eliminar heurísticas existentes o proponer nuevas según corresponda; eliminar redundancias.
- Paso 6: Etapa de especificación: formalizar el nuevo conjunto de heurísticas usando una plantilla que incluya: Id, Prioridad (3 crítico, 2 importante, 1 útil), Nombre, Definición, Explicación, Característica de la aplicación evaluada, Ejemplos, Beneficios, Problemas previstos, Checklist, Atributo de usabilidad/UX evaluado, Heurísticas relacionadas y referencias. Recomiendan entre 10 y 16 heurísticas.
- Paso 7: Etapa de validación: validar mediante evaluación heurística (comparando con heurísticas de control), juicio de expertos y pruebas con usuarios. Se proponen cinco criterios para evaluar efectividad y varios indicadores cuantitativos (números de problemas identificados, problemas específicos, severidad, etc.).
- Paso 8: Etapa de refinamiento: documentar los problemas detectados en la validación y definir qué heurísticas crear, refinar o eliminar y cómo iterar etapas si es necesario.

6. Explicación de la metodología (resumen de cada paso)

6.1 Paso 1: Etapa exploratoria

Realizar revisión bibliográfica sobre el dominio, características, atributos de usabilidad/UX y heurísticas existentes. Se recomienda revisar artículos científicos, tesis, experimentos previos y fuentes confiables.

6.2 Paso 2: Etapa experimental

Analizar datos de experimentos previos o realizar nuevos experimentos (evaluación heurística, pruebas de usabilidad, entrevistas o encuestas) para obtener información complementaria.

6.3 Paso 3: Etapa descriptiva

Seleccionar y priorizar la información recolectada. Agrupar por temas y priorizar en escala de tres niveles: (3) muy importante, (2) algo importante, (1) no importante.

6.4 Paso 4: Etapa correlacional

Emparejar características del dominio con atributos de usabilidad/UX y heurísticas existentes. Cada característica debe tener al menos un atributo asociado y, si es posible, corresponder a heurísticas existentes. Recomiendan crear categorías de heurísticas para reducir complejidad.

6.5 Paso 5: Etapa de selección

Para cada heurística existente decidir: mantener, eliminar, adaptar o crear nueva. Evitar heurísticas redundantes y documentar decisiones.

6.6 Paso 6: Etapa de especificación

Formalizar las heurísticas con la plantilla propuesta (Id, Prioridad, Nombre, Definición, Explicación, Característica evaluada, Ejemplos, Beneficios, Checklist, Atributo de usabilidad/UX, Heurísticas relacionadas). Recomiendan entre 10–16 heurísticas y, si se desea mayor detalle, desarrollar un checklist.

6.7 Paso 7: Etapa de validación

Validar mediante: (1) Evaluación heurística comparativa (grupos experimental y control evaluando productos representativos), (2) Juicio de expertos (investigadores en HCI y profesionales que realizan evaluaciones heurísticas) mediante encuestas que valoren utilidad, claridad, facilidad de uso y necesidad de checklist, y (3) Pruebas con usuarios para verificar si los problemas detectados por las heurísticas son percibidos como problemas por usuarios y para investigar problemas no detectados por un grupo.

6.8 Paso 8: Etapa de refinamiento

Documentar problemas surgidos al usar las heurísticas, especificar qué heurísticas crear, refinar o eliminar y decidir qué etapas repetir.

7. Validación de la metodología

Se realizó la validación en dos iteraciones con expertos y investigadores. A cada participante se le entregó una versión breve y otra detallada de la metodología. El objetivo fue recoger retroalimentación para mejorar la metodología.

7.1 Primera iteración: validación por opinión de expertos

Se pidió a un experto y cinco investigadores su opinión. Se obtuvo revisión y sugerencias, que se incorporaron (entradas y salidas de cada etapa, prioridad de información, ejemplos de correlación, mejoras en selección y especificación, plantillas más completas, validaciones múltiples, precisiones en escalas y en selección de expertos, etc.).

7.2 Segunda iteración: validación por juicio experto (encuesta)

Nueve expertos aplicaron la metodología y completaron un cuestionario que evalúa cada paso en dimensiones D1 (utilidad), D2 (claridad), D3 (facilidad de uso) y D4 (necesidad de más detalles) con escala Likert de 1 a 5, además de preguntas globales Q1–Q5 y cuatro preguntas abiertas.

Resultados cuantitativos (resumen):

- D1 (Utilidad): media alta (4.68). Paso 6 (Especificación) fue considerado el más útil. Paso 2 el menos útil, aunque aun alto.
- D2 (Claridad): media 4.40; Paso 4 (Correlacional) el menos claro.
- D3 (Facilidad de uso): media 3.61; Paso 4 el más difícil.
- D4 (Necesidad de más detalles): media 2.64; Paso 4 y Paso 5 mostraron mayor necesidad de detalle.

Preguntas globales:

- Q1 Easiness (facilidad): promedio 3.44
- Q2 Overall utility: promedio 4.89
- Q3 Intention of future use: promedio 4.78
- Q4 Completeness: promedio 3.78
- Q5 Additional graphics: promedio 3.78

Análisis estadístico no paramétrico (Friedman, Spearman) mostró correlaciones esperadas (por ejemplo, claridad y facilidad influyen en percepción de aplicabilidad y voluntad de uso futuro). Los expertos sugirieron mejorar la especificación del Paso 4 y añadir diagramas BPMN para clarificar el proceso.

Resultados cualitativos: los expertos encontraron que el emparejamiento entre atributos de UX y características de dominio (Paso 4) es difícil y consume tiempo; la especificación de heurísticas (Paso 6) requiere cuidado y recursos; las pruebas con usuarios requieren tiempo y recursos; en general la metodología fue considerada completa y útil.

8. Conclusiones

La evaluación heurística es un método popular para inspección de usabilidad [43]. Muchos conjuntos de heurísticas han sido desarrollados para dominios específicos, pero a menudo carecen de formalidad y validación. Una metodología formal facilita la formulación, especificación, validación y refinamiento de heurísticas y propone pasos bien definidos y métodos de validación.

Se comparó y mejoró la metodología de Rusu et al. [9] añadiendo nuevos pasos, definiciones, diagramas y tablas. Se realizaron dos validaciones: una revisión por expertos y una encuesta a 9 expertos, cuyos comentarios llevaron a refinamientos, especialmente en la etapa correlacional.

La metodología ha sido aplicada en varios estudios de caso y ha demostrado ser efectiva para producir conjuntos de heurísticas finales. Es aplicable a aspectos relacionados con UX como jugabilidad, comunicabilidad y aprendibilidad, y tiene potencial para desarrollar heurísticas para otros atributos de calidad.

Trabajo futuro incluye estudiar la aplicabilidad de la metodología para heurísticas de atributos no‑funcionales distintos a usabilidad y evaluar la eficiencia de la metodología.

Agradecimientos

Los autores agradecen a los participantes y miembros del grupo de investigación UseCV en HCI, y al apoyo de la Escuela de Ingeniería Informática de la PUCV. Daniela Quiñones recibió becas “INF‑PUCV” y “Postgrado PUCV 2017”.

Apéndices

El documento incluye diagramas BPMN para cada etapa (Apéndices A–K) y numerosas tablas explicativas (Tablas 1–22) con ejemplos y plantillas, así como ejemplos de heurísticas desarrolladas para sitios web de parques nacionales. Para referencias completas, ver el PDF original.

Referencias

(Se mantienen las referencias bibliográficas tal como en el documento original.)

[1] N. Bevan, J. Carter, S. Harker, ISO 9241-11 revised: what have we learnt about usability since 1998? in: M. Kurosu (Ed.), Human-Computer Interaction: Design and Evaluation, Vol. 9169 Springer, 2015, pp. 143–151 Lecture Notes in Computer Science.
[2] ISO 9241-210, Ergonomics of Human-system Interaction — Part 210: Human-centred Design for Interactive Systems, International Organization for Standardization, 2010.
[3] H. Hartson, T. Andre, R. Williges, Criteria for evaluating usability evaluation methods, Int. J. Hum.-Comput. Interact. 13 (4) (2001) 373–410.
[4] J. Scholtz, Usability Evaluation, National Institute of Standards and Technology, 2004.
[5] D. Quiñones, C. Rusu, How to develop usability heuristics: a systematic literature review, Comput. Stand. Interfaces 53 (2017) 89–122.
[6] P. Jaferian, K. Hawkey, A. Sotirakopoulos, M. Velez-Rojas, K. Beznosov, Heuristics for evaluating it security management tools, Hum.–Comput. Interaction 29 (4) (2014) 311–350.
[7] S. Hermawati, G. Lawson, Establishing usability heuristics for heuristics evaluation in a specific domain: is there a consensus? Appl. Ergon. 56 (2016) 34–51.
[8] G. Sim, J.C. Read, G. Cockton, Evidence based design of heuristics for computer assisted assessment, in: T. Gross, J. Gulliksen, P. Kotze, L. Oestreicher, P. Palanque, R.O. Prates, M. Winckler (Eds.), Proceedings of Human-Computer Interaction INTERACT 2009, 2009, pp. 204–216.
[9] C. Rusu, S. Roncagliolo, V. Rusu, C. Collazos, A methodology to establish usability heuristics, Proceedings of the Fourth International Conference on Advances in Computer-Human Interactions, ACHI2011, 2011, pp. 59–62.
[10] D. Van Greunen, A. Yeratziotis, D. Pottas, A three-phase process to develop heuristics, Proceedings of the 13th ZA-WWW Conference, Johannesburg, 2011.
[11] M. Hub, V. Čapková, Heuristic evaluation of usability of public administration portal, DEO, Narsingh, et al. Applied Computer Science, Procedings of International Conference on Applied Computer Science, ACS, 2010.
[12] F. Franklin, F. Breyer, J. Kelner, Heurísticas de usabilidad para sistemas colaborativos remotos de realidad aumentada, Proceedings of XVI Symposium on Virtual and Augmented Reality, SVR, 2014, pp. 53–62.
[13] B. Lechner, A. Fruhling, S. Petter, H. Siy, The chicken and the pig: user involvement in developing usability heuristics, Proceedings of the Nineteenth Americas Conference on Information Systems, 2013.
[14] S. Hermawati, G. Lawson, A user-centric methodology to establish usability heuristics for specific domains, Proceedings of the International Conference on Ergonomics & Human Factors, 2015, pp. 80–85.
[15] R. Inostroza, C. Rusu, S. Roncagliolo, V. Rusu, C. Collazos, Developing SMASH: a set of SMArtphone's uSability Heuristics, Comput. Stand. Interfaces 43 (2016) 40–52.
[16] ISO 9241-11, Ergonomic Requirements for Office Work with Visual Display Terminals (VDT's) – Part 11: Guidance on Usability, International Organization for Standardization, Geneva, 1998.
[17] N. Bevan, International standards for HCI and usability, Int. J. Hum. Comput. Stud. 55 (4) (2001) 533–552.
[18] A. Fernández, E. Insfran, S. Abrahão, Usability evaluation methods for the web: a systematic mapping study, J. Inf. Softw. Technol. 53 (2011) 789–817.
[19] J. Nielsen, Usability inspection methods, Proceedings of Conference on Human factors in computing systems, Boston, Massachusetts, United States, 1994.
[20] J. Nielsen, R. Molich, Heuristic evaluation of user interfaces, Proceeding of Conference on Human factors in Computing Systems, SIGCHI '90, 1990, pp. 249–256.
[21] J. Nielsen, Ten Usability Heuristics, https://www.nngroup.com/articles/ten-usability-heuristics/ (accessed 20 October 2017).
[22] A. Vermeeren, E. Lai-Chong, V. Roto, M. Obrist, J. Hoonhout, K. Väänänen-Vainio-Mattila, User experience evaluation methods: current state and development needs, Proceedings of the 6th Nordic Conference on Human-Computer Interaction: Extending Boundaries, New York, 2010, pp. 521–530.
[23] A. Allam, A. Razak, H. Mohamed, User experience: challenges and opportunities, J. Inf. Syst. Res. Innov. 3 (2013) 28–36.
[24] All About UX, Information for User Experience Professionals, http://www.allaboutux.org/ (accessed 21 October 2017).
[25] C. Rusu, S. Roncagliolo, G. Tapia, D. Hayvar, V. Rusu, D. Gorgan, Usability heuristics for grid computing applications, Proceedings of the Fourth International Conference on Advances in Computer-Human Interactions, ACHI, 2011, pp. 53–58.
[26] C. Rusu, R. Muñoz, S. Roncagliolo, S. Rudloff, V. Rusu, A. Figueroa, Usability heuristics for virtual worlds, Proceedings of the Third International Conference on Advances in Future Internet, IARIA, 2011, pp. 16–19.
[27] A. Solano, C. Rusu, C. Collazos, S. Roncagliolo, J.L. Arciniegas, V. Rusu, Usability heuristics for interactive digital television, Proceedings of the Third International Conference on Advances in Future Internet, IARIA, 2011, pp. 60–63.
[28] J. Díaz, C. Rusu, J. Pow-Sang, S. Roncagliolo, A cultural – oriented usability heuristics proposal, Proceedings of the 2013 Chilean Conference on Human Computer Interaction, ChileCHI '13, 2013, pp. 82–87.
[29] J. Díaz, C. Rusu, C.A. Collazos, Experimental validation of a set of cultural-oriented usability heuristics: e-Commerce websites evaluation, Comput. Stand. Interfaces 50 (2017) 160–178.
[30] R.X.E. de Almeida, S.B.L. Ferreira, D.S. da Silveira, M. Pimentel, R. Goldbach and A. T. Bessa, “Heurísticas de Usabilidad Orientadas às Redes Sociais”, in IV Encontro de Administração da Informação, 2013.
[31] K.R. da, H. Rodrigues, C.A.C. Teixeira, V.P. de, A. Neris, Heuristics for assessing emotional response of viewers during the interaction with TV programs, in: M. Kurosu (Ed.), Human–Computer Interaction, Part I, HCII, Springer, 2014, pp. 577–588 LNCS 8510.
[32] E.V. Neto, F.F.C. Campos, Evaluating the usability on multimodal interfaces: a case study on tablets applications, Design, User Experience, and Usability. Theories, Methods, and Tools for Designing the User Experience, Springer International Publishing, 2014, pp. 484–495.
[33] R. Yáñez Gómez, D.C. Caballero, J.L. Sevillano, Heuristic evaluation on mobile interfaces: a new checklist, Sci. World J. (2014).
[34] F. Paz, F.A. Paz, J.A. Pow-Sang, L. Collantes, Usability heuristics for transactional web sites, Proceedings of the 11th International Conference on Information Technology, 2014, pp. 627–628.
[35] N. Gale, P. Mirza-Babaei, I. Pedersen, Heuristic guidelines for wearable augmented reality applications, Proceedings of the 2015 Annual Symposium on Computer–Human Interaction in Play, CHI PLAY '15, 2015, pp. 529–534.
[36] L.C. Rocha, R.M. Andrade, A.L. Sampaio, V. Lelli, Heuristics to evaluate the usability of ubiquitous systems, Proceedings of International Conference on Distributed, Ambient, and Pervasive Interactions, Springer, 2017, pp. 120–141.
[37] F. Sanz, R. Gálvez, C. Rusu, S. Roncagliolo, V. Rusu, C.A. Collazos, J.P. Cofré, A. Campos, D. Quiñones, A set of usability heuristics and design recommendations for u-learning applications, Information Technology: New Generations, Springer International Publishing, 2016, pp. 983–993.
[38] A. Campos, C. Rusu, S. Roncagliolo, F. Sanz, R. Gálvez, D. Quiñones, Usability heuristics and design recommendations for driving simulators, Information Technology: New Generations, Springer International Publishing, 2016, pp. 1287–1290.
[39] A. Yeratziotis, D. Pottas, D. Vvan Greunen, A usable security heuristic evaluation for the online health social networking paradigm, Int. J. Hum.-Comput. Interaction 28 (10) (2012) 678–694.
[40] L. Kuparinen, J. Silvennoinen, H. Isomäki, Introducing usability heuristics for mobile map applications, Proceedings of the 26th International Cartographic Conference, 2013.
[41] J.S. Mtebe, M.M. Kissaka, Heuristics for evaluating usability of learning management systems in Africa, Proceedings of IST-Africa Conference, IEEE, 2015, pp. 1–13.
[42] G. Joyce, M. Lilley, Towards the development of usability heuristics for native smartphone mobile applications, in: A. Marcus (Ed.), Design, User Experience, and Usability. Theories, Methods, and Tools for Designing the User Experience, 8517 Springer International Publishing, 2014, pp. 465–474.
[43] A. Anganes, M.S. Pfaff, J.L. Drury, C.M. O'Toole, The heuristic quality scale, Interact. Comput. 28 (5) (2016) 584–597.
[44] F. Paz, F.A. Paz, J.A. Pow-Sang, L. Collantes, Usability heuristics for transactional web sites, Proceedings of the 11th International Conference on Information Technology, 2014, pp. 627–628.
[45] F. Paz, F.A. Paz, J.A. Pow-Sang, Experimental case study of new usability heuristics, Design, User Experience, and Usability: Design Discourse, Springer International Publishing, 2015, pp. 212–223.
[46] D. Quiñones, C. Rusu, S. Roncagliolo, Redefining usability heuristics for transactional web applications, Proceedings of the 11th International Conference on Information Technology: New Generations, ITNG, IEEE, 2014, pp. 260–265.
[47] D. Quinones, C. Rusu, S. Roncagliolo, V. Rusu, C. Collazos, Developing usability heuristics: a formal or informal process? IEEE Lat. Am. Trans. 14 (7) (2016) 3400–3409.
[48] D. Quiñones, A methodology to develop usability/user experience heuristics, Proceedings of the XVIII International Conference on Human Computer Interaction, 2017 Article No. 57.
[49] M. Chinosi, A. Trombetta, BPMN: an introduction to the standard, Comput. Stand. Interfaces 34 (1) (2012) 124–134.
[50] J. Nielsen, Usability 101: Introduction to Usability, 2012. https://www.nngroup.com/articles/usability-101-introduction-to-usability/ (Accessed 20 October 2017).
[51] P. Morville, User Experience Design, 2004. http://semanticstudios.com/user_experience_design/ (Accessed 26 October 2017).
[52] N. Aguirre, Experiencia de Usuario en Museos Virtuales, Undergraduate Thesis Pontificia Universidad Católica de Valparaíso, Chile, 2015.
[53] C. Rusu, V. Rusu, S. Roncagliolo, D. Quiñones, V.Z. Rusu, H.M. Fardoun, D.M. Alghazzawi, D. Quiñones et al. Proceedings of the International Conference on Social Computing and Social Media, Springer International Publishing, 2016, pp. 59–70.
[54] V. Rusu, C. Rusu, D. Quiñones, S. Roncagliolo, C.A. Collazos, What happens when evaluating social media's usability? Proceedings of the International Conference on Social Computing and Social Media, Springer, 2017, pp. 117–126.
[55] V. Rusu, C. Rusu, D. Guzmán, S. Roncagliolo, D. Quiñones, Online travel agencies as social media: analyzing customers’ opinions, Proceedings of the International Conference on Social Computing and Social Media, Springer, 2017, pp. 200–209.
