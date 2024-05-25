import random

class Bot:
    def __init__(self):
        self.commands = {
            'hello' : self.say_hello,
            'roll' : self.roll_dice,
            'quit' : self.quit_bot
        }

    def run(self):
        print('Bot start')
        while True:
            command = input('Command: ').lower()
            if command in self.commands:
                self.commands[command]()
            else:
                print('la commande n\'existe pas')

    def say_hello(self):
        print('Bonjour !, Je suis un bot')

    def roll_dice(self):
        print(f"Result dice : {random.randint(1, 6)}")

    def quit_bot(self):
        print('bie')
        exit()

Bot().run()