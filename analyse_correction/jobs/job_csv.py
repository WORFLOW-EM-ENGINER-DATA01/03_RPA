import pandas as pd
import numpy as np
from typing import Union, List, Dict
from domain.types import StockPurchaseList

# faker
def faker(data) -> None:
    data['quantity'] = None
    data['quantity'] = data['quantity'].map(
        lambda num: np.random.randint(1_000, size=1)[0])
    data.to_csv('./Data/analyse.csv', index=False)


def cleanData(data):
    data_copy = data.copy()
    data_copy = data_copy[data_copy['price'] != 0]
    data_copy['price'] = abs(data['price'].astype(float))
    data_copy['profit'] = data['profit'].astype(float)
    data_copy['rate'] = None
    data_copy['rate'] = np.round(data['profit']/data['price'], 2)

    return data_copy


def optimize(data: pd.DataFrame, amount: float) -> StockPurchaseList:
    # ordonner les données
    data.sort_values(by=['rate'])
    res = []
    for index, row in data.iterrows():
        # calculer combien d'action on peut acheter
        count = 0
        while amount > row.price and count <= row['quantity']:
            amount = round(amount - row.price, 2)
            count += 1

        if count > 0:
            res.append((
                row['name'],
                row['price'],
                count,
                amount)
            )

        if amount <= 0:
            return res

    return res
