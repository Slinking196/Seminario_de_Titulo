# Experiencia del Cliente en Hostales de Valparaíso: Analizando las Opiniones de los Turistas

Virginica Rusu1(&), Cristian Rusu2, Daniela Quiñones2, Silvana Roncagliolo2, Victoria Carvajal2, y Martin Muñoz2

1 Universidad de Playa Ancha, Av. Playa Ancha 850, 2340000 Valparaíso, Chile — virginica.rusu@upla.cl
2 Pontificia Universidad Católica de Valparaíso, Av. Brasil 2241, 2340000 Valparaíso, Chile — {cristian.rusu, daniela.quinones, silvana.roncagliolo}@pucv.cl, victoria.carvajal.videla@gmail.com, m.a.feldstedt@gmail.com

## Resumen
La Experiencia del Cliente (Customer eXperience) es uno de los conceptos clave en la Ciencia del Servicio, un campo de investigación interdisciplinario orientado a la innovación sistemática de los servicios. La experiencia del turista, como cliente de servicios específicos, está fuertemente relacionada con la calidad de los servicios ofrecidos. Las agencias de viaje en línea generan comunidades donde los turistas pueden evaluar cuantitativa (puntuaciones) y cualitativamente (reseñas) los servicios que recibieron. Sus opiniones ofrecen información para otros viajeros al elegir servicios turísticos y proporcionan datos valiosos para los responsables de la toma de decisiones en entidades turísticas. Las opiniones de los turistas expresan de hecho sus experiencias como clientes. Muchas investigaciones se centran en los comentarios cualitativos de los turistas, evaluando sus reseñas con técnicas de big data y procesamiento de lenguaje natural. Sin embargo, nosotros nos centramos en los datos cuantitativos. El artículo presenta un estudio cuantitativo sobre las opiniones de los turistas que usaron servicios de alojamiento ofrecidos a través de la agencia de viajes en línea HostelWorld, en hostales de Valparaíso, Chile. Usamos estadística descriptiva para analizar el perfil de los turistas y estadística inferencial para analizar sus opiniones.

**Palabras clave:** Experiencia del Turista · Experiencia del Cliente · Ciencia del Servicio · Agencia de viajes en línea

## 1 Introducción

La Ciencia del Servicio es un campo de investigación interdisciplinario orientado a la innovación sistemática de los servicios. Uno de los conceptos clave en la Ciencia del Servicio es la Experiencia del Cliente (CX). No existe consenso sobre la definición de CX. Una definición amplia fue propuesta por Laming y Mason, que consideran que la CX incluye “las experiencias físicas y emocionales que ocurren a través de las interacciones con el producto y/o la oferta de servicio de una marca desde el punto de primer contacto directo y consciente, a través del viaje total hasta la etapa posconsumo” [1].

La CX se logra mediante una secuencia de interacciones entre el cliente y la empresa (o empresas), en todos los «puntos de contacto» [2, 3]. La evaluación de la CX es desafiante [4, 5]. Debe realizarse en cada punto de contacto, debe atender todos los productos/sistemas/servicios con los que el cliente interactúa y debe capturar la naturaleza específica del punto de contacto.

La CX y la Ciencia del Servicio son particularmente relevantes en el turismo. La oferta de servicios turísticos (y asociados) está creciendo rápidamente. Los canales tradicionales de promoción/venta/retroalimentación son reemplazados por canales virtuales: agencias de viaje en línea, museos virtuales, sitios web de atracciones turísticas, etc. La CX incluye interacciones con sistemas de software (sitios web), atención al cliente (presencial, por teléfono, por correo electrónico), así como las opiniones de otros turistas (compartidas en sitios especializados, redes sociales, encuestas personalizadas, etc.). La experiencia del turista, como cliente de servicios específicos, está fuertemente relacionada con la calidad de los servicios ofrecidos [6, 7].

A lo largo de los años, nuestro trabajo se ha centrado en evaluar la Experiencia de Usuario (UX) de sitios web relacionados con el turismo: agencias de viajes en línea, museos virtuales, parques nacionales. Utilizamos un enfoque interdisciplinario, enfocándonos en el área de aplicación (turismo), pero también en la especificidad de los productos implicados (sistemas de software).

