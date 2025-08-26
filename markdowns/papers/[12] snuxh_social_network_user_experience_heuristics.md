# SNUXH: Un conjunto de heurísticas de experiencia de usuario para redes sociales

Daniela Quiñones *, Cristian Rusu, Diego Arancibia, Sebastián González y María Josée Saavedra

Pontificia Universidad Católica de Valparaíso, Escuela de Ingeniería Informática, Valparaíso 2340000, Chile; cristian.rusu@pucv.cl (C.R.); diego.arancibia.c01@mail.pucv.cl (D.A.); sebastian.gonzalez.c@mail.pucv.cl (S.G.); maria-josee.saavedra.c@mail.pucv.cl (M.J.S.)

*Correspondencia: daniela.quinones@pucv.cl

Recibido: 27 de agosto de 2020; Aceptado: 17 de septiembre de 2020; Publicado: 19 de septiembre de 2020

## Resumen

Con el crecimiento y la saturación de Internet, el uso de las redes sociales en línea ha aumentado. Actualmente las redes sociales son utilizadas por una amplia variedad de usuarios —con diferentes objetivos y en distintos contextos de uso—, por lo que es esencial diseñar aplicaciones de redes sociales intuitivas y fáciles de usar que generen una experiencia de usuario (UX) positiva. La evaluación heurística es un método consolidado que permite detectar problemas de usabilidad; un grupo de expertos evalúa un producto y/o sistema usando un conjunto de heurísticas como guía. Aunque la evaluación heurística está orientada a evaluar la usabilidad, puede ser útil para evaluar otros aspectos relacionados con la UX. Debido a las características específicas de las redes sociales, es necesario contar con un conjunto de heurísticas específico para evaluarlas. Se han propuesto conjuntos de heurísticas específicas para redes sociales, pero se enfocan únicamente en evaluar la usabilidad. Este artículo presenta un conjunto de heurísticas que atienden no solo problemas de usabilidad, sino también otros factores de UX: heurísticas de experiencia de usuario para redes sociales (SNUXH). El nuevo conjunto de heurísticas se desarrolló, validó y refinó en cuatro iteraciones. Los resultados obtenidos en la validación experimental indican que el conjunto SNUXH es útil y más efectivo que las heurísticas genéricas (heurísticas de Nielsen) al evaluar redes sociales.

**Palabras clave:** experiencia de usuario; usabilidad; redes sociales; evaluación heurística; heurísticas; validación experimental

## 1. Introducción

Hoy en día las redes sociales forman parte de la vida diaria de las personas. En un estudio realizado por GlobalWebIndex en 2018 con 113.932 usuarios de varios países [1], se concluyó que el 98% de los consumidores digitales son usuarios de redes sociales, y la adopción es alta incluso entre 55–64 años (94%). Las redes sociales han evolucionado a plataformas multimedia, y por ello los usuarios las usan tanto para informarse como para mantenerse en contacto con amigos o para entretenimiento.

Es un hecho que las redes sociales son ampliamente usadas. Una red social puede definirse como una estructura social formada por personas o entidades conectadas por algún tipo de relación o interés común [2]. Mantenemos estas redes usando dispositivos (smartphones, laptops, tablets) y aplicaciones. Existe una gran variedad de redes sociales y los usuarios eligen las que satisfacen sus expectativas y les permiten realizar las tareas deseadas (vender, compartir, leer noticias, etc.). Si una red social es difícil de usar o los usuarios no entienden su funcionamiento, puede causar frustración y pérdida de uso. Por ello, es crucial evaluar la usabilidad y la experiencia que los usuarios tienen al usar redes sociales, detectar problemas y corregirlos para mejorar la satisfacción.

La evaluación heurística [4] es un método ampliamente usado para evaluar usabilidad; sin embargo, dependiendo del conjunto de heurísticas empleadas, también permite evaluar otros atributos de UX [6–9]. La UX no es lo mismo que la usabilidad; la UX incluye dimensiones como accesibilidad, comunicabilidad, usabilidad, entre otras. Las conocidas heurísticas de Nielsen [10] se usan en evaluaciones generales, pero las redes sociales poseen características específicas que pueden hacer que un conjunto genérico de heurísticas no detecte problemas particulares [6,11,12].

