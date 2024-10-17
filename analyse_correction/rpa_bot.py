import pandas as pd 
import numpy as np


data = pd.read_csv('./Data/analyse.csv')

# print(data.head(10))
# print(data.tail(10))

# Retirez du dataset les valeurs dont le prix est nul
# Retirez du dataset les valeurs dont le prix est nul

print( (data['price'] < 0).sum())

# On nettoye ces données
mask =

