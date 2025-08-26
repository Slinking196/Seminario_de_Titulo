Aplicación de una metodología para desarrollar heurísticas de experiencia de usuario

Daniela Quiñones, Cristian Rusu

Pontificia Universidad Católica de Valparaíso, Valparaíso, Chile

Resumen

Un método de evaluación por heurísticas permite evaluar la usabilidad de dominios de aplicación. Para evaluar aplicaciones que presentan características específicas de dominio, los investigadores pueden usar, además de las heurísticas bien conocidas (habitualmente las de Nielsen), conjuntos de heurísticas de usabilidad específicas. Las heurísticas también pueden enfocarse en aspectos de la experiencia de usuario (UX) distintos de la usabilidad. En un trabajo anterior propusimos una metodología formal para establecer heurísticas de usabilidad/UX. La metodología tiene 8 etapas que incluyen actividades para formular, especificar, validar y refinar un nuevo conjunto de heurísticas para un dominio de aplicación específico. La metodología fue validada mediante opinión de expertos y varios estudios de caso. Aunque al especificar la metodología explicamos en detalle cada una de sus etapas, algunas actividades pueden resultar difíciles de ejecutar sin una guía que ayude al investigador a determinar cómo llevarlas a cabo. Este artículo presenta una explicación detallada sobre cómo aplicar cada etapa de la metodología para crear un nuevo conjunto de heurísticas para un dominio específico. Además, el artículo explica cómo iterar las etapas de la metodología y cuándo detener el proceso de desarrollo de nuevas heurísticas.

Palabras clave: Usabilidad · Experiencia de usuario · Evaluación por heurísticas · Heurísticas de usabilidad · Heurísticas de experiencia de usuario · Metodología

1 Introducción

Desarrollar nuevas heurísticas como instrumentos de evaluación se ha convertido en una actividad crítica para evaluar no solo la usabilidad y la experiencia de usuario (UX), sino también las características específicas de distintos dominios de aplicación. Es importante evaluar el dominio de aplicación considerando todos sus componentes, características y los atributos (o factores) de usabilidad/UX que son críticos en ese dominio.

La evaluación mediante heurísticas es un método de inspección ampliamente usado para evaluar usabilidad y, en muchos casos, aspectos de UX [1]. En este método, expertos inspeccionan un producto/sistema/servicio para identificar problemas de usabilidad/UX y "medir" el grado de usabilidad/UX según principios o heurísticas. Las heurísticas son reglas o pautas utilizadas para realizar la evaluación [3]. La evaluación por heurísticas es útil para detectar problemas de usabilidad/UX; sin embargo, puede ser necesario usar heurísticas específicas del dominio, porque cada dominio puede tener características únicas que requieren reglas de evaluación particulares [3].

Existen metodologías que apoyan el proceso de desarrollo de heurísticas [4–10]; sin embargo, hasta nuestro trabajo previo no había un protocolo claro para la validación heurística. Formalizamos el proceso completo y propusimos una metodología con actividades detalladas para cada etapa [11]. La metodología fue diseñada con entradas, actividades, salidas y diagramas BPMN para cada etapa y fue validada en varias iteraciones. Concluimos que la metodología es percibida como útil y efectiva: produce un "producto" final (un conjunto de heurísticas) y ha sido usada en diversos estudios de caso [11].

No obstante, aunque en la especificación inicial describimos cada etapa en detalle, algunos investigadores pueden necesitar una guía más práctica que explique cómo ejecutar actividades concretas (cómo clasificar y priorizar la información recopilada, qué documentar, etc.). Este artículo cubre esa necesidad: muestra cómo aplicar cada etapa, cómo iterar y cuándo detenerse.

La explicación se ilustra con el caso de desarrollo de heurísticas UX para sitios web de parques nacionales [12], complementada con otros estudios de caso.

2 Marco teórico