Las agencias de viaje en línea generan comunidades donde los turistas pueden evaluar cuantitativa (puntuaciones) y cualitativamente (reseñas) los servicios que recibieron. Sus opiniones (1) ofrecen información para otros viajeros al elegir servicios turísticos, y (2) ofrecen información valiosa para los responsables de la toma de decisiones en entidades turísticas. Las opiniones de los turistas expresan de hecho sus experiencias como clientes.

Muchas investigaciones se centran en los comentarios cualitativos de los turistas, evaluando sus reseñas con técnicas de big data y procesamiento de lenguaje natural. Sin embargo, nosotros centramos nuestro trabajo en los datos cuantitativos. En estudios previos analizamos datos cuantitativos sobre la opinión de los viajeros disponibles en dos sitios de agencias de viajes en línea: www.tripadvisor.cl y www.hotelclub.com [8, 9]. Se identificaron relaciones y tendencias en los datos.

El artículo presenta un estudio cuantitativo sobre las opiniones de los turistas que utilizaron servicios de alojamiento ofrecidos a través de la agencia de viajes en línea HostelWorld [10] en hostales de Valparaíso, Chile. La Sección 2 presenta el estudio de caso. La Sección 3 discute los resultados de nuestro estudio. La Sección 4 destaca conclusiones y trabajo futuro.

## 2 Estudio de Caso: HostelWorld

HostelWorld es una agencia de viajes en línea que ofrece alojamiento en hostales de todo el mundo. Como se indica en www.hostelworld.com, trabaja con alrededor de 36,000 propiedades en 178 países (ver Fig. 1). Según declara, el sitio también ofrece más de 12 millones de reseñas verificadas de huéspedes. Las reseñas son tanto cualitativas (opinión de los huéspedes sobre el hostal) como cuantitativas. La evaluación cuantitativa incluye la percepción de los huéspedes sobre 7 dimensiones, que representan variables de la calidad del servicio:

- Calidad/precio
- Ubicación
- Ambiente
- Instalaciones
- Seguridad
- Personal
- Limpieza

Cada dimensión se califica en una escala de 1 (peor) a 10 (mejor). También está disponible una evaluación global, como promedio de las 7 dimensiones. La puntuación global también se asocia a una evaluación conceptual, siendo “Superb” la mejor, asociada a puntuaciones globales de 9.0 a 10.

El sitio ofrece una vista general de las reseñas de los huéspedes que incluye (ver Fig. 2):
- La puntuación global y la evaluación conceptual asociada,
- La evaluación conceptual en 3 dimensiones: Ubicación, Personal y Limpieza,
- El número total de reseñas de huéspedes disponibles para el hostal.

Como las 3 dimensiones mencionadas se muestran de entrada, parece que tienen un significado especial para los viajeros, desde la perspectiva de HostelWorld.

Al acceder a los detalles de una propiedad, se puede obtener acceso a:
- Puntuaciones en las 7 dimensiones, así como puntuación global y evaluación conceptual (ver Fig. 3),
- Puntuación global y evaluación conceptual de cada reseñante (ver Fig. 4).

Además, cada reseña también proporciona:
- «Nombre» del huésped (o «Anónimo»),
- País de residencia del huésped,
- Tipo de huésped,
- Grupo de edad,
- Número de reseñas que el huésped ha hecho y el nivel asociado de «experiencia», siendo «Globetrotter» el más alto,
- Fecha de la reseña.

Las reseñas se pueden ordenar por varios criterios: “Top Rated” (mejor valoradas), “Lowest Rated” (peor valoradas), “Newest” (más nuevas), “Oldest” (más antiguas) y “Age Group” (grupo etario). El usuario puede elegir mostrar todas las reseñas disponibles o solo las reseñas en inglés. El nivel de detalle, especialmente la «experiencia» del huésped, así como la flexibilidad en el filtrado y ordenamiento de reseñas, muestran la relevancia que tienen las opiniones de los huéspedes.

## 3 Resultados y Discusión

Extraímos todas las reseñas asociadas a hostales en Valparaíso, Chile, disponibles a fines de diciembre de 2016. Obtuvimos un total de 3,035 reseñas.

HostelWorld clasifica a los viajeros en 6 categorías, como sigue (se indica el número de reseñas por categoría):

