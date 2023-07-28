import uvicorn
from fastapi import FastAPI
from sklearn.neighbors import NearestNeighbors
import os

# Crear una instancia de FastAPI
app = FastAPI(title='Proyecto Individual #1 - MLOP',
            description='Javier Melo - Data_PT02')  

# Definir la ruta al archivo CSV
csv_file_path = "DATA/df_movies1.csv"
csv_file_path_crew = "DATA/df_crewfinal.csv"



##########################################################################################

@app.get('/cantidad_filmaciones_mes', tags=['Consulta 1'])
def cantidad_filmaciones_mes(mes: str):
    df_movies = pd.read_csv(csv_file_path)

    meses = {
        'enero': 1,
        'febrero': 2,
        'marzo': 3,
        'abril': 4,
        'mayo': 5,
        'junio': 6,
        'julio': 7,
        'agosto': 8,
        'septiembre': 9,
        'octubre': 10,
        'noviembre': 11,
        'diciembre': 12
    }
    
    mes = mes.lower()
    
    if mes not in meses:
        return f"No se reconoce el mes '{mes.capitalize()}'"
    
    # Obtenemos el número del mes a partir del diccionario de mapeo
    numero_mes = meses[mes]
    
    # Convertimos la columna 'release_date' a tipo fecha
    df_movies['release_date'] = pd.to_datetime(df_movies['release_date'])
    
    # Filtramos las filas que corresponden al mes específico
    peliculas_mes = df_movies[df_movies['release_date'].dt.month == numero_mes]
    
    # Obtenemos la cantidad de películas estrenadas en el mes
    cantidad_peliculas = len(peliculas_mes)
    
    # Devolvemos la cantidad de películas en la respuesta
    return f"{cantidad_peliculas} cantidad de películas fueron estrenadas en el mes de {mes.capitalize()}"

##############################################################################################################

@app.get('/cantidad_filmaciones_dia', tags=['Consulta 2'])

# Función para contar la cantidad de películas estrenadas en un día de la semana específico
def cantidad_filmaciones_dia(dia):
    df_movies = pd.read_csv(csv_file_path)


  # Convertir el nombre del día a minúsculas para realizar la comparación
    dia = dia.lower()

    # Verificar si el valor del día es válido
    dias_validos = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    if dia not in dias_validos:
        return f"No se reconoce el día '{dia.capitalize()}'"
    

    # Filtrar el DataFrame para obtener las filas correspondientes al día consultado
    filmaciones_dia = df_movies[df_movies['dia'].str.lower() == dia]

    # Obtener la cantidad de películas estrenadas en el día consultado
    cantidad_filmaciones = len(filmaciones_dia)

    mensaje = f"La cantidad de películas estrenadas en {dia.capitalize()} es: {cantidad_filmaciones}"
    return {"mensaje": mensaje}


############################################

@app.get('/score_titulo', tags=['Consulta 3'])
def score_titulo(titulo_de_la_filmacion: str):
    df_movies = pd.read_csv(csv_file_path)
    # Filtrar la fila correspondiente al título de la filmación
    pelicula = df_movies[df_movies['title'] == titulo_de_la_filmacion]
    
    if pelicula.empty:
        return f"No se encontró la filmación con título '{titulo_de_la_filmacion}'"
    
    # Obtener el título, año de estreno y score de la película
    titulo = pelicula['title'].iloc[0]
    anio_estreno = pelicula['release_year'].iloc[0]
    score = pelicula['popularity'].iloc[0]
    
    # Devolver la información en la respuesta
    return f"La película {titulo} fue estrenada en el año {anio_estreno} con un score/popularidad de {score}"
#############################################################################

