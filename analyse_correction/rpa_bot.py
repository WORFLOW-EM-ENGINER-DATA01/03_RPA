import pandas as pd 
import numpy as np
from typing import TypedDict, Union, List

class DataFrameSchema:
    name: str
    price: float
    profit: float
    rate: float

data = pd.read_csv('./Data/analyse.csv')
# faker
def faker(data)-> None:
    data['quantity'] = None
    data['quantity'] = data['quantity'].map(lambda num : np.random.randint(1_000, size=1)[0] )
    data.to_csv('./Data/analyse.csv', index=False)
    
# faker(data)

# Retirez du dataset les valeurs dont le prix est nul

# print( (data['price'] < 0).sum())

# Nettoyage Les valeurs négatives sont une erreur de saisie 
data = data[ data['price'] != 0 ]
# on a caster en float pour effectuer des calculs
data['price'] = data['price'].astype(float)
data['profit'] = data['profit'].astype(float)

# on change les valeurs négatives en positives
data['price'] = abs(data['price'] )

# on place 500 comment faire le meilleur investissement avec ces actions ?
amount = 500
data['rate'] = np.round(data['profit']/data['price'], 2)

# print( data.head() )

def optimize(data : pd.DataFrame, amount : float)-> List:
    # ordonner les données
    data.sort_values(by=['rate'])
    res = []
    for index, row in data.iterrows():
        # calculer combien d'action on peut acheter
        count = 0
        while amount > row.price and count <= row['quantity']:
            amount = round( amount - row.price, 2 )
            count +=1
            
        if count > 0:
            res.append({
                'name' : row['name'], 
                'price' : row['price'], 
                'quantity' : count, 
                'credit' : amount } 
            )
        
        if amount <= 0:
            return res 
        
    return res 
            
        
print( optimize(data , amount))

    



