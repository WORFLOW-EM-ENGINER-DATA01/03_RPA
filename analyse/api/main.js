import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import fs from 'fs/promises'; // Assurez-vous d'utiliser 'fs/promises' pour éviter les callbacks
import path from 'path';
import { fileURLToPath } from 'url';  // Pour gérer les chemins dans les modules ES
import csvtojson from 'csvtojson'
const app = express();
const PORT = 5000;

// Configurer CORS pour accepter les requêtes de votre application React
app.use(cors({
    origin: 'http://localhost:5173',
    methods: ['GET', 'POST'],
    credentials: true
}));

app.use(bodyParser.json());

// Résoudre __dirname pour les modules ES
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Définir le chemin vers le fichier CSV
const csvFilePath = path.join(__dirname, '../Data/analyse.csv')

app.get('/api/show', async (req, res) => {
    try {
        const filePath = '../Data/analyse.csv'
        const jsonArray = await csvtojson().fromFile(filePath);
        res.status(200).json(jsonArray);
    } catch (err) {
        console.error(err);
        res.status(500).send('Erreur lors de la lecture du fichier');
    }
});

// Endpoint pour enregistrer les données dans le fichier CSV
app.post('/api/save', async (req, res) => {
    const data = req.body;

    // Créer une ligne CSV avec un retour à la ligne
    const csvLine = `\n${data.name},${data.price},${data.profit}`;

    try {
        // Ajouter la nouvelle ligne au fichier CSV
        await fs.appendFile(csvFilePath, csvLine);  // Méthode asynchrone avec promesse
        console.log('Les données ont été enregistrées dans analyse.csv');
        res.status(200).send('Données enregistrées avec succès');
    } catch (err) {
        console.error('Erreur lors de l\'enregistrement des données', err);
        res.status(500).send('Erreur lors de l\'enregistrement des données');
    }
});

// Démarrer le serveur
app.listen(PORT, () => {
    console.log(`Serveur en cours d'exécution sur http://localhost:${PORT}`);
});