- Femenino: 1129 reseñas (37.3%),
- Masculino: 1012 reseñas (33.3%),
- Pareja: 604 reseñas (19.9%),
- Grupo todo femenino: 98 reseñas (3.2%),
- Grupo todo masculino: 40 reseñas (1.3%),
- Grupo mixto: 152 reseñas (5%).

Cabe mencionar que la mayoría de las reseñas las realizan viajeros en solitario (70.6%), seguidos por parejas (19.9%) y grupos de viajeros (9.5%). No todos los viajeros reseñan los hostales donde se alojaron; sin embargo, parece que los viajeros en solitario son los huéspedes más frecuentes en los hostales.

Por grupo de edad, según la clasificación de HostelWorld, la cantidad de reseñas es la siguiente:

- 18–24: 877 reseñas (28.9%),
- 25–30: 1409 reseñas (46.5%),
- 31–40: 584 reseñas (19.2%),
- 41+: 165 reseñas (5.4%).

El mayor número de reseñas fue realizado por huéspedes de entre 25 y 30 años. Los hostales parecen ser preferidos por personas jóvenes, ya que el 75.4% de las reseñas fueron hechas por personas de hasta 30 años.

Por país de origen, la mayoría de las reseñas fueron hechas por viajeros extranjeros:

- 2,924 reseñas realizadas por viajeros extranjeros (96.3%),
- 111 reseñas realizadas por viajeros chilenos (3.7%).

Analizando el país de origen de los viajeros, la mayoría provienen de EE. UU. (489 reseñas, 16.1%), seguido por Inglaterra (380 reseñas, 12.5%), Alemania (308 reseñas, 10.1%), Australia (284 reseñas, 9.4%), Francia (199 reseñas, 6.6%) y Brasil (155 reseñas, 5.1%). Todos los demás países representan menos del 5% de los viajeros.

También agrupamos a los viajeros por región geográfica, según la definición de la Organización Mundial del Turismo (UNWTO). Por región, el número de reseñas es el siguiente (1 reseña no encaja en ninguna región geográfica):

- Europa: 1491 reseñas (49.1%),
- Américas: 1112 reseñas (36.6%),
- Asia y Pacífico: 401 reseñas (13.2%),
- Medio Oriente: 16 reseñas (0.5%),
- África: 14 reseñas (0.5%).

Comprobamos la normalidad de las 7 dimensiones usando la prueba de Kolmogorov–Smirnov (con p-valor ≤ 0.05 como regla de decisión). Verificamos la hipótesis:

- H0: la variable sigue una distribución normal,
- H1: la variable no sigue una distribución normal.

Como muestra la Tabla 1, ninguna de las variables sigue una distribución normal. Por lo tanto, usamos pruebas estadísticas no paramétricas para analizar los datos. En todas las pruebas se usó p-valor ≤ 0.05 como regla de decisión.

**Tabla 1.** Prueba de Kolmogorov–Smirnov para verificar una distribución normal.

| Valor | Calidad/precio | Ubicación | Ambiente | Instalaciones | Seguridad | Personal | Limpieza |
|---:|---:|---:|---:|---:|---:|---:|---:|
| p-valor | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

Usamos la prueba de Kruskal–Wallis H para comprobar la hipótesis:

- H0: no hay diferencias significativas entre las opiniones de diferentes tipos de viajeros,
- H1: hay diferencias significativas entre las opiniones de diferentes tipos de viajeros.

Como muestra la Tabla 2, no hay diferencias significativas entre las opiniones de diferentes tipos de viajeros en 3 dimensiones: Ubicación, Ambiente e Instalaciones. Se observan diferencias significativas en 4 dimensiones: Calidad/precio, Seguridad, Personal y Limpieza.

**Tabla 2.** Pruebas de Kruskal–Wallis H por tipo de viajeros (p-valores).

| Dimensión | Calidad/precio | Ubicación | Ambiente | Instalaciones | Seguridad | Personal | Limpieza |
|---:|---:|---:|---:|---:|---:|---:|---:|
| p-valor | 0.013 | 0.531 | 0.091 | 0.245 | 0.005 | 0.002 | 0.004 |

También usamos Kruskal–Wallis H para comprobar la hipótesis:

- H0: no hay diferencias significativas entre las opiniones de viajeros pertenecientes a diferentes grupos de edad,
- H1: hay diferencias significativas entre las opiniones de viajeros pertenecientes a diferentes grupos de edad.

