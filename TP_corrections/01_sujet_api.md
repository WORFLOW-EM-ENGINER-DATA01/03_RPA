# Projet RPA

## Partie 1 Plateforme API

### Implémentation de l'API de gestion des factures

Dans ce TP, vous allez mettre en œuvre une API de gestion des factures pour une plateforme de gestion administrative afin de faire le bilan pédagogique et financier d'un organisme de formation.

## Objectifs

- Mettre en place une API RESTful pour la gestion des factures.
- Implémenter différentes fonctionnalités pour récupérer des factures en fonction de différents critères tels que l'année, la date, le nom du formateur, le nom de l'école, etc.
- Tester l'API à l'aide d'outils tels que Postman ou curl.
- Créer une interface graphique avec React permettant de calculer des points importants pour le bilan pédagogique.

## Mise en place de l'environnement

Utilisez API Platform.

## Structure du projet API 

```txt
.
├── __init__.py
├── api
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── models.py
│   ├── router.py
│   └── schemas.py
└── main.py
```

## Modèle de données

Utilisez le fichier qui se trouve dans le dossier Data : [factures](./app-fastapi-rpa/db/invoices.json)

### Table `Invoice` :

- `id`: Identifiant unique de la facture (clé primaire).
- `invoice_number`: Numéro unique de la facture.
- `client`: Nom du client associé à la facture.
- `amount_ht`: Montant hors taxes de la facture.
- `hours_count`: Nombre d'heures facturées.
- `days_count`: Nombre de jours facturés.
- `trainer`: Nom du formateur.
- `trainer_shortcode`: Code du formateur.
- `payment_due`: Délai de paiement de la facture.
- `intervention_dates`: Dates d'intervention associées à la facture.

## Mise en place des données

Une fois connecté à la base de données `db` de Postgres, créez les données en exécutant le script suivant :

```sql
\c db

CREATE TABLE invoices (
    id SERIAL PRIMARY KEY,
    invoice_number VARCHAR(10) NOT NULL,
    client VARCHAR(100) NOT NULL,
    amount_ht DECIMAL(10, 2) NOT NULL,
    hours_count INTEGER NOT NULL,
    days_count INTEGER NOT NULL,
    trainer VARCHAR(100) NOT NULL,
    trainer_shortcode VARCHAR(50) NOT NULL,
    payment_due VARCHAR(50) NOT NULL,
    intervention_dates JSONB
) ;

-- Création des écoles
CREATE TABLE schools (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

INSERT INTO schools (name) VALUES 
('Computer School'),
('ESIT'),
('EIT'),
('The Bridge');

-- Création des formateurs
CREATE TABLE trainers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    shortcode VARCHAR(50) NOT NULL
);

INSERT INTO trainers (name, shortcode) VALUES 
('Lucie Bouvier', 'LB01'),
('Margot Caron', 'MC01'),
('Théophile Sauvage', 'TS01'),
('Susan Fernandes', 'SF01'),
('Danielle Chevallier', 'DC01'),
('Martine Roger', 'MR01'),
('Clémence Auger', 'CA01'),
('Franck Riou', 'FR01'),
('Joséphine Joseph', 'JJ01'),
('Claude Garcia', 'CG01');

-- Génération des factures
INSERT INTO invoices (
    invoice_number, client, amount_ht, hours_count, days_count, 
    trainer, trainer_shortcode, payment_due, intervention_dates
)
SELECT 
    '0000' || i AS invoice_number,
    CASE 
        WHEN i % 4 = 0 THEN 'Computer School'
        WHEN i % 4 = 1 THEN 'ESIT'
        WHEN i % 4 = 2 THEN 'EIT'
        WHEN i % 4 = 3 THEN 'The Bridge'
    END AS client,
    ROUND((RANDOM() * 2000 + 500)::numeric, 2) AS amount_ht,  -- Corrected rounding syntax
    ROUND(RANDOM() * 80 + 10)::integer AS hours_count,  -- Ensure integer type
    ROUND(5)::integer AS days_count,  -- Ensure integer type
    (
        SELECT name FROM trainers ORDER BY RANDOM() LIMIT 1
    ) AS trainer,
    (
        SELECT shortcode FROM trainers ORDER BY RANDOM() LIMIT 1
    ) AS trainer_shortcode,
    'Payment due: ' || (ROUND(RANDOM() * 60 + 15))::integer || ' days' AS payment_due,  -- Ensure integer type
       jsonb_build_object(
        'start_date', to_char(
            DATE '2023-01-01' + ((i - 1) / 10 * INTERVAL '1 MONTH') + ((i - 1) % 10 * 3 || ' days')::INTERVAL, 
            'YYYY-MM-DD'
        ),
        'end_date', to_char(
            DATE '2023-01-01' + ((i - 1) / 10 * INTERVAL '1 MONTH') + ((i - 1) % 10 * 3 || ' days')::INTERVAL + INTERVAL '5 days', 
            'YYYY-MM-DD'
        )
    ) AS intervention_dates
FROM generate_series(1, 120) AS s(i);
```

