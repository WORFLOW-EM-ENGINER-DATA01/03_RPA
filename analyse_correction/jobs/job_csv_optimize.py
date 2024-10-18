import numpy as np
import pandas as pd

def optimize_with_numpy(data: pd.DataFrame, amount: float):
    # Extraction des données nécessaires
    prices = data['price'].values
    profits = data['profit'].values
    quantities = data['quantity'].values
    names = data['name'].values

    # Définir la matrice pour la programmation dynamique
    num_items = len(prices)
    dp = np.zeros((num_items + 1, int(amount * 100) + 1))  # Multiplier par 100 pour travailler avec des entiers

    # Algorithme de programmation dynamique avec NumPy
    for i in range(1, num_items + 1):
        price = int(prices[i - 1] * 100)  # Conversion en centimes
        profit = profits[i - 1]
        quantity = quantities[i - 1]

        for w in range(price, int(amount * 100) + 1):
            max_quantity = min(quantity, w // price)
            for q in range(1, max_quantity + 1):
                dp[i, w] = max(dp[i, w], dp[i - 1, w - q * price] + q * profit)

    # Reconstruction de la solution
    w = int(amount * 100)
    selected_items = []

    for i in range(num_items, 0, -1):
        if dp[i, w] != dp[i - 1, w]:
            price = int(prices[i - 1] * 100)
            quantity = quantities[i - 1]
            chosen_quantity = 0

            while w >= price and dp[i, w] == dp[i, w - price] + profits[i - 1]:
                chosen_quantity += 1
                w -= price

            selected_items.append((names[i - 1], prices[i - 1], chosen_quantity))

    return selected_items
