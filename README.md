## HenryInd_Proj
## Proyecto Individual Javier Melo


README - Proyecto de Ciencia de Datos
Este es un README para el proyecto de Ciencia de Datos desarrollado por Javier Melo, un estudiante de la carrera "DATA SCIENCE" PT1.

## Tabla de Contenidos
1. Objetivo del Proyecto
2. ETL y EDA
3. Diccionario de datos
4. Análisis Exploratorio de Datos (EDA)
5. Sistema de Recomendación
6. API con FASTAPI

***
### Objetivo del Proyecto
***

El objetivo principal de este proyecto es crear un sistema de recomendación para una start-up que provee servicios de agregación de plataformas de streaming. El sistema de recomendación aún no ha sido implementado, por lo que el primer desafío es desarrollarlo. Sin embargo, los datos con los que se trabaja son poco maduros y requieren un proceso de limpieza y transformación.

El proyecto abarca diversas etapas, desde el tratamiento y recolección de datos (tareas de Data Engineer) hasta el entrenamiento y mantenimiento de un modelo de Machine Learning para realizar predicciones a medida que lleguen nuevos datos.

Durante el desarrollo de este proyecto, se aplicaron varias habilidades blandas que fueron fundamentales para su éxito.

El trabajo en este proyecto de forma independiente permitió demostrar autonomía, organización y capacidad para resolver problemas de manera efectiva.

Para mantener un seguimiento ordenado de las tareas y una gestión eficiente del proyecto, se utilizó la herramienta Trello, que permitió establecer metas, asignar plazos y priorizar las actividades adecuadamente.

Además, se hizo uso de habilidades de comunicación escrita, utilizando el formato de comentarios de Google en el código y redactando de manera clara y concisa para facilitar la comprensión de las ideas.

A lo largo del proyecto, se enfrentaron diversos desafíos que requerían pensamiento crítico y capacidad de aprendizaje autodirigido. Se investigaron soluciones a problemas técnicos y se adquirieron nuevos conocimientos en el área de Ingeniería de Datos y Machine Learning para poder desarrollar y aplicar modelos de aprendizaje automático de manera efectiva.

En resumen, este proyecto permitió fortalecer habilidades como la autonomía, la organización, la resolución de problemas, la comunicación escrita, el aprendizaje autodirigido y el pensamiento crítico. Estas habilidades resultaron fundamentales para lograr el éxito en el desarrollo del proyecto y se espera seguir cultivándolas en futuras oportunidades.

***
## ETL y EDA
***
### Exploración y Limpieza de Datos
***

En esta etapa de mi proyecto de Ciencia de Datos, realicé el proceso de Extracción, Transformación y Carga (ETL), lo que me permitió crear nuevos conjuntos de datos para obtener una visión más clara y enriquecedora de mis datos.

Durante la exploración y limpieza de los datos iniciales, realicé varias acciones para mejorar la calidad y utilidad de los datos. Desanidé campos como belongs_to_collection y production_companies, lo cual me permitió extraer información relevante que utilizé en consultas a la API. Esta información adicional me proporcionó una visión más detallada sobre las colecciones a las que pertenecen las películas y las compañías de producción involucradas, enriqueciendo así mi análisis.

Además, para garantizar la integridad de los datos, rellené los valores nulos en los campos revenue y budget con ceros. Esto me permitió manejar adecuadamente los datos faltantes y evitar problemas en etapas posteriores del proyecto.

También eliminé los registros con valores nulos en el campo release_date y aseguré que todas las fechas estén en el formato AAAA-mm-dd. Esta transformación fue esencial para analizar y comparar de manera efectiva las fechas de estreno de las películas.

Con el fin de ampliar las posibilidades de análisis, creé una nueva columna llamada release_year, que extrajo el año de lanzamiento de cada película. Esta adición me permitió realizar análisis basados en años y observar las tendencias a lo largo del tiempo, proporcionando una perspectiva temporal valiosa.

Para evaluar el rendimiento financiero de las películas, calculé un nuevo campo llamado return, que representa el retorno de inversión al dividir los campos revenue y budget. En casos donde no había datos disponibles, asigné el valor cero. Esta métrica brindó información valiosa sobre el rendimiento financiero de las películas, permitiéndome tomar decisiones informadas basadas en datos.

Por último, simplifiqué el conjunto de datos eliminando columnas irrelevantes como video, imdb_id, adult, original_title, poster_path y homepage. Esta acción redujo el ruido en los datos y me permitió centrarme en las características clave que impulsarían mi análisis y resultados.

En resumen, el proceso de ETL me permitió crear nuevos conjuntos de datos que mejoraron mi comprensión de los datos y me proporcionaron una base sólida para realizar análisis más profundos y reveladores.

***
### Diccionario de datos
***

En mi proyecto individual de Ciencia de Datos, decidí separar los datos en diferentes conjuntos y crear diccionarios de datos para cada uno de ellos. Esta estructura organizativa ha sido muy beneficiosa en varios aspectos.

Al separar los datos en conjuntos específicos, como datasets_final.csv, ML_data.csv, cast_data.csv, crew_data.csv y movie_genres.csv, logré una mayor modularidad y claridad en la estructura de mi proyecto. Cada archivo representa un aspecto distinto de los datos y me permite trabajar de manera independiente en cada uno de ellos, centrándome en sus características únicas.

