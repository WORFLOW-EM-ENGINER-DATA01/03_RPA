# Les fichiers

## Introduction à la Manipulation des Fichiers en Python

Python offre des fonctionnalités intégrées pour travailler avec des fichiers. Les fichiers peuvent être ouverts, lus, écrits et fermés à l'aide de fonctions fournies par Python.

## Ouvrir un Fichier

Pour ouvrir un fichier en Python, utilise la fonction `open()`. Cette fonction prend deux arguments : le chemin vers le fichier et le mode d'ouverture.

```python
# Ouvre un fichier en mode lecture
file = open("exemple.txt", "r")
```

## Modes d'Ouverture de Fichier

- `"r"` : Lecture seule (par défaut). Le fichier doit exister.
- `"w"` : Écriture seule. Crée un nouveau fichier ou écrase le contenu d'un fichier existant.
- `"a"` : Ajout. Écrit à la fin du fichier ou crée un nouveau fichier s'il n'existe pas.
- `"r+"` : Lecture et écriture. Le fichier doit exister.
- `"b"` : Mode binaire pour les fichiers non textuels.

## Lecture depuis un Fichier

Une fois le fichier ouvert, tu peux lire son contenu à l'aide de différentes méthodes :

```python
# Lecture de tout le contenu
content = file.read()

# Lecture d'une ligne
line = file.readline()

# Lecture de toutes les lignes dans une liste
lines = file.readlines()
```

## Écriture dans un Fichier

Pour écrire dans un fichier, ouvre-le en mode écriture puis utilise la méthode `write()` :

```python
# Ouvre le fichier en mode écriture
file = open("nouveau_fichier.txt", "w")

# Écriture dans le fichier
file.write("Bonjour, monde !\n")
file.write("C'est un nouveau fichier.")
```

## Fermeture d'un Fichier

Il est important de fermer un fichier après l'avoir utilisé pour libérer les ressources :

```python
file.close()
```

## Utilisation de la Clause `with`

Python offre une syntaxe plus propre pour ouvrir et fermer automatiquement un fichier en utilisant la clause `with` :

```python
with open("exemple.txt", "r") as file:
    content = file.read()
    # Le fichier est automatiquement fermé à la fin du bloc with
```

## Manipulation de Fichiers Texte et Fichiers Binaires

En Python, les fichiers texte et binaires sont manipulés de la même manière. Cependant, il est important de spécifier le mode approprié lors de l'ouverture d'un fichier binaire.

```python
# Ouvre un fichier binaire en mode lecture
with open("image.jpg", "rb") as file:
    content = file.read()
```
