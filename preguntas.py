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
