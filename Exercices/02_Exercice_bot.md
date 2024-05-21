# Création d'un Bot Python Simple

## Objectif :
Créer un bot Python simple qui répond à certaines commandes de l'utilisateur dans la console.

## Description de l'Exercice :
Dans cet exercice, créer un bot Python.

Le bot répondra à certaines commandes de l'utilisateur, telles que "hello" pour saluer, "roll" pour lancer un dé virtuel, et "quit" pour quitter le bot.

## Instructions :
1. Crée une classe `HellBot` avec les méthodes suivantes :
   - `__init__()`: Initialise le bot avec un dictionnaire de commandes.
   - `run()`: Lance le bot en boucle, attendant les commandes de l'utilisateur.
   - `say_hello()`: Affiche "Bonjour ! Je suis un bot." lorsque la commande "hello" est entrée.
   - `roll_dice()`: Lance un dé virtuel et affiche le résultat lorsque la commande "roll" est entrée.
   - `quit_bot()`: Arrête le bot lorsque la commande "quit" est entrée.

1. À la fin du script, ajoute un bloc `if __name__ == "__main__":` pour instancier et lancer le bot.

## Exemple d'Utilisation :
```
Bot démarré. Tapez 'quit' pour quitter.
Commande : hello
Bonjour ! Je suis un bot.
Commande : roll
Tu as lancé un dé et obtenu : 4
Commande : quit
Arrêt du bot.
```
