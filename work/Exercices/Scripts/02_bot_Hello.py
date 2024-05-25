import random

class HelloBot:
    def __init__(self):
        self.commands = {
            "hello": self.say_hello,
            "roll": self.roll_dice,
            "quit": self.quit_bot
        }
    
    def run(self):
        print("Bot démarré. Tapez 'quit' pour quitter.")
        while True:
            command = input("Commande : ").lower()
            if command in self.commands:
                self.commands[command]()
            else:
                print("Commande non reconnue. Essayez à nouveau.")

    def say_hello(self):
        print("Bonjour ! Je suis un bot.")

    def roll_dice(self):
        result = random.randint(1, 6)
        print(f"Tu as lancé un dé et obtenu : {result}")

    def quit_bot(self):
        print("Arrêt du bot.")
        exit()

# Lancement du bot
if __name__ == "__main__":
    bot = HelloBot()
    bot.run()
