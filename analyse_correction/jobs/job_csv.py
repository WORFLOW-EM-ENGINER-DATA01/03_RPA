import pandas as pd
import numpy as np
from typing import Union, List, Dict
from domain.types import StockPurchaseList

def optimize(data: pd.DataFrame, amount: float) -> StockPurchaseList:
    # ordonner les données
    data.sort_values(by=['rate'], ascending=False)
    purchases = []
    for index, row in data.iterrows():
        max_purchase_count = min(int(amount // row['price']), row['quantity'])
        
        if max_purchase_count > 0:
            # Réduire le montant disponible
            amount = round(amount - (max_purchase_count * row['price']), 2)
            # Ajouter l'achat à la liste des achats
            purchases.append((row['name'], row['price'], max_purchase_count, amount))
            
    return purchases
    