Se han propuesto conjuntos de heurísticas para redes sociales [13–15], pero se enfocan en la usabilidad o en características muy concretas (p. ej., seguridad en redes de salud [14]). En este artículo presentamos SNUXH —un conjunto de heurísticas de experiencia de usuario orientadas a redes sociales— destinado a evaluar aspectos más amplios de la UX además de la usabilidad. SNUXH se desarrolló en cuatro iteraciones usando la metodología de Quiñones et al. [6,7], y se especifica cada heurística con 13 elementos: id, prioridad, nombre, definición, explicación, característica de red social, ejemplos, beneficios, problemas, checklist, atributo de usabilidad relacionado, atributo de UX relacionado y conjuntos de heurísticas existentes relacionados. SNUXH fue validado y refinado mediante experimentos con expertos y usuarios. La versión de la tercera iteración y su validación preliminar se pueden revisar en la referencia [16].

El artículo se organiza como sigue: la Sección 2 explora el marco teórico; la Sección 3 explica brevemente la metodología aplicada para desarrollar SNUXH; la Sección 4 muestra el proceso seguido para desarrollar SNUXH; la Sección 5 describe la validación y los resultados; la Sección 6 presenta el conjunto final de SNUXH; y la Sección 7 concluye y presenta trabajos futuros.

## 2. Marco teórico

Se presentan brevemente los conceptos de red social, UX, usabilidad y evaluación heurística. Además, se describe trabajo relacionado.

### 2.1 Redes sociales

Una red social es una estructura social formada por personas o entidades conectadas por algún tipo de relación o interés común [2]. Hoy, una red social está asociada a sitios web o aplicaciones móviles que permiten a los usuarios conectar con otros. Estas redes ofrecen perfiles públicos o semipúblicos, permiten incluir datos personales e interactuar mediante herramientas variadas [17]. Según ONTSI [19], las redes sociales se clasifican en directas e indirectas.

En redes directas hay colaboración entre personas con intereses comunes; los usuarios crean perfiles y gestionan su información y privacidad (p. ej., Facebook, YouTube, Twitter). Se pueden clasificar por propósito, modo de operación, grado de apertura y nivel de integración. En redes indirectas el perfil no siempre es visible; hay comunidades o grupos que dirigen la discusión (p. ej., Reddit, blogs).

Todas las redes sociales comparten seis características [2,17,19,20]: seguridad, conectividad, interacción, personalización, gestión de contenido y centro de ayuda.

### 2.2 Experiencia de usuario y usabilidad

La UX se define como “percepciones y respuestas de una persona resultantes del uso y/o uso anticipado de un producto, sistema o servicio” [21]. Incluye emociones, creencias, preferencias, percepciones, respuestas físicas y psicológicas, comportamientos y logros antes, durante y después del uso. La UX depende del usuario y su contexto.

Varios modelos describen la UX. Morville [22] propone siete factores: útil, usable, deseable, localizable, accesible, creíble y valioso. Arhippainen y Tähti [23] la descomponen en factores de usuario, sociales, culturales, contexto y producto. Kankainen [24] la ve como resultado de una acción motivada en un contexto específico.

La usabilidad es parte de la UX y se define como la medida en que un producto puede ser usado por usuarios especificados para lograr objetivos con efectividad, eficiencia y satisfacción en un contexto especificado [21]. La norma ISO 9241 identifica efectividad, eficiencia y satisfacción como atributos de usabilidad. Para SNUXH se usaron los factores de Morville y los atributos de usabilidad de ISO 9241.

### 2.3 Evaluación heurística

