# Introduction aux Expressions Régulières en Python

Les expressions régulières, souvent appelées regex ou regexp, sont des motifs de recherche de texte qui permettent de rechercher et de manipuler des chaînes de caractères de manière complexe et flexible. Le module `re` en Python fournit des fonctions pour travailler avec des expressions régulières.

## Utilisation du Module `re`

1. **Importer le Module :**
   Avant d'utiliser le module `re` 

   ```python
   import re
   ```

1. **Rechercher un Motif dans une Chaîne :**
   La fonction `re.search()` recherche un motif dans une chaîne et retourne le premier résultat trouvé :

   ```python
   text = "Le numéro de téléphone est 123-456-7890."
   match = re.search(r'\d{3}-\d{3}-\d{4}', text)
   if match:
       print("Numéro de téléphone trouvé :", match.group())
   ```

1. **Correspondance en Début de Chaîne :**
   Utilise `^` pour rechercher un motif au début de la chaîne :

   ```python
   text = "Bonjour, comment ça va ?"
   match = re.search(r'^Bonjour', text)
   if match:
       print("Motif trouvé au début de la chaîne")
   ```

1. **Correspondance en Fin de Chaîne :**
   Utilise `$` pour rechercher un motif à la fin de la chaîne :

   ```python
   text = "Bonjour, comment ça va ?"
   match = re.search(r'ça va \?$', text)
   if match:
       print("Motif trouvé à la fin de la chaîne")
   ```

1. **Utilisation de Groupes :**
   Les groupes permettent de capturer des parties spécifiques d'un motif :

   ```python
   text = "Le numéro de téléphone est 123-456-7890."
   match = re.search(r'(\d{3})-(\d{3})-(\d{4})', text)
   if match:
       print("Code régional :", match.group(1))
       print("Premiers chiffres :", match.group(2))
       print("Derniers chiffres :", match.group(3))
   ```

1. **Recherche de Toutes les Correspondances :**
   Utilise `re.findall()` pour trouver toutes les correspondances d'un motif dans une chaîne :

   ```python
   text = "Les numéros de téléphone sont 123-456-7890 et 987-654-3210."
   matches = re.findall(r'\d{3}-\d{3}-\d{4}', text)
   print("Numéros de téléphone trouvés :", matches)
   ```

1. **Remplacement de Texte :**
   Utilise `re.sub()` pour remplacer des correspondances de motifs par un texte spécifique :

   ```python
   text = "Le numéro de téléphone est 123-456-7890."
   new_text = re.sub(r'\d{3}-\d{3}-\d{4}', 'XXX-XXX-XXXX', text)
   print("Texte modifié :", new_text)
   ```
