import pandas as pd
import numpy as np
from typing import Union, List, Dict
from domain.types import StockPurchaseList

# faker
def faker(data, output) -> None:
    data['quantity'] = None
    data['quantity'] = data['quantity'].map(
        lambda num: np.random.randint(1_000, size=1)[0]
    )
    data.to_csv(output, index=False)

def cleanData(data):
    data_copy = data.copy()
    data_copy = data_copy[data_copy['price'] != 0]
    data_copy['price'] = abs(data['price'].astype(float))
    data_copy['profit'] = data['profit'].astype(float)
    data_copy['rate'] = None
    data_copy['rate'] = np.round(data['profit']/data['price'], 2)

    return data_copy