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

def prueba_de_normalidad(column, column_name):
    ks_statistic, p_value = stats.kstest(column, 'norm', args=(np.mean(column), np.std(column)))

    # Imprimir los resultados
    print(f"Estadístico de prueba (ks_statistic) = {ks_statistic:.20f}")
    print(f"p-value = {p_value:.20f}")

    alpha = 0.05
    if p_value < alpha:
        print(f"Se rechaza la hipótesis nula: los datos de '{column_name}' NO provienen de una distribución normal." + "\n")
    else:
        print(f"No se rechaza la hipótesis nula: los datos de '{column_name}' parecen provenir de una distribución normal." + "\n")
        
def frecuencias(column):
    frecuencia = column.value_counts()
    porcentaje = column.value_counts(normalize=True) * 100
    tabla_frecuencia = pd.DataFrame({'Frecuencia': frecuencia, 'Porcentaje': porcentaje})
    print(tabla_frecuencia)
        
