import uvicorn
from fastapi import FastAPI
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import os

# Crear una instancia de FastAPI
app = FastAPI(title='Proyecto Individual #1 - MLOP',
            description='Javier Melo - Data_PT02')  

# Definir la ruta al archivo CSV

csv_file_path = "DATA/df_movies1.csv"
csv_file_path_crew = "DATA/df_crewfinal.csv"

##########################################################################################

@app.get('/peliculas_idioma/{idioma}', tags=['Consulta 1'])
def peliculas_idioma(idioma: str):
    df_movies = pd.read_csv(csv_file_path)

    # Convertimos la columna 'spoken_languages' a tipo lista de diccionarios
    df_movies['spoken_languages_desanidada'] = df_movies['spoken_languages_desanidada'].apply(eval)

    # Filtramos las filas que contienen el idioma específico en la lista de idiomas
    peliculas_idioma = df_movies[df_movies['spoken_languages_desanidada'].apply(lambda x: any(d['name'].lower() == idioma.lower() for d in x))]

    # Obtenemos la cantidad de películas en el idioma especificado
    cantidad_peliculas = len(peliculas_idioma)

    # Devolvemos la cantidad de películas en la respuesta
    return f"{cantidad_peliculas} esta es la cantidad de películas que fueron estrenadas en el idioma {idioma}"


##############################################################################################################

@app.get('/peliculas_duracion/{pelicula}', tags=['Consulta 2'])
def peliculas_duracion(pelicula: str):
    df_movies = pd.read_csv(csv_file_path)

    # Convertimos la columna 'release_date' a tipo fecha
    df_movies['release_date'] = pd.to_datetime(df_movies['release_date'])

    # Convertimos la columna 'runtime' a tipo numérico (puede ser necesario si está en formato de texto)
    df_movies['runtime'] = pd.to_numeric(df_movies['runtime'], errors='coerce')

    # Filtramos la película específica
    pelicula_info = df_movies[df_movies['title'].str.lower() == pelicula.lower()]

    if pelicula_info.empty:
        return f"No se encontró información para la película '{pelicula}'"

    # Obtenemos la duración y el año de la película
    titulo = pelicula_info['title'].iloc[0]
    duracion = pelicula_info['runtime'].values[0]
    anio = pelicula_info['release_date'].dt.year.values[0]

    # Devolver la información en la respuesta
    return f"La película {titulo} fue estrenada en el año {anio} con una duración de {duracion} minutos."


############################################################################

@app.get('/franquicia/{franquicia}', tags=['Consulta 3'])
def franquicia(franquicia: str):
    df_movies = pd.read_csv(csv_file_path)
    
    # Filtrar las filas correspondientes a la franquicia
    peliculas_franquicia = df_movies.query("name_collect == @franquicia")

    if peliculas_franquicia.empty:
        return f"No se encontraron películas para la franquicia '{franquicia}'"

    # Convertir los valores de la columna 'revenue' a números (float)
    peliculas_franquicia['revenue'] = pd.to_numeric(peliculas_franquicia['revenue'], errors='coerce')

    # Calcular la cantidad de películas, ganancia total y ganancia promedio
    cantidad_peliculas = peliculas_franquicia.shape[0]
    ganancia_total = peliculas_franquicia['revenue'].sum()
    ganancia_promedio = peliculas_franquicia['revenue'].mean()

    # Construir el mensaje de respuesta formateando los números
    mensaje = "La franquicia {franquicia} posee {cantidad_peliculas} películas, una ganancia total de ${ganancia_total:,.0f} y una ganancia promedio de ${ganancia_promedio:,.0f}".format(
        franquicia=franquicia,
        cantidad_peliculas=cantidad_peliculas,
        ganancia_total=ganancia_total,
        ganancia_promedio=ganancia_promedio
    )

    # Retornar el mensaje en formato JSON
    return {'mensaje': mensaje}

#############################################################################

@app.get('/peliculas_pais/{pais}', tags=['Consulta 4'])
def peliculas_pais(pais: str):
    df_movies = pd.read_csv(csv_file_path)
    
    # Filtrar las filas correspondientes al país
    peliculas_en_pais = df_movies.query("name_country == @pais")

    # Calcular la cantidad de películas producidas en el país
    cantidad_peliculas = peliculas_en_pais.shape[0]

    # Construir el mensaje de respuesta
    mensaje = f"En el país {pais} se han producido {cantidad_peliculas} películas."

    # Retornar el mensaje en formato JSON
    return {mensaje}

