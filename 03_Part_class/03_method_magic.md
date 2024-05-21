### Introduction aux Méthodes Magiques en Python

Les méthodes magiques en Python, également connues sous le nom de méthodes dunder (pour "double underscore"), sont des méthodes spéciales qui commencent et se terminent par des doubles underscores. 

🚀 Elles permettent de définir comment les objets de vos classes se comportent avec les opérations Python intégrées. 

Ces méthodes ne sont généralement pas appelées directement, mais sont invoquées automatiquement en réponse à certaines opérations.

Voici un guide pratique sur certaines des méthodes magiques les plus couramment utilisées en Python.

## 1. `__init__` (Constructeur)
La méthode `__init__` est appelée lorsqu'une instance de la classe est créée. Elle initialise les attributs de l'objet.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
print(person.name)  # Outputs: Alice
print(person.age)   # Outputs: 30
```

## 1. `__str__` (Représentation en chaîne de caractères)
La méthode `__str__` est appelée par la fonction `str()` et par `print()` pour obtenir une représentation en chaîne de caractères de l'objet.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

person = Person("Alice", 30)
print(person)  # Outputs: Alice, 30 years old
```

## 1. `__repr__` (Représentation officielle)
La méthode `__repr__` est appelée par la fonction `repr()` et est souvent utilisée pour fournir une représentation détaillée et non ambiguë de l'objet, utile pour le débogage.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Alice", 30)
print(repr(person))  # Outputs: Person(name='Alice', age=30)
```

## 1. `__len__` (Longueur)
La méthode `__len__` est appelée par la fonction `len()` pour retourner la longueur ou la taille de l'objet.

```python
class Group:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

group = Group(["Alice", "Bob", "Charlie"])
print(len(group))  # Outputs: 3
```

## 1. `__eq__` (Égalité)
La méthode `__eq__` est utilisée pour comparer deux objets pour l'égalité avec l'opérateur `==`.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

person1 = Person("Alice", 30)
person2 = Person("Alice", 30)
print(person1 == person2)  # Outputs: True
```

#### 6. `__add__` (Addition)
La méthode `__add__` permet de définir le comportement de l'opérateur `+`.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

vector1 = Vector(1, 2)
vector2 = Vector(3, 4)
print(vector1 + vector2)  # Outputs: Vector(4, 6)
```

#### 7. `__getitem__` (Accès aux éléments)
La méthode `__getitem__` permet de définir le comportement de l'accès aux éléments, comme pour les listes ou les dictionnaires.

```python
class CustomList:
    def __init__(self, elements):
        self.elements = elements

    def __getitem__(self, index):
        return self.elements[index]

custom_list = CustomList([1, 2, 3, 4, 5])
print(custom_list[2])  # Outputs: 3
```
