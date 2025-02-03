import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.stats.diagnostic as diag
import statsmodels.api as sm
from tabulate import tabulate

def top_10_budget_movies(df):
    #Ordenar los datos de mayor a menor por presupuesto, enseñar solo los primeros 10
    top_10_budget = df.sort_values(by='budget', ascending=False).head(10)
    print(top_10_budget[['title', 'budget']])
    
def top_10_revenue_movies(df):
      #Ordenar los datos de mayor a menor por ingresos, enseñar solo los primeros 10
    top_10_revenue = df.sort_values(by='revenue', ascending=False).head(10)
    print(top_10_revenue[['title', 'revenue']])
    
def top_votes(df):
      #Ordenar los datos de mayor a menor por cantidad de votos, enseñar solo el primero
    top_votes = df.sort_values(by='voteCount', ascending=False).head(1)
    print(top_votes[['title', 'voteCount']])

def worst_movie(df):
      #Ordenar los datos de menor a mayor por promedio en votos, enseñar solo el primero
    worst_movie = df.sort_values(by='voteAvg', ascending=True).head(1)
    print(worst_movie[['title', 'voteAvg']])
    
def movies_per_year(df):
    #Convertir a formato date_time para poder extraer el año 
    df['releaseDate'] = pd.to_datetime(df['releaseDate'], errors='coerce')
    
    #Estraer el año
    df['year'] = df['releaseDate'].dt.year
    
    #Ordenar por indice y el valor es la cantidad que aparece
    movies_per_year = df['year'].value_counts().sort_index()
    
    #Encontrar el año con más peliculas y la cantidad
    anio_mas_peliculas = movies_per_year.idxmax()
    cantidad_max = movies_per_year.max()

    print(f"El año con más películas fue {anio_mas_peliculas} con {cantidad_max} películas.")
    
    #Generar el gráfico
    plt.figure(figsize=(15, 6))

    movies_per_year.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.xlabel("Año")
    plt.ylabel("Cantidad de películas")
    plt.title("Número de películas producidas por año")
    
    plt.show()

# --------- Inciso F ---------- #
def recent_genre(df):
    recent_movies = df.sort_values(by='releaseDate').head(20)
    all_genres = recent_movies['genres']
    recent_genres = all_genres.str.split('|').explode().value_counts()
    print("Géneros en las 20 películas más recientes:\n",recent_genres)
    
def popular_genre(df):
    # Cálculo de Génerp Principal
    genres = df['genres']
    top_genre = genres.str.split('|').explode().value_counts()
    print("Género principal: \n",top_genre.head(1))
    
    # Histograma
    histogram = plt.figure(figsize=(12, 5))
    ax = histogram.add_subplot(1,1,1)
    ax.bar(top_genre.index, top_genre.values, color="skyblue")
    ax.set_xlabel("Género")
    ax.set_ylabel("Conteo")
    ax.set_title("Distribución de Géneros")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
    
def top_genre(df):
    top_movies = df.sort_values(by='popularity').head(20)
    top_genres = top_movies['genres']
    genre_count = top_genres.str.split('|').explode().value_counts()
    print("Géneros en 20 películas más populares: \n",genre_count)
    
# --------- Inciso G ---------- #
def genre_revenue(df):
    top_movies = df.sort_values(by="revenue", ascending=False).head(50)
    tm_genres = top_movies['genres'].str.split('|').explode().drop_duplicates().to_numpy()
    gen_revenue = pd.DataFrame(columns=['genre','revenueSum'])

    for gen in tm_genres:
        filtered = df[df['genres'].str.contains(gen, na=False)]
        tem = pd.DataFrame({'genre':[gen],'revenueSum': [filtered['revenue'].sum()]})
        gen_revenue = pd.concat([gen_revenue, tem],ignore_index=True)
    gr_sorted = gen_revenue.sort_values(by='revenueSum', ascending=False)
    print(gr_sorted)
    
# --------- Inciso H ---------- #
def actor_amount_influence(df):
    df1 = df[['revenue','actorsAmount']]
    fig, ax= plt.subplots(nrows=1, ncols=2,figsize=(12, 5))
    # Cantidad de Actores VS Ingresos
    ax[0].scatter(df1['actorsAmount'], df1['revenue'], color='blue', marker='o', label='Data Points')
    ax[0].set_xlabel('Cantidad de Actores')
    ax[0].set_ylabel('Ingresos')
    ax[0].set_title('Cantidad de Actores VS Ingresos de películas')

    # Año VS Cantidad de actores
    df2 = df[['releaseDate','actorsAmount']]
    df2['releaseDate'] = pd.to_datetime(df2['releaseDate'],errors='coerce').dt.year
    ax[1].scatter(df2['releaseDate'],df2['actorsAmount'])
    ax[0].set_xlabel('Año de lanzamiento')
    ax[0].set_ylabel('Cantidad de Actores')
    ax[0].set_title('Año de lanzamiento VS Cantidad de Actores en películas')
    plt.tight_layout()
    plt.show()

# --------- Inciso I ---------- #
def gender_proportion(df):
    dfi = df[['actorsAmount','castWomenAmount','castMenAmount','revenue','popularity']]
    dfi = dfi[dfi['revenue']!=0]
    dfi = dfi[dfi['castMenAmount']<500]
    dfi['total'] = dfi['castWomenAmount'] +dfi['castMenAmount']
    dfi['pWomen'] = dfi['castWomenAmount']/dfi['total']
    dfi['pMen'] = dfi['castMenAmount']/dfi['total']
    fig, ax= plt.subplots(nrows=1, ncols=2,figsize=(12, 5))

    ax[0].scatter(dfi['pWomen'], dfi['revenue'], color="skyblue")
    ax[0].set_xlabel("Proporción de Mujeres en el reparto")
    ax[0].set_ylabel("Ingresos de la película")
    ax[0].set_title("Proporción de Mujeres VS Ingresos")

    ax[1].scatter(dfi['pWomen'], dfi['popularity'], color="skyblue")
    ax[1].set_xlabel("Proporción de Mujeres en el reparto")
    ax[1].set_ylabel("Popilaridad de la película")
    ax[1].set_title("Proporción de Mujeres VS Popularidad")
    plt.tight_layout()
    plt.show()