El archivo ML_data.csv desempeñó un papel fundamental en mi proyecto de Machine Learning. Las columnas disponibles en este conjunto de datos me proporcionaron la información necesaria para realizar predicciones utilizando el algoritmo de "Vecinos más Cercanos" (K-Nearest Neighbors) en el contexto del aprendizaje automático. Utilizando estas características, pude entrenar el modelo y hacer predicciones precisas sobre la popularidad de las películas.

Los diccionarios de datos asociados a datasets_final.csv, cast_data.csv, crew_data.csv y movie_genres.csv proporcionan descripciones detalladas de cada columna en cada conjunto de datos. Esto es fundamental para comprender la información contenida en ellos. Conociendo el propósito y el significado de cada columna, puedo tomar decisiones más informadas y realizar análisis más precisos y relevantes.

En resumen, la separación de los datos en diferentes conjuntos y la creación de diccionarios de datos específicos para cada uno de ellos ha sido una elección estratégica en mi proyecto individual de Ciencia de Datos. Esta estructura modular y descriptiva me ha permitido realizar análisis más profundos, utilizar el conjunto de datos ML_data.csv para el entrenamiento de un modelo de Machine Learning y realizar predicciones precisas utilizando el algoritmo de "Vecinos más Cercanos" (K-Nearest Neighbors). Además, me ha proporcionado una visión más completa de los diferentes aspectos de las películas, como su información general, elenco, equipo de producción y géneros.

***
### Análisis Exploratorio de Datos (EDA)
***

Después de completar la limpieza de datos, realicé un análisis exploratorio exhaustivo utilizando técnicas estadísticas y visualizaciones. El análisis exploratorio se encuentra en un archivo en la carpeta "data_a_explorar" y se presenta en un notebook que contiene gráficas de exploración.

Durante el análisis exploratorio, utilicé diversas bibliotecas como pandas, numpy, matplotlib.pyplot y seaborn. Estas herramientas me permitieron llevar a cabo diferentes actividades, como calcular el porcentaje de valores faltantes en cada columna, filtrar las columnas con valores faltantes y examinar variables numéricas como "popularity", "vote_average", "vote_count", "runtime", "budget", "revenue" y "return".

También realicé cálculos de estadísticas descriptivas, como la media, mediana, desviación estándar y percentiles, para comprender la distribución de los datos. Generé histogramas y gráficos de caja para visualizar las variables numéricas, así como un gráfico de dispersión para analizar la relación entre los ingresos y presupuestos de las películas.

Además, realicé diversas visualizaciones para explorar la distribución de películas por mes y año de lanzamiento, los países con mayor producción cinematográfica, los géneros más populares a lo largo del tiempo, entre otros análisis. También generé un mapa de calor para examinar las relaciones entre las variables.

Este análisis exploratorio de datos fue fundamental para obtener conocimientos valiosos que nos ayudaron a comprender mejor el conjunto de datos y a tomar decisiones informadas en etapas posteriores del proyecto. Nos permitió descubrir patrones, identificar valores atípicos y obtener una comprensión más profunda de las características de las películas y su éxito financiero.

***
## Sistema de Recomendación
***
### Desarrollo de Modelos de Machine Learning
***

Además del análisis exploratorio de datos, implementé un modelo de Machine Learning para abordar el siguiente desafío:

Sistema de recomendación: Utilicé técnicas de filtrado colaborativo y/o basado en contenido para construir un sistema de recomendación de películas personalizadas.
Esto permitió a los usuarios descubrir nuevas películas en función de sus preferencias. A través de la API, los usuarios pueden ingresar el nombre de una película y el endpoint correspondiente les proporcionará 5 recomendaciones basadas en las características de la película y en las preferencias de otros usuarios con gustos similares. Esto mejora la experiencia del usuario al ofrecer sugerencias relevantes y personalizadas para su disfrute cinematográfico.

***
## API con FASTAPI
***
### Desarrollo de la API
***

La API se ha desarrollado utilizando FastAPI, un framework web de Python que nos ha permitido crear servicios web de manera rápida y eficiente. A continuación, se describen las librerías y frameworks utilizados en la creación de la API, junto con una breve explicación de su función y su uso en el proyecto:

FastAPI: FastAPI es un framework web de alto rendimiento basado en Python. Se ha utilizado para crear y gestionar la API, proporcionando rutas y controladores para las diferentes funciones y endpoints.

pandas: pandas es una librería de Python ampliamente utilizada para la manipulación y análisis de datos. Se ha utilizado para cargar y procesar los conjuntos de datos, permitiendo realizar consultas y llevar a cabo operaciones sobre ellos.

zipfile: zipfile es una librería de Python que permite trabajar con archivos comprimidos en formato ZIP. Se ha utilizado para descomprimir archivos ZIP que contenían los conjuntos de datos necesarios para la API.

sklearn.neighbors: sklearn.neighbors es un módulo de la librería scikit-learn que contiene algoritmos de vecinos más cercanos (K-Nearest Neighbors). Se ha utilizado para implementar funcionalidades relacionadas con el sistema de recomendación, como encontrar vecinos más cercanos basados en características similares.

Cada una de estas librerías y frameworks ha desempeñado un papel fundamental en el desarrollo de la API, permitiendo implementar diversas funcionalidades, desde el procesamiento de datos hasta la creación de modelos de Machine Learning para el sistema de recomendación. Su uso combinado ha proporcionado las herramientas necesarias para construir una API robusta y funcional.