Como muestra la Tabla 3, no hay diferencias significativas entre las opiniones de viajeros por grupo de edad en ninguna de las 7 dimensiones.

**Tabla 3.** Pruebas de Kruskal–Wallis H por grupo de edad (p-valores).

| Dimensión | Calidad/precio | Ubicación | Ambiente | Instalaciones | Seguridad | Personal | Limpieza |
|---:|---:|---:|---:|---:|---:|---:|---:|
| p-valor | 0.729 | 0.460 | 0.723 | 0.664 | 0.370 | 0.170 | 0.455 |

Usamos la prueba de Mann–Whitney U para comprobar la hipótesis:

- H0: no hay diferencias significativas entre las opiniones de viajeros chilenos y extranjeros,
- H1: hay diferencias significativas entre las opiniones de viajeros chilenos y extranjeros.

Como indica la Tabla 4, hay diferencias significativas entre las opiniones de viajeros chilenos y extranjeros en las 7 dimensiones.

**Tabla 4.** Pruebas de Mann–Whitney U por origen de los viajeros (doméstico vs internacional) — p-valores.

| Dimensión | Calidad/precio | Ubicación | Ambiente | Instalaciones | Seguridad | Personal | Limpieza |
|---:|---:|---:|---:|---:|---:|---:|---:|
| p-valor | 0.003 | 0.000 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000 |

Usamos Kruskal–Wallis H para comprobar la hipótesis:

- H0: no hay diferencias significativas entre las opiniones de viajeros pertenecientes a diferentes regiones geográficas,
- H1: hay diferencias significativas entre las opiniones de viajeros pertenecientes a diferentes regiones geográficas.

Como muestra la Tabla 5, existen diferencias significativas entre las opiniones de viajeros de diferentes regiones geográficas en las 7 dimensiones.

**Tabla 5.** Pruebas de Kruskal–Wallis H por región geográfica — p-valores.

| Dimensión | Calidad/precio | Ubicación | Ambiente | Instalaciones | Seguridad | Personal | Limpieza |
|---:|---:|---:|---:|---:|---:|---:|---:|
| p-valor | 0.015 | 0.002 | 0.004 | 0.004 | 0.006 | 0.004 | 0.000 |

La Tabla 6 presenta las puntuaciones medias por dimensión, así como la puntuación global general.

**Tabla 6.** Puntuaciones medias por dimensión.

| Categorías | Calidad/precio | Ubicación | Ambiente | Instalaciones | Seguridad | Personal | Limpieza | Puntuación global |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Por tipo de viajeros: ||||||||| 
| Femenino | 8.45 | 9.03 | 8.37 | 7.96 | 8.62 | 8.65 | 8.01 | 8.44 |
| Masculino | 8.71 | 9.11 | 8.52 | 8.14 | 8.83 | 8.96 | 8.38 | 8.67 |
| Pareja | 8.52 | 9.03 | 8.32 | 8.07 | 8.88 | 8.72 | 8.31 | 8.55 |
| Grupo todo femenino | 8.57 | 9.06 | 8.41 | 7.98 | 8.55 | 8.65 | 8.18 | 8.49 |
| Grupo todo masculino | 8.60 | 8.75 | 8.70 | 8.00 | 8.70 | 8.95 | 8.05 | 8.53 |
| Grupo mixto | 8.61 | 9.09 | 8.41 | 7.92 | 8.83 | 8.91 | 8.17 | 8.56 |
| Por grupo de edad: ||||||||| 
| 18–24 | 8.52 | 9.06 | 8.35 | 8.01 | 8.67 | 8.66 | 8.16 | 8.49 |
| 25–30 | 8.57 | 9.05 | 8.41 | 8.05 | 8.80 | 8.80 | 8.19 | 8.55 |
| 31–40 | 8.61 | 9.11 | 8.49 | 8.09 | 8.75 | 8.87 | 8.33 | 8.60 |
| 41+ | 8.59 | 8.97 | 8.55 | 8.00 | 8.80 | 9.04 | 8.17 | 8.59 |
| Por origen: ||||||||| 
| Doméstico (chileno) | 8.95 | 9.50 | 9.03 | 8.85 | 9.15 | 9.28 | 8.77 | 9.08 |
| Internacional (extranjeros) | 8.55 | 9.04 | 8.39 | 8.01 | 8.74 | 8.77 | 8.19 | 8.53 |
| Por región geográfica: ||||||||| 
| Europa | 8.51 | 9.00 | 8.37 | 7.96 | 8.69 | 8.71 | 8.06 | 8.47 |
| Américas | 8.67 | 9.17 | 8.54 | 8.19 | 8.86 | 8.92 | 8.39 | 8.68 |
| Asia y Pacífico | 8.51 | 8.95 | 8.25 | 7.97 | 8.74 | 8.70 | 8.27 | 8.49 |
| Medio Oriente | 8.00 | 8.88 | 7.75 | 7.88 | 8.25 | 8.50 | 8.50 | 8.25 |
| África | 8.29 | 9.14 | 8.14 | 7.86 | 8.43 | 8.71 | 7.86 | 8.35 |
| Todos los huéspedes | 8.56 | 9.06 | 8.42 | 8.04 | 8.75 | 8.79 | 8.21 | 8.55 |