Los métodos de evaluación se clasifican en métodos de inspección (expertos) y métodos de prueba (usuarios). La evaluación heurística es un método de inspección propuesto por Nielsen y Molich [5,29], donde entre 3 y 5 expertos examinan una interfaz y encuentran problemas de usabilidad/UX usando heurísticas. Nielsen propuso 10 heurísticas generales (NH1–NH10) para evaluar diseño de interacción [10]. Debido a que pueden ser muy genéricas, se han generado heurísticas específicas para distintos dominios [11,12].

### 2.4 Trabajo relacionado

Esteves et al. [13] proponen ocho heurísticas orientadas a redes sociales con nombre y explicación breve, pero sin cubrir ciertos aspectos generales (p. ej., estética y minimalismo) ni presentar validación experimental. Yeratziotis et al. [14] presentan 11 heurísticas para la seguridad de redes sociales de salud, útiles pero demasiado específicas. Dubois [15] analiza redes sociales desde la psicología y propone checklists en lugar de heurísticas nombradas, lo que dificulta su uso en evaluaciones heurísticas.

## 3. Metodología aplicada para establecer SNUXH

Aunque existen varios conjuntos de heurísticas para dominios específicos [11,12], hay pocas metodologías formales para desarrollar y validar nuevas heurísticas [6,33–38]. El proceso de validación es crítico para asegurar que el nuevo conjunto detecte problemas generales y específicos del dominio [11,12].

SNUXH se desarrolló usando la metodología de Quiñones et al. [6,7], elegida por su claridad y por proponer métodos concretos de validación tanto cuantitativos como cualitativos. La metodología tiene ocho etapas aplicables iterativamente: 1) Exploratoria, 2) Experimental, 3) Descriptiva, 4) Correlacional, 5) Selección, 6) Especificación, 7) Validación y 8) Refinamiento. Cada etapa define entradas, actividades y salidas. (Ver Tabla 1 en el artículo original).

## 4. Aplicación de la metodología para establecer SNUXH

SNUXH se construyó durante cuatro iteraciones. La Figura 1 del artículo muestra las etapas realizadas en cada iteración. En la primera iteración se ejecutaron todas las etapas; las iteraciones subsiguientes se centraron en validar y mejorar el conjunto.

### 4.1 Primera iteración

Se realizó una revisión bibliográfica (Paso 1) sobre redes sociales, atributos UX/usabilidad y conjuntos de heurísticas existentes. En el Paso 2 se realizó una evaluación heurística de Facebook con tres conjuntos de heurísticas (Nielsen, Esteves y Yeratziotis). A partir de ese experimento se identificaron problemas, asociaciones incorrectas entre problemas y heurísticas, y heurísticas poco claras o faltantes.

En el Paso 3 se agrupó y priorizó la información: se seleccionaron seis características de redes sociales (seguridad, conectividad, interacción, personalización, gestión de contenido, centro de ayuda), tres atributos de usabilidad (efectividad, eficiencia, satisfacción) y cinco atributos de UX (útil, usable, deseable, localizable, creíble). En el Paso 4 se correlacionaron las características con atributos y heurísticas existentes; se observó que muchas características requerían heurísticas nuevas o adaptadas.

En el Paso 5 se mantuvieron, adaptaron o descartaron heurísticas existentes: no se mantuvo ninguna sin cambios, 25 se adaptaron, 9 se descartaron y se creó una nueva para gestión de contenido. En el Paso 6 se especificó la primera versión SNH (16 heurísticas). En el Paso 7 se validó mediante evaluaciones heurísticas comparando SNH con las heurísticas de Nielsen en Facebook. Los resultados mostraron que SNH fue más efectivo que NH según los cinco criterios definidos en la metodología (asociaciones correctas/incorrectas, número de problemas específicos, severidad y criticidad). En el Paso 8 se refinó el conjunto, eliminando dos heurísticas y mejorando especificaciones, y se planificó la segunda iteración.

### 4.2 Segunda iteración