Usabilidad, evaluación y UX: la usabilidad suele definirse como la "capacidad de ser usado" y abarca eficacia, eficiencia y satisfacción en un contexto de uso (ISO 9241‑11) [14]. UX es un concepto más amplio que incluye percepciones, respuestas y aspectos emocionales antes, durante y después del uso (ISO 9241‑210) [14]. Hay más de 86 métodos para evaluar usabilidad y UX; en términos generales, los métodos se dividen en inspecciones (expertos) y pruebas con usuarios. La evaluación por heurísticas es uno de los métodos de inspección más usados [1].

2.1 Usabilidad

La usabilidad implica que un producto funcione de forma efectiva y eficiente y que el usuario pueda alcanzar sus objetivos con satisfacción. Cada usuario puede tener objetivos distintos y el contexto de uso influye en la interacción [15].

2.2 Experiencia de usuario (UX)

La UX no solo considera la facilidad de uso, sino también las respuestas emocionales y las percepciones. La norma ISO 9241‑210 define la UX como "las percepciones y respuestas de la persona resultantes del uso y/o del uso anticipado de un producto, sistema o servicio" [14]. Autores como Morville, Revang y Arhippainen & Tähti han propuesto modelos y factores que ayudan a descomponer la UX en atributos evaluables (p.ej. útil, usable, deseable, encontrable, accesible, creíble, valioso) [16–19].

2.3 Evaluación por heurísticas

La evaluación por heurísticas consiste en que expertos inspeccionan la interfaz basada en un conjunto de heurísticas para identificar problemas de usabilidad/UX. Las heurísticas de Nielsen (10 heurísticas) son las más utilizadas, pero suelen ser generales; por ello surgieron más de 80 conjuntos de heurísticas específicas para dominios concretos [3, 20, 21].

3 La metodología

Presentamos una metodología formal para desarrollar heurísticas de usabilidad/UX en dominios específicos [11]. La metodología consta de 8 etapas que pueden aplicarse de forma iterativa para refinar el conjunto de heurísticas. Validamos la metodología mediante opiniones de expertos y aplicaciones prácticas, demostrando su eficacia en distintos dominios (agencias de viaje online, sitios web, redes sociales, videojuegos, entre otros).

La metodología puede utilizarse para crear heurísticas o checklists que evalúen usabilidad y otros aspectos de UX (p. ej. jugabilidad, aprendibilidad) o incluso atributos distintos a la usabilidad (seguridad, adaptabilidad). La Figura 1 del artículo original muestra las 8 etapas.

Para cada etapa definimos: (1) una definición, (2) las entradas necesarias, (3) las actividades a realizar, (4) las salidas esperadas y (5) un diagrama BPMN que ilustra el flujo de trabajo. La Tabla 1 resume las etapas con sus entradas y salidas.

4 Cómo usar la metodología en la práctica: una guía de uso

Esta sección detalla cómo aplicar cada etapa y cómo iterar para crear un nuevo conjunto de heurísticas. El investigador puede adaptar las actividades según su caso. La explicación se organiza en dos partes: (1) en la Sección 4.1 describimos cómo aplicar cada etapa (entradas, actividades, salidas y cómo documentar), y (2) en la Sección 4.2 explicamos cómo iterar, cuándo y cuántas iteraciones realizar.

Se usa el caso de estudio de heurísticas UX para sitios web de parques nacionales [12] como ejemplo principal. También se incluyen ejemplos en comercio electrónico, grid computing y smartphones.

4.1 Cómo usar las etapas de la metodología

4.1.1 Paso 1: etapa exploratoria

• Entrada: Dominio de aplicación que requiere un nuevo conjunto de heurísticas o checklist.
• Salidas esperadas: (①) información sobre la aplicación (definiciones y características); (②) atributos de usabilidad y UX; (③) conjuntos de heurísticas y otros elementos relevantes.

El investigador realiza una revisión bibliográfica para recopilar definiciones, propósitos, contexto de uso, ventajas/desventajas y características generales y específicas del dominio. Las características generales son comunes a la mayoría de productos de software; las específicas distinguen el dominio (p.ej., tareas particulares, tipos de usuarios, clasificaciones del dominio, aplicaciones concretas).

