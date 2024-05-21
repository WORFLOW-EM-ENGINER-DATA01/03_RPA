# Les objets

Les objets en Python sont des éléments essentiels de la programmation orientée objet (POO). 

Ils permettent d'organiser et de structurer le code de manière efficace en regroupant des données et des fonctionnalités connexes dans des entités autonomes appelées objets.

## Création d'une Classe

Une classe est un modèle ou un plan à partir duquel des objets sont créés. Elle définit les attributs (variables) et les méthodes (fonctions) que les objets de cette classe possèderont. Voici comment créer une classe simple en Python :

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_details(self):
        print(f"Make: {self.make}, Model: {self.model}")
```

### Création d'Objets

Une fois qu'une classe est définie, des objets peuvent être créés à partir de celle-ci. 

Chaque objet est une instance de la classe à partir de laquelle il a été créé. Voici comment créer des objets à partir de la classe `Car` :

```python
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")
```

### Accès aux Attributs et Méthodes

Les attributs et les méthodes d'un objet peuvent être accédés à l'aide de la notation pointée (`.`). Voici comment accéder aux attributs et appeler les méthodes des objets `voiture1` et `voiture2` :

```python
# Accessing attributes
print(car1.make)  # Displays "Toyota"
print(car2.model)  # Displays "Accord"

# Calling methods
car1.display_details()  # Displays "Make: Toyota, Model: Camry"
car2.display_details()  # Displays "Make: Honda, Model: Accord"
```
