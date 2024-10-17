import pandas as pd

# Charger les données depuis le fichier CSV
file_path = '../Data/analyse.csv'  # Chemin vers le fichier CSV
df = pd.read_csv(file_path)

# Supposons que vous avez un montant total à investir
total_investment = 100  # Exemple de montant que vous souhaitez investir

# Récupérer les prix et les profits sous forme de listes
prices = df['price'].tolist()
profits = df['profit'].tolist()
names = df['name'].tolist()

# Trouver le meilleur investissement (problème du sac à dos)
n = len(prices)

# Créer une table de programmation dynamique pour stocker les résultats
dp = [[0 for _ in range(total_investment + 1)] for _ in range(n + 1)]

# Remplir la table dp
for i in range(1, n + 1):
    for w in range(total_investment + 1):
        if prices[i - 1] <= w:
            dp[i][w] = max(profits[i - 1] + dp[i - 1][w - int(prices[i - 1])], dp[i - 1][w])
        else:
            dp[i][w] = dp[i - 1][w]

# Récupérer les actions qui donnent le meilleur profit
w = total_investment
selected_items = []
for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected_items.append(names[i - 1])
        w -= int(prices[i - 1])

# Afficher le résultat
max_profit = dp[n][total_investment]
print(f"Le meilleur profit possible est : {max_profit}")
print(f"Les actions sélectionnées sont : {', '.join(selected_items)}")