Si no existen conjuntos de heurísticas relacionadas (dominios recientes), se recomienda recopilar otros elementos útiles (principios, recomendaciones de diseño, guías, patrones) que sirvan de base para crear las heurísticas.

4.1.2 Paso 2: etapa experimental (opcional)

• Entrada: dominio de aplicación.
• Salidas posibles: (④) características adicionales detectadas; (⑤) problemas de usabilidad detectados.

Esta etapa es opcional y consiste en analizar datos previos o ejecutar experimentos (p. ej. inspecciones guiadas) para identificar problemas o características no detectadas en la etapa exploratoria. Los resultados de esta etapa alimentan el Paso 3.

4.1.3 Paso 3: etapa descriptiva

• Entradas: información sobre la aplicación (①), atributos de usabilidad/UX (②), conjuntos de heurísticas y otros elementos (③), y opcionalmente ④ y ⑤.
• Salidas: (⑦) información seleccionada sobre la aplicación; (⑧) características seleccionadas; (⑨) atributos de usabilidad/UX priorizados; (⑩) conjuntos de heurísticas y elementos priorizados.

En esta etapa, el investigador prioriza y agrupa la información recolectada en cinco tópicos: (1) información del dominio; (2) características del dominio; (3) atributos de usabilidad/UX; (4) características adicionales; (5) problemas de usabilidad. Se sugiere usar una escala de prioridad de 3 niveles (3: muy importante; 2: algo importante; 1: no importante).

Ejemplo: en el caso de parques nacionales los autores recolectaron propuestas de atributos (ISO 9241, Nielsen, Morville) y seleccionaron las propuestas más útiles para su dominio (Tablas 2–4 en el artículo original muestran el proceso de priorización y justificación).

4.1.4 Paso 4: etapa correlacional

• Entradas: ⑦, ⑧, ⑨, ⑩.
• Salidas: ⑪ características, atributos y heurísticas coincidentes; ⑫ categorías (opcional).

Se realiza el emparejamiento entre características del dominio, atributos de usabilidad/UX y heurísticas existentes. Se identifica qué características están cubiertas por heurísticas existentes, cuáles están parcialmente cubiertas y cuáles no lo están (y por lo tanto requieren heurísticas nuevas). Opcionalmente, se agrupan heurísticas en categorías según convenga.

4.1.5 Paso 5: etapa de selección

• Entradas: ⑩ y ⑪.
• Salida: ⑬ heurísticas clasificadas (mantener, adaptar, crear y eliminar).

Se revisan heurísticas existentes y se decide cuáles mantener, adaptar, eliminar o crear. Es habitual encontrar redundancias que deben resolverse.

4.1.6 Paso 6: etapa de especificación

• Entradas: ⑥ (problemas con heurísticas existentes, opcional), ⑪, ⑫ (categorías, opcional), ⑬.
• Salida: ⑭ conjunto de heurísticas propuesto, formalmente especificado.

En esta etapa se define el número y contenido de las heurísticas, se decide si agruparlas por categorías y se especifican siguiendo una plantilla estandarizada (p.ej. id, nombre, definición, explicación, ejemplos, beneficios, problemas asociados). Se recomienda mantener un número moderado de heurísticas (aprox. 10–16) y usar checklists adicionales para más detalle.

4.1.7 Paso 7: etapa de validación

• Entrada: ⑭ conjunto de heurísticas propuesto.
• Salidas: ⑮ resultados de evaluaciones heurísticas; ⑯ resultados de juicio experto; ⑰ resultados de pruebas con usuarios.

La validación se realiza mediante tres tipos de experimentos: (1) evaluaciones heurísticas comparando el conjunto propuesto con heurísticas de control; (2) juicio de expertos (encuestas sobre utilidad, claridad, facilidad de uso y necesidad de checklists); (3) pruebas con usuarios para corroborar si los problemas detectados por heurísticas son percibidos como tales por los usuarios.