@app.get('/votos_titulo', tags=['Consulta 4'])
def votos_titulo(titulo_de_la_filmación):
    df_movies = pd.read_csv(csv_file_path)
    # Filtrar las filas que corresponden al título de la filmación
    pelicula = df_movies[df_movies['title'] == titulo_de_la_filmación]
    
    # Verificar si se cumplen las condiciones mínimas de votos (al menos 2000)
    cantidad_votos = int(pelicula['vote_count'].iloc[0])
    if cantidad_votos < 2000:
        return f"La película '{titulo_de_la_filmación}' no cumple con el mínimo de 2000 votos."
    
    # Obtener el título, cantidad de votos y valor promedio de las votaciones
    titulo = pelicula['title'].iloc[0]
    promedio_votos = pelicula['vote_average'].iloc[0]
    
    # Devolver la información en la respuesta
    return f"La película '{titulo}' cuenta con un total de {cantidad_votos} valoraciones, con un promedio de {promedio_votos}."

########################################################################
@app.get('/get_actor', tags=['Consulta 5'])
def get_actor(nombre_actor:str):
    df_movies = pd.read_csv(csv_file_path)

    # Filtrar las filas que corresponden al nombre del actor
    peliculas_actor = df_movies[df_movies['cast'].str.contains(nombre_actor, case=False, na=False)]
    
    # Filtrar las filas que corresponden a películas en las que el actor no es director
    peliculas_actor = peliculas_actor[~peliculas_actor['crew'].str.contains(nombre_actor, case=False, na=False)]
    
    # Obtener la cantidad de películas en las que ha participado el actor
    cantidad_peliculas = peliculas_actor.shape[0]
    
    # Verificar si el actor ha participado en al menos una película
    if cantidad_peliculas == 0:
        return f"El actor {nombre_actor} no ha participado en ninguna película."
    
    # Convertir los valores de la columna 'revenue' a tipo numérico
    peliculas_actor['revenue'] = pd.to_numeric(peliculas_actor['revenue'], errors='coerce')
    
    # Eliminar las filas con valores nulos en la columna 'revenue'
    peliculas_actor = peliculas_actor.dropna(subset=['revenue'])
    
    # Calcular el retorno total del actor sumando los retornos de las películas en las que ha participado
    retorno_total = peliculas_actor['revenue'].sum()
    
    # Calcular el promedio de retorno por película
    promedio_retorno = retorno_total / cantidad_peliculas
    
    # Devolver la información en la respuesta
    return f"El actor {nombre_actor} ha participado en {cantidad_peliculas} filmaciones. Ha conseguido un retorno total de {retorno_total} con un promedio de {promedio_retorno} por filmación."
    
############################################################

@app.get("/get_director/", tags=['Consulta 6'])
def nombre_director(nombre: str):

    df_movies = pd.read_csv(csv_file_path)
    df_movies_crew = pd.read_csv(csv_file_path_crew)

    # Filtrar las filas en las que el director aparece en la columna "crew_name" y "crew_job" contiene "Director"
    director_movies = df_movies_crew[(df_movies_crew['crew_name'].str.contains(nombre, case=False)) & (df_movies_crew['crew_job'].str.contains("Director"))]
    
    # Verificar si se encontraron películas del director
    if director_movies.empty:
        return {"mensaje": f"No se encontró al director {nombre} en la base de datos."}
    
    # Obtener los ID de las películas en las que el director ha trabajado
    movie_ids = director_movies['crews_id_M'].tolist()
    
    # Filtrar el dataset "df_movies" para obtener los nombres, años, presupuestos, ingresos y relación de las películas correspondientes
    movies = df_movies[df_movies['crews_id_M'].isin(movie_ids)]
    
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
            "relacion": row['return']
        })
    
    return {
        "nombre_director": nombre,
        "ganancias": ganancias,
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
    nn_model = NearestNeighbors(n_neighbors=6, metric='euclidean')
    nn_model.fit(features)

    # Encontrar las películas más similares
    _, indices = nn_model.kneighbors([[movie_popularity] + [0] * len(genres.columns)], n_neighbors=6)

    # Obtener los títulos de las películas recomendadas (excluyendo la película dada en la consulta)
    recommendations = movie_data.iloc[indices[0][1:]]['title']

    return recommendations.tolist()

@app.get("/recomendacion/{movie_title}", tags=['Machine Learning'])
def recomendar_pelicula(movie_title: str):
    recommended_movies = movie_recommendation(movie_title)
    return {"Peliculas Recomendadas": recommended_movies[:5]}  # Devuelve las primeras 5 películas recomendadas

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