Las puntuaciones medias por grupos son bastante homogéneas. En las 7 dimensiones, las diferencias son en su mayoría inferiores a 1 punto en una escala de 10 puntos. Las instalaciones obtienen la puntuación más baja en casi todos los casos, excepto para los viajeros del Medio Oriente; en su opinión, el Ambiente obtuvo la puntuación más baja.

Realizamos pruebas de Spearman q para comprobar la hipótesis:

- H0: q = 0, dos dimensiones son independientes,
- H1: q ≠ 0, dos dimensiones son dependientes.

**Tabla 7.** Prueba de Spearman q para las 7 dimensiones (coeficientes).

| Dimensión | Calidad/precio | Ubicación | Ambiente | Instalaciones | Seguridad | Personal | Limpieza |
|---:|---:|---:|---:|---:|---:|---:|---:|
| Calidad/precio | 1 | 0.393 | 0.613 | 0.641 | 0.483 | 0.570 | 0.606 |
| Ubicación | 0.393 | 1 | 0.358 | 0.355 | 0.418 | 0.368 | 0.374 |
| Ambiente | 0.613 | 0.358 | 1 | 0.570 | 0.401 | 0.623 | 0.519 |
| Instalaciones | 0.641 | 0.355 | 0.570 | 1 | 0.492 | 0.514 | 0.643 |
| Seguridad | 0.483 | 0.418 | 0.401 | 0.492 | 1 | 0.438 | 0.506 |
| Personal | 0.570 | 0.368 | 0.623 | 0.514 | 0.438 | 1 | 0.485 |
| Limpieza | 0.606 | 0.374 | 0.519 | 0.643 | 0.506 | 0.485 | 1 |

Como muestra la Tabla 7, todas las dimensiones están correlacionadas (débil, moderada o fuertemente). Hay 4 correlaciones fuertes:

- «Calidad/precio» está fuertemente correlacionada con «Ambiente», «Instalaciones» y «Limpieza»; cuando los viajeros consideran que obtuvieron una buena relación calidad/precio, también evalúan positivamente el ambiente del hostal, las instalaciones y su limpieza.
- «Instalaciones» está fuertemente correlacionada con «Limpieza»; una evaluación positiva de las instalaciones del hostal va acompañada de una evaluación positiva de su limpieza.

## 4 Conclusiones

La CX es un concepto clave en la Ciencia del Servicio, pero últimamente la comunidad de Interacción Humano‑Computadora (HCI) muestra un creciente interés en el campo. La experiencia del turista se centra en el turista como cliente de servicios específicos. Evaluar la experiencia del turista es tan desafiante como evaluar la CX en general.

Las agencias de viajes en línea generan comunidades donde los turistas evalúan cuantitativa (a través de puntuaciones) y cualitativamente (a través de reseñas) los servicios que recibieron. Muchas investigaciones se centran en los comentarios cualitativos de los turistas, pero nosotros nos centramos en los datos cuantitativos. Evaluamos más de 3,000 reseñas de hostales ubicados en Valparaíso, Chile, disponibles en la agencia de viajes en línea HostelWorld.

Las reseñas de los huéspedes parecen ser particularmente importantes para HostelWorld. La agencia ofrece una vista general de las reseñas a primera vista, pero también información detallada sobre todas las reseñas disponibles, así como sobre el nivel de experiencia de los huéspedes que realizaron esas reseñas. Además, ofrece opciones para ordenar y filtrar las reseñas. Tres de las 7 dimensiones evaluadas por los huéspedes parecen ser particularmente relevantes en la visión de HostelWorld: Ubicación, Personal y Limpieza.

