# RPA projet

## API Plateform

### Implémentation de l'API de gestion des factures

Dans ce TP, vous allez mettre en œuvre une API de gestion des factures pour une plateforme de gestion administrative. 

## Objectifs

- Mettre en place une API RESTful pour la gestion des factures.
- Implémenter différentes fonctionnalités pour récupérer des factures en fonction de différents critères tels que l'année, la date, le nom du formateur, le nom de l'école, etc.
- Tester l'API à l'aide d'outils tels que Postman ou curl.

1. Mise en place de l'environnement

Utilisez API platform

1. Modèle de données

Utilisez le fichier qui se trouve dans le dossier Data : [factures](./app-fastapi-rpa/db/invoices.json)

Modèle des données en SQL

```txt
┌───────────────────────┐
│       Trainer         │
├───────────────────────┤
│ id (PK)               │
│ name (unique)         │
│ shortcode (unique)    │
│ training_level        │
└───────────────────────┘
           │
           │ 1
           │
           │ n
           ▼
┌───────────────────────┐
│       Invoice         │
├───────────────────────┤
│ id (PK)               │
│ invoice_number        │
│ client                │
│ amount_ht             │
│ hours_count           │
│ days_count            │
│ trainer_id (FK)       │
│ payment_due           │
└───────────────────────┘
           │
           │ 1
           │
           │ n
           ▼
┌───────────────────────┐
│  InterventionDate     │
├───────────────────────┤
│ id (PK)               │
│ invoice_id (FK)       │
│ start_date            │
│ end_date              │
└───────────────────────┘

```

### Table `Trainer` :

- `id`: Identifiant unique du formateur (clé primaire).
- `name`: Nom du formateur.
- `shortcode`: Code court unique associé au formateur.
- `training_level`: Niveau de formation du formateur.

### Table `Invoice` :

- `id`: Identifiant unique de la facture (clé primaire).
- `invoice_number`: Numéro unique de la facture.
- `client`: Nom du client associé à la facture.
- `amount_ht`: Montant hors taxes de la facture.
- `hours_count`: Nombre d'heures facturées.
- `days_count`: Nombre de jours facturés.
- `trainer_id`: Identifiant du formateur associé à la facture (clé étrangère vers la table `TRAINER`).
- `payment_due`: Délai de paiement de la facture.

### Table `InterventionDate` :

- `id`: Identifiant unique de la date d'intervention (clé primaire).
- `invoice_id`: Identifiant de la facture associée à la date d'intervention (clé étrangère vers la table `INVOICE`).
- `start_date`: Date de début de l'intervention.
- `end_date`: Date de fin de l'intervention.


1. Implémentation des endpoints

Implémentez les endpoints suivants pour récupérer les factures :

   1. `GET /invoices` : Récupère toutes les invoices.
   2. `GET /invoices/year/<annee>` : Récupère les factures pour une année spécifiée.
   3. `GET /invoices/date/<date>` : Récupère les factures pour une date spécifiée.
   4. `GET /invoices/trainer/<nom_formateur>` : Récupère les factures pour un formateur spécifié.
   5. `GET /invoices/bytrainer/<nom_formateur>` : Récupère les factures pour partitionner par formateur.
   6. `GET /invoices/school/<nom_ecole>` : Récupère les factures pour une école spécifiée.
   7. `GET /invoices/date/<date>/trainer/<name_trainer>` : Récupère les factures pour une date et un formateur spécifiés.
   8. `GET /factures/date/<date>/school/<name_school>` : Récupère les factures pour une date et une école spécifiées.
   9. `GET /factures/date/<date>/trainer/<name_trainer>/school/<name_school>` : Récupère les factures pour une date, un formateur et une école spécifiés.


1. Documentation

- Créez une documentation décrivant chaque endpoint, les paramètres acceptés et les réponses attendues.

## Livrables

- Code source de l'API.
- Documentation de l'API.
- Rapport décrivant les étapes de développement, les problèmes rencontrés et les solutions adoptées.
