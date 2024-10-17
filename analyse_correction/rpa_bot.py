import pandas as pd 
import numpy as np


data = pd.read_csv('./Data/analyse.csv')

# print(data.head(10))
# print(data.tail(10))
# print( data.describe())

# Retirez du dataset les valeurs dont le prix est nul
# Retirez du dataset les valeurs dont le prix est nul

print( (data['price'] < 0).sum())

# Nettoyage Les valeurs négatives sont une erreur de saisie 

# on a retirer les valeurs nulles
data = data[ data['price'] != 0 ]
# on a caster en float pour effectuer des calculs
data['price'] = data['price'].astype(float)
data['profit'] = data['profit'].astype(float)

# on change les valeurs négatives en positives
data['price'] = abs(data['price'] )

# on place 500 comment faire le meilleur investissement avec ces actions ?
amount = 500