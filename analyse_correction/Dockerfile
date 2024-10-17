# Utiliser l'image officielle Python
FROM python:3.12-slim

# Installer les dépendances nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les packages Python à partir du fichier requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Installer les Taps et Targets pour Singer (exemple)
# RUN pip install target-postgres target-csv

# Définir le répertoire de travail
WORKDIR /usr/src/app

# Copier tous les fichiers de l'application
COPY . .