Se realizaron los pasos 6–8: se creó SNWH (segunda versión) con 14 heurísticas y se añadió el elemento de checklist en la especificación. Se aplicó una encuesta a los tres evaluadores del experimento anterior para medir utilidad, claridad, facilidad de uso y necesidad de elementos adicionales. Los resultados mostraron buenas percepciones generales, aunque se señaló la necesidad de añadir checklists y mejorar la claridad de algunas heurísticas. En la refinación se ajustaron, eliminaron y unieron heurísticas, y se planificó tercera iteración.

### 4.3 Tercera iteración

Se repitieron los pasos 6–8 y se propuso SNXH (tercera versión) con 12 heurísticas. Se validó mediante pruebas con usuarios (co-discovery) y opinión de expertos: cuatro grupos (dos usuarios cada uno) realizaron tareas en Facebook y se identificaron problemas que fueron comparados con SNXH. Los resultados indicaron que la mayoría de problemas detectados estaban cubiertos por SNXH, aunque se identificaron huecos para nuevos heurísticos (por ejemplo, intuitividad de ciertos elementos). También se entrevistó a expertos HCI que propusieron mejoras (nombres más claros, separación entre prevención y recuperación de errores, evaluar flexibilidad de uso, entre otros). Con esta retroalimentación se planificó la cuarta iteración.

### 4.4 Cuarta iteración

Se realizó la especificación final SNUXH (cuarta versión) con 14 heurísticas, incorporando los refinamientos de iteraciones previas. La versión final se presenta en la Sección 6.

## 5. Validación de SNUXH

La validación de un nuevo conjunto de heurísticas es compleja. La metodología propuesta sugiere validación mediante evaluación heurística, juicio de expertos y pruebas de usuario. SNUXH se validó experimentalmente en tres iteraciones usando estos métodos.

### 5.1 Primera iteración: evaluación heurística

Se seleccionaron seis evaluadores para comparar SNH con las heurísticas de control (Nielsen). Facebook fue el caso de estudio. Dos grupos de tres evaluadores trabajaron por separado: grupo experimental (SNH) y grupo control (NH). Se compararon los problemas identificados mediante cinco criterios: asociaciones correctas/incorrectas, número de problemas específicos identificados, severidad, criticidad y número total de problemas. Los resultados mostraron que SNH superó a NH en las cinco métricas: detectó más problemas (42 vs 34), más problemas específicos, y mayor severidad/criticidad en los problemas encontrados. SNH obtuvo mejor porcentaje de asociaciones correctas (76.19% vs 52.9%) y menor porcentaje de asociaciones incorrectas.

Señalaron heurísticas con pocas o ninguna asociación y heurísticas cuya especificación debía clarificarse.

### 5.2 Segunda iteración: juicio de expertos

Se aplicó una encuesta a los tres evaluadores que usaron SNH para medir cuatro dimensiones por heurística: utilidad, claridad, facilidad de uso y necesidad de elementos adicionales (checklists). En promedio las heurísticas obtuvieron puntuaciones altas, destacando utilidad (4.25/5). Sin embargo, la claridad y la necesidad de checklists tuvieron puntuaciones algo menores, indicando la necesidad de mejorar redacción y añadir elementos de apoyo especialmente en heurísticas nuevas como privacidad y control de contenido.

### 5.3 Tercera iteración: pruebas de usuario y opinión experta

Se realizó una prueba co-discovery con ocho usuarios (cuatro grupos) para validar si los problemas detectados por evaluadores eran percibidos por usuarios y para hallar nuevos problemas. Las tareas planteadas (buscar ayuda rápida, crear eventos, invitar amigos, crear publicaciones y eliminar eventos) mostraron problemas reales que fueron comparados con SNXH: la mayoría estaban cubiertos, salvo algunos relacionados con la intuitividad de ciertos elementos. La opinión de expertos aportó recomendaciones concretas: homogeneizar terminología, separar prevención y recuperación de errores, aclarar nombres de heurísticas, evaluar consistencia entre plataformas, ampliar el alcance de la heurística de alertas/ notificaciones y considerar la flexibilidad de uso.

## 6. SNUXH: conjunto final de heurísticas de experiencia de usuario para redes sociales