No todos los viajeros realizan reseñas tras hospedarse en un hostal. Sin embargo, las reseñas disponibles muestran que los hostales de Valparaíso son preferidos por viajeros en solitario (70.6% de las reseñas) y por viajeros jóvenes (75.4%). El equilibrio de género se inclina ligeramente a favor de las viajeras. La mayoría de los viajeros son extranjeros; solo el 3.7% son chilenos. Por región geográfica, la mayoría proviene de Europa (49.1%); por país de origen, la mayor parte proviene de EE. UU. (16.1%).

No hay diferencias significativas entre las opiniones de los viajeros por grupo de edad en ninguna de las 7 dimensiones. Por el contrario, hay diferencias significativas entre las opiniones de viajeros domésticos y extranjeros en las 7 dimensiones. También hay diferencias significativas en las 7 dimensiones al analizar la opinión de los viajeros por región geográfica. Existen diferencias significativas por tipo de viajero en 4 de las 7 dimensiones: Calidad/precio, Seguridad, Personal y Limpieza.

Las opiniones de los huéspedes son relativamente homogéneas; en las 7 dimensiones, las diferencias son menores a 1 punto en una escala de 10 en la mayoría de los casos. Las instalaciones obtienen la puntuación más baja en la mayoría de los casos. Todas las dimensiones están correlacionadas en distintos grados.

Como trabajo futuro, ampliaremos nuestro estudio a hostales de otras ciudades. Sería particularmente interesante comparar la percepción de los viajeros sobre los hostales de Valparaíso y Viña del Mar, que están ubicados geográficamente juntos, pero son bastante diferentes en términos de lo que ofrecen como atractivos turísticos.

## Referencias

1. Laming, C., Mason, K.: Customer experience – an analysis of the concept and its performance in airline brands. Res. Transp. Bus. Manag. 10, 15–25 (2014).
2. Interaction Design Foundation: Customer Touchpoints - The Point of Interaction Between Brands, Businesses, Products and Customers. http://www.interaction-design.org/literature/article/customer-touchpoints-the-point-of-interaction-between-brands-businesses-products-and-customers. Accessed 20 Jan 2020.
3. Stein, A., Ramaseshan, B.: Towards the identification of customer experience touch point elements. J. Retail. Consum. Serv. 30, 8–19 (2016).
4. Grigoroudis, E., Siskos, Y.: Customer Satisfaction Evaluation: Methods for Measuring and Implementing Service Quality. Springer, Heidelberg (2010). https://doi.org/10.1007/978-1-4419-1640-2.
5. Rusu, V., Rusu, C., Botella, F., Quiñones, D., Bascur, C., Rusu, V.Z.: Customer eXperience: a bridge between service science and human-computer interaction. In: Ahram, T., Karwowski, W., Pickl, S., Taiar, R. (eds.) IHSED 2019. AISC, vol. 1026, pp. 385–390. Springer, Cham (2020). https://doi.org/10.1007/978-3-030-27928-8_59.
6. Tussyadiah, I.: Toward a theoretical foundation for experience design in tourism. J. Travel Res. 53(5), 543–564 (2014).
7. Bosangit, C., Hibbert, S., McCabe, S.: If I was going to die I should at least be having fun: travelblogs, meaning and tourist experience. Ann. Tour. Res. 55, 1–14 (2015).
8. Rusu, V., et al.: Assessing the customer eXperience based on quantitative data: virtual travel agencies. In: Marcus, A. (ed.) DUXU 2016. LNCS, vol. 9746, pp. 499–508. Springer, Heidelberg (2016). https://doi.org/10.1007/978-3-319-40409-7_47.
9. Rusu, V., Rusu, C., Guzmán, D., Roncagliolo, S., Quiñones, D.: Online travel agencies as social media: analyzing customers’ opinions. In: Meiselwitz, G. (ed.) SCSM 2017. LNCS, vol. 10282, pp. 200–209. Springer, Cham (2017). https://doi.org/10.1007/978-3-319-58559-8_17.
10. HostelWorld Homepage. http://www.hostelworld.com/. Accessed 20 Jan 2020.
