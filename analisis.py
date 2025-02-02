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
    #Sacamos ks statistic
    ks_statistic, p_value = stats.kstest(column, 'norm', args=(np.mean(column), np.std(column)))

    # Imprimir los resultados
    print(f"Estadístico de prueba (ks_statistic) = {ks_statistic:.20f}")
    print(f"p-value = {p_value:.20f}")

    #Valor de (no me acuerdo que era jsjsjsj)
    alpha = 0.05
    if p_value < alpha:
        print(f"Se rechaza la hipótesis nula: los datos de '{column_name}' NO provienen de una distribución normal." + "\n")
    else:
        print(f"No se rechaza la hipótesis nula: los datos de '{column_name}' parecen provenir de una distribución normal." + "\n")
        
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

    # Graficar histograma
    axes[0].hist(column)
    axes[0].set_title(f'Histograma de {column_name}')
    axes[0].set_xlabel(column_name)
    axes[0].set_ylabel('Densidad')

    # Graficar boxplot
    axes[1].boxplot(column)
    axes[1].set_title(f'Boxplot de {column_name}')
    axes[1].set_ylabel(column_name)
    # Mostrar gráficos
    plt.tight_layout()
    plt.show()
        
def frecuencias(column):
    #Encontrar las veces que aparece cierto valor
    frecuencia = column.value_counts()
    #El porcentaje de los valores
    porcentaje = column.value_counts(normalize=True) * 100
    #Crear e imprimir la tabla
    tabla_frecuencia = pd.DataFrame({'Frecuencia': frecuencia, 'Porcentaje': porcentaje})
    print(tabla_frecuencia)
        