Tras las iteraciones y validaciones, se consolidó SNUXH con 14 heurísticas. Se clasificaron según prioridad: cuatro heurísticas críticas (prioridad 3: SNUXH3, SNUXH12, SNUXH13, SNUXH14), siete importantes (prioridad 2) y tres útiles (prioridad 1). En términos de usabilidad: seis heurísticas evalúan efectividad, seis eficiencia y nueve satisfacción. En términos de UX: dos heurísticas evalúan lo "útil", nueve lo "usable", seis lo "deseable", cinco lo "localizable" y siete lo "creíble".

SNUXH12 es una heurística nueva enfocada en personalización y control del contenido publicado para proteger la sensibilidad del usuario y permitir filtrar o reportar contenido no deseado.

Cada heurística se presenta con una tabla que incluye: id, prioridad, nombre, definición, explicación, característica de red social, ejemplos, beneficios, problemas, checklist, atributo de usabilidad relacionado, atributo de UX relacionado y heurísticas existentes relacionadas. A continuación se resumen las 14 heurísticas (en el artículo original las Tablas 6–19 presentan cada una en detalle).

Resumidamente, las heurísticas son:

- SNUXH1: Retroalimentación visual y estado de la red social
- SNUXH2: Coincidencia entre la red social y el mundo real
- SNUXH3: Control y libertad del usuario
- SNUXH4: Consistencia y estándares en multiplataforma
- SNUXH5: Prevención de errores
- SNUXH6: Minimizar la carga de memoria del usuario
- SNUXH7: Diseño estético y minimalista
- SNUXH8: Flexibilidad y personalización
- SNUXH9: Ayudar a los usuarios a reconocer, diagnosticar y recuperarse de errores
- SNUXH10: Centro de ayuda
- SNUXH11: Percepción y estado del usuario
- SNUXH12: Control del contenido publicado
- SNUXH13: Control de privacidad
- SNUXH14: Seguridad y recuperación de la cuenta de usuario

Cada heurística incluye explicación, checklist y ejemplos (figuras en el artículo original) que facilitan su aplicación.

## 7. Conclusiones

Las redes sociales son usadas con diversos propósitos y los usuarios esperan interacciones naturales, agradables e intuitivas. Evaluar la UX es esencial para detectar elementos que dificultan la interacción y corregirlos. Dado que las redes sociales tienen características específicas, hace falta un instrumento específico. Aunque existen conjuntos de heurísticas para redes sociales, suelen evaluar solo parte de la UX (por ejemplo, la usabilidad).

Se propuso SNUXH, un conjunto de 14 heurísticas orientadas a evaluar tanto aspectos de UX (útil, usable, deseable, localizable, creíble) como atributos de usabilidad (efectividad, eficiencia, satisfacción). Las heurísticas se desarrollaron siguiendo una metodología formal y fueron validadas experimentalmente en cuatro iteraciones mediante evaluación heurística, juicio de expertos y pruebas con usuarios.

Los resultados muestran que SNUXH es efectivo y supera a las heurísticas genéricas (Nielsen) en los criterios evaluados. Los expertos percibieron SNUXH como útil y fácil de usar, aunque sugirieron mejoras que fueron incorporadas.

Limitaciones: la validación inicial se centró en Facebook; es necesario evaluar SNUXH en otras redes (Twitter, Instagram) y con usuarios de distintos rangos etarios. En trabajos futuros se propone validar SNUXH en más redes y plataformas (desktop y mobile).

## Agradecimientos y referencias

Los autores agradecen a los participantes (expertos e investigadores) involucrados en los experimentos y al grupo de investigación UseCV en HCI (PUCV). Daniela Quiñones es financiada por ANID (FONDECYT Iniciación Nº 11190759).

El artículo incluye apéndices con detalles metodológicos, tablas y referencias completas (ver el archivo fuente).

---

**Licencia:** Este artículo es de acceso abierto y se distribuye bajo los términos de la licencia Creative Commons Attribution (CC BY) (http://creativecommons.org/licenses/by/4.0/).
