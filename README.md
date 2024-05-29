# Démarrage 

```bash
# Soit du Python en local
docker build -t env-python .
docker run -it --rm --name env-running-python -v ./:/usr/src/app env-python /bin/bash

# Soit directement jupyter 
# docker pull jupyter/datascience-notebook
docker run -it --rm -p 10000:8888 -v "${PWD}":/home/jovyan/work quay.io/jupyter/datascience-notebook:2024-04-29

# Token et mot de passe
jupyter server list
# récupération du token et définition du mot de passe

docker run -p 1080:1080 -p 1025:1025 maildev/maildev
psql -h localhost -U admin -d db

docker exec -it docker_postgres psql -U admin 
``` 

# Syntaxe pour faire une requête SQL avec un champ JSON en Postgres

```sql
SELECT *
FROM invoices
WHERE intervention_dates->>'start_date' = :start_date
```