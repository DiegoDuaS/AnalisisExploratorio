""""
Hoja de Trabajo 1 
Mineria de Datos 
Diego Duarte 22075
José Marchena 22
"""
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.stats.diagnostic as diag
import statsmodels.api as sm
from tabulate import tabulate

#Configuracion para mostrar todas las filas y columnas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#Importar Datos
movies=pd.read_csv("movies.csv", encoding="ISO-8859-1")

#Resumen del Conjunto de Datos
print(movies.describe())

print(movies.info())