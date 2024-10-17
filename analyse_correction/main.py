import pandas as pd 
from jobs.job_csv import cleanData, optimize
from jobs.job_postgres import Hydrate

file_path = './Data/analyse.csv'  # Chemin vers le fichier CSV
investments = pd.read_csv(file_path)
investments = cleanData(investments)

# job 1 
investments = optimize(investments, amount = 1500)

# job 2
hy = Hydrate(investments)

print(investments)
hy.execute()
