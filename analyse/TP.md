# TP : Gestion de données CSV avec une API Express et une interface React

### Objectif du TP

L'objectif de ce TP est de créer une application qui permet de gérer des données dans un fichier CSV à l'aide d'une API développée en Express et d'une interface utilisateur construite avec React.

Il faut générer le meilleur bénéfice pour un investissement donné.

Utilisez la méthode greedy, ou approche gloutonne, c'est une stratégie algorithmique utilisée pour résoudre des problèmes d'optimisation. 

1. Nettoyez les données et les normalisez, pensez à caster les valeurs si nécessaire.
2. Fixez un montant d'investissement et trouvez le meilleur placement.

### Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- **Node.js**
- **Docker** 
- **Docker Compose** 

### Structure du projet

Organisez votre projet comme suit :

```
/action
│
├── /Data
│   └── analyse.csv
│
├── /api
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── server.js
│   └── package.json
│
└── /app-rpa
    └── src
        ├── App.js
        ├── index.js
        └── ... 
```

### Étapes d'installation

1. **Créer le fichier CSV**  
   Créez un fichier `analyse.csv` dans le dossier `/Data` avec quelques lignes d'exemple pour commencer.

2. **Créer l'API en Express**  
   - Créez un nouveau dossier `/api`.
   - Dans ce dossier, créez un fichier `package.json` pour définir les dépendances.
   - Créez un fichier `main.js` pour configurer l'API qui lira et écrira dans le fichier CSV.
   - Écrivez un `Dockerfile` pour votre API afin qu'elle soit facilement déployable avec Docker.
   - Créez un fichier `docker-compose.yml` pour orchestrer votre application.

3. **Créer l'interface utilisateur en React**  
   - Créez un dossier `/app-rpa`.
   - Initialisez un projet React à l'intérieur de ce dossier.
   - Configurez un `Dockerfile` pour votre application React.
   - Créez un fichier `docker-compose.yml` pour le frontend.

4. **Développer l'interface utilisateur**  
   - Dans le dossier `src`, créez le fichier `App.js` pour gérer l'affichage des données et la soumission de nouvelles entrées.

### Exécution du projet

1. **Démarrer l'API**  
   Ouvrez un terminal, naviguez vers le dossier `/api`, et exécutez la commande pour construire et démarrer l'API.

2. **Démarrer l'interface utilisateur**  
   Ouvrez un autre terminal, naviguez vers le dossier `/app-rpa`, et exécutez la commande pour construire et démarrer l'interface utilisateur.

3. **Accéder à l'application**  
   Ouvrez votre navigateur et accédez à `http://localhost:3000` pour interagir avec votre application.

### Remarques

- Assurez-vous que vos chemins de fichiers dans le code pointent correctement vers le fichier `analyse.csv`.
- Les données ajoutées via l'interface devraient être sauvegardées dans le fichier CSV.
- En cas de modifications de code, utilisez les commandes Docker appropriées pour reconstruire vos conteneurs.