Para la validación por evaluación heurística se proponen criterios cuantitativos (C1–C5) y, en casos específicos, criterios adicionales (p.ej. C6 para dimensión cultural). Las métricas incluyen porcentajes de asociaciones correctas/incorrectas de problemas a heurísticas, cantidad de problemas identificados (específicos, severidad, criticidad), etc. Las fórmulas (1)–(5) del artículo original muestran cómo calcular CA, IA, ESS, ESV y ESC.

4.1.8 Paso 8: etapa de refinamiento

• Entradas: ⑮, ⑯, ⑰ (al menos una de ellas requerida).
• Salida: ⑱ documento de refinamiento que especifica qué heurísticas crear, refinar o eliminar, y qué pasos repetir.

Basado en los resultados de validación, se realiza la refinación: ajustar definiciones, ampliar la especificación, crear o eliminar heurísticas y decidir iteraciones adicionales. Recomendamos al menos dos iteraciones para un conjunto bien validado.

4.2 Iteración de las etapas

Si bien es posible completar las 8 etapas sin iteraciones, recomendamos aplicar la metodología de forma iterativa (al menos 2 iteraciones). En la primera iteración conviene ejecutar todas las etapas (salvo la 2 si es opcional); las iteraciones posteriores se enfocan en validación y refinamiento. El número y alcance de las iteraciones dependen de recursos disponibles (evaluadores, expertos, tiempo) y del dominio.

Los autores detallan diagramas de iteración para los casos de parques nacionales, smartphones y aspectos culturales (Fig. 2). Los ejemplos muestran cómo algunas iteraciones cubren desde investigación exploratoria hasta múltiples rondas de validación y refinamiento.

5 Conclusiones

El gran número de conjuntos de heurísticas desarrollados refleja la necesidad de instrumentos para evaluar dominios de aplicación específicos. Proponemos una metodología formal de 8 etapas para facilitar el desarrollo de heurísticas de usabilidad/UX. La metodología es flexible: permite decidir qué etapas ejecutar, cuántas iteraciones realizar y qué pasos repetir según el dominio y recursos. Recomendamos validación robusta y medidas estandarizadas de efectividad.

En trabajos futuros planeamos describir en detalle la aplicación completa de la metodología y adaptarla a atributos distintos de la usabilidad (p. ej. Customer eXperience). También exploraremos el apoyo mediante herramientas de software.

Conflictos de interés

Ninguno.

Agradecimientos

Los autores agradecen a todos los participantes (expertos e investigadores) involucrados en los experimentos, especialmente al grupo de investigación "UseCV" en Interacción Humano-Computador (PUCV). También agradecen a Dania Delgado y Daniela Zamora por compartir su trabajo sobre heurísticas para sitios de parques nacionales. El trabajo fue apoyado por la Universidad de Playa Ancha, Valparaíso, Chile.

Referencias

(Se preservan las referencias del documento original.)

[1] A. Anganes, M.S. Pfaff, J.L. Drury, C.M. O'Toole, The heuristic quality scale, Interact. with Comput. 28 (5) (2016) 584–597.
[2] J. Nielsen, R. Molich, Heuristic evaluation of user interfaces, Proceedings of CHI, 1990, pp. 249–256.
[3] J. Nielsen, Ten Usability Heuristics, NNGroup.
[4] C. Rusu, S. Roncagliolo, V. Rusu, C. Collazos, A methodology to establish usability heuristics, ACHI 2011, pp. 59–62.
[5] D. Van Greunen, A. Yeratziotis, D. Pottas, A three-phase process to develop heuristics, ZA-WWW 2011.
[6] M. Hub, V. Čapková, et al., Heuristic evaluation of usability of public administration portal, 2010.
... (referencias completas en el PDF original)


---
Archivo generado automáticamente: `markdowns/papers/applying_methodology_usability.md`.