########################################################################

@app.get('/productoras_exitosas/{productora}', tags=['Consulta 5'])
def productoras_exitosas(productora: str):
    df_movies = pd.read_csv(csv_file_path)
    
    # Filtrar las filas correspondientes a la productora
    peliculas_productora = df_movies.query("name_company == @productora")

    if peliculas_productora.empty:
        return f"No se encontraron películas para la productora '{productora}'"

    # Convertir los valores de la columna 'revenue' a números (float)
    peliculas_productora['revenue'] = pd.to_numeric(peliculas_productora['revenue'], errors='coerce')

    # Calcular el revenue total y la cantidad de películas
    revenue_total = peliculas_productora['revenue'].sum()
    cantidad_peliculas = peliculas_productora.shape[0]

    # Construir el mensaje de respuesta
    mensaje = f"La productora {productora} ha tenido un revenue de ${revenue_total:,} y ha realizado {cantidad_peliculas} películas."

    # Retornar el mensaje en formato JSON
    return {'mensaje': mensaje}

############################################################

@app.get("/get_director/{nombre}", tags=['Consulta 6'])
def nombre_director(nombre_director: str):
    
    df_movies = pd.read_csv(csv_file_path)
    df_movies_crew = pd.read_csv(csv_file_path_crew)
    
    # Filtrar las filas en las que el director aparece en la columna "crew_name" y "crew_job" contiene "Director"
    director_movies = df_movies[(df_movies['crew'].str.contains(nombre_director, case=False)) & (df_movies_crew['crews_job'] == "Director")]

    # Verificar si se encontraron películas del director
    if director_movies.empty:
        return {"mensaje": f"No se encontró al director {nombre_director} en la base de datos."}

    # Obtener los ID de las películas en las que el director ha trabajado
    movie_ids = director_movies['id'].tolist()

    # Filtrar el DataFrame "df_unidos" para obtener los nombres, años, presupuestos, ingresos y relación de las películas correspondientes
    movies = df_movies[df_movies['id'].isin(movie_ids)]

    # Calcular las ganancias sumando todas las relaciones de las películas
    ganancias = round(movies['return'].sum(), 2)

    # Crear una lista de diccionarios con los ID, nombres, años, presupuestos, ingresos y relación de las películas
    movie_info = []
    for _, row in movies.iterrows():
        
        movie_info.append({
            "id": row['id'],
            "titulo": row['title'],
            "anio": row['release_year'],
            "presupuesto": row['budget'],
            "ingresos": row['revenue'],
            "retorno_pelicula": row['return']
        })

    return {
        "nombre_director": nombre_director,
        "retorno_total_director": ganancias,
        "peliculas": movie_info
    }

###################################################################################################################

def movie_recommendation(movie_title):
    movie_data = pd.read_csv('DATA/ML_data_movies.csv') 
    # Buscar la película por título en la columna 'title'
    movie = movie_data[movie_data['title'] == movie_title]

    if len(movie) == 0:
        return "La película no se encuentra en la base de datos."

    # Obtener el género y la popularidad de la película
    movie_genre = movie['genero'].values[0]
    movie_popularity = movie['popularity'].values[0]

    # Crear una matriz de características para el modelo de vecinos más cercanos
    features = movie_data[['popularity']]
    genres = movie_data['genero'].str.get_dummies(sep=' ')
    features = pd.concat([features, genres], axis=1)

    # Manejar valores faltantes (NaN) reemplazándolos por ceros
    features = features.fillna(0)

    # Crear el modelo de vecinos más cercanos
    nn_model = NearestNeighbors(n_neighbors=11, metric='euclidean')
    nn_model.fit(features)

    # Encontrar las películas más similares
    _, indices = nn_model.kneighbors([[movie_popularity] + [0] * len(genres.columns)], n_neighbors=6)

    # Obtener los títulos de las películas recomendadas (excluyendo la película dada en la consulta)
    recommendations = movie_data.iloc[indices[0][1:]]['title']

    return recommendations.tolist()

@app.get("/recomendacion/{movie_title}", tags=['Machine Learning'])
def recomendar_pelicula(movie_title: str):
    recommended_movies = movie_recommendation(movie_title)
    return {"Peliculas Recomendadas": recommended_movies[:6]}  # Devuelve las primeras 5 películas recomendadas

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
