# Analyse de Données et Parsing de PDF de Facturation

Vous devez avoir les modules suivants

- Bibliothèque `PyPDF` pour lire les fichiers PDF
- Bibliothèque `re` pour les expressions régulières

## Étapes

1. **Installer les bibliothèques nécessaires :**
   ```bash
   pip install PyPDF
   ```

1. **Télécharger un fichier PDF de facturation : Facture_001.pdf dans le dossier Data**

1. **Créer une classe pour représenter une facture :**
   Utilisez des méthodes magiques pour gérer les opérations sur les objets facture.

1. **Écrire le script pour extraire les données :**
   Utilisez `PyPDF` pour lire le fichier PDF et `re` pour extraire les montants HT et TTC.

## Indication

1. Créez un fichier PDF à partir des données ci-après
1. Puis utilisez une facture quelconque, vous pouvez récupérer la facture se trouvant dans le dossier Data Facture_000100.pdf

```
Facture n°12345
Date : 21/05/2024

Description         Quantité      Prix Unitaire      Total HT
Produit A               2               50               100
Produit B               1               150              150

Montant Total HT : 250.00
Montant Total TTC : 300.00
```