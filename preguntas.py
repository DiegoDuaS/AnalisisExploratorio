import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.stats.diagnostic as diag
import statsmodels.api as sm
from tabulate import tabulate

def top_10_budget_movies(df):
    top_10_budget = df.sort_values(by='budget', ascending=False).head(10)
    print(top_10_budget[['title', 'budget']])
    
def top_10_revenue_movies(df):
    top_10_revenue = df.sort_values(by='revenue', ascending=False).head(10)
    print(top_10_revenue[['title', 'revenue']])