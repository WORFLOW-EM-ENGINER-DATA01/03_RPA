# Pratique RPA

Dans cet exercice, vous allez créer une fonction qui lit les informations d'un fichier PDF de facturation, extrait les montants HT et TTC, et les enregistre dans un fichier CSV. 

Ce processus est typique des tâches d'automatisation robotique des processus (RPA).

1. **Installer les bibliothèques nécessaires :**
   ```bash
   pip install PyPDF pandas
   ```

1. **Créer une fonction pour extraire le texte du PDF :**
   Utilisez `PyPDF` pour lire le fichier PDF.

1. **Créer une fonction pour parser le texte et extraire les informations :**
   Utilisez des expressions régulières pour trouver les montants HT et TTC.

1. **Créer une fonction pour enregistrer les données dans un fichier CSV :**
   Utilisez `pandas` pour gérer les données et les enregistrer.
