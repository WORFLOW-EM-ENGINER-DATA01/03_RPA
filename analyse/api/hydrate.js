import puppeteer from 'puppeteer';
import fs from 'fs';
import { createReadStream } from 'fs';
import csv from 'csv-parser';

// Chemin vers le fichier CSV
const csvFilePath = '../Data/analyse.csv';

// Fonction pour charger les données CSV
async function loadCSVData(filePath) {
  const results = [];
  return new Promise((resolve, reject) => {
    createReadStream(filePath)
      .pipe(csv())
      .on('data', (data) => results.push(data))
      .on('end', () => resolve(results))
      .on('error', (err) => reject(err));
  });
}

// Fonction principale pour interagir avec le formulaire
async function fillForm() {
  const browser = await puppeteer.launch({ headless: false }); // headless: false pour voir le navigateur
  const page = await browser.newPage();

  // Charger les données du fichier CSV
  const data = await loadCSVData(csvFilePath);

  // Naviguer vers votre page React
  await page.goto('http://localhost:5173');

  // Attendre que la page soit complètement chargée
  await page.waitForSelector('form');  // Assurez-vous que le formulaire est chargé

  for (let row of data) {
    // Remplir les champs avec les données du CSV
    await page.type('input[name="nom"]', row['name']);
    await page.type('input[name="price"]', row['price']);
    await page.type('input[name="profit"]', row['profit']);

    // Soumettre le formulaire
    await page.click('button[type="submit"]'); // Remplacez par le sélecteur correct pour le bouton submit

    // Attendre après chaque soumission
    await page.waitForTimeout(2000);  // Attendre 2 secondes avant de passer à la ligne suivante
  }

  // Fermer le navigateur
  await browser.close();
}

// Lancer le script
fillForm().catch(console.error);
