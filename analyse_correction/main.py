import pandas as pd 
from infrastructures.sanitize import cleanData
from jobs.job_postgres import Hydrate
from jobs.job_csv import optimize
from config import fileName, amount

# job 1 - sanatize
investments = pd.read_csv(fileName)
investments = cleanData(investments)

# job 2 - optimize
investments = optimize(investments, amount)

# job 3 - hydrate database
hy = Hydrate(investments)
hy.execute()