## Implémentation des endpoints

Implémentez les endpoints suivants pour récupérer les factures :

1. `GET /api/invoices` : Récupère toutes les factures.
2. `GET /api/invoices/year/<annee>` : Récupère les factures pour une année spécifiée.
3. `GET /api/invoices/date/<date>` : Récupère les factures pour une date spécifiée.
4. `GET /api/trainers` : Récupère tous les noms des formateurs.
5. `GET /api/invoices/trainer/<nom_formateur>` : Récupère les factures parformateur spécifié.
6. `GET /api/invoices/school/<nom_ecole>` : Récupère les factures pour une école spécifiée.
7. `GET /api/invoices/date/<date>/trainer/<name_trainer>` : Récupère les factures pour une date et un formateur spécifiés.
8. `GET /factures/date/<date>/school/<name_school>` : Récupère les factures pour une date et une école spécifiées.
9. `GET /factures/date/<date>/trainer/<name_trainer>/school/<name_school>` : Récupère les factures pour une date, un formateur et une école spécifiés.

🚀 Pour les requêtes très spécifiques sur les champs JSON, vous pouvez utiliser la syntaxe suivante :

```python
def get_all_intervention_by_start_date(db: Session, start : str ):
    
    sql_query = """
        SELECT *
        FROM invoices
        WHERE intervention_dates->>'start_date' = :start_date
    """
    # Exécuter la requête SQL avec les paramètres
    result = db.execute(text(sql_query), {"start_date": start})
    # Récupérer les résultats
    invoices = result.fetchall()
    
    return invoices
```

## Documentation

- Créez une documentation décrivant chaque endpoint, les paramètres acceptés et les réponses attendues.

## Livrables

- Code source de l'API.
- Documentation de l'API.
- Rapport décrivant les étapes de développement, les problèmes rencontrés et les solutions adoptées.
- Création d'une interface utilisateur pour gérer le bilan pédagogique et financier.

## Partie 2 UI

- Développement de l'Interface Utilisateur avec React RPA - BPF

## Objectifs

- Développer une application React qui consomme l'API de gestion des factures.
- Lister toutes les factures dans l'application.
- Implémenter des fonctionnalités permettant de calculer automatiquement le bilan pédagogique et financier (BPF) :
  - Récupérer l'ensemble des jours de formation.
  - Compter le nombre d'étudiants.
  - Compter le nombre de formateurs.
  - Récupérer les noms des formateurs et le nombre d'heures travaillées par chacun.
  - Récupérer toutes les matières travaillées.
  - Faire un document précis pour expliquer comment utiliser l'application.

## Prérequis

- Node.js et npm installés.
- Connaissance de base en React et en consommation d'API RESTful.

## 1. Création de l'application React

1. Ouvrez votre terminal et créez une nouvelle application React en utilisant `vite.js` :

2. Installez Axios pour faciliter les appels API :

   ```bash
   npm install axios
   ```

## 2. Structure du projet

Organisez votre projet de manière cohérente. Voici une structure suggérée à voir avec vite.js

## 3. Création du service API

Dans le dossier `services` ou `store` avec Reduxtoolkit, créez un fichier `api.js` pour gérer les appels API :

```javascript
import axios from 'axios';

const API_URL = 'http://localhost:8002/api'; // Remplacez par l'URL de votre API

export const getInvoices = () => {
    return axios.get(`${API_URL}/invoices`);
};

export const getInvoicesByYear = (year) => {
    return axios.get(`${API_URL}/invoices/year/${year}`);
};

// Ajoutez d'autres fonctions pour les différents endpoints si nécessaire
```

## Livrables

- Code source de l'application React (Github) 
- Documentation de l'application.
- Rapport décrivant les étapes de développement, les problèmes rencontrés et les solutions adoptées.
