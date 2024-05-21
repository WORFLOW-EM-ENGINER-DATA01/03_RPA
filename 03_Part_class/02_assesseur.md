# Utilisation de la Décoration `@property` pour un Getter

Le décorateur `@property` est utilisé pour définir une méthode comme un getter. 
Cette méthode peut être appelée comme un attribut, sans utiliser de parenthèses. Voici un exemple :

```python
class Person:
    def __init__(self, name):
        self._name = name  # Private attribute with underscore prefix

    # Getter for the name attribute
    @property
    def name(self):
        return self._name

# Creating a Person object
person = Person("Alice")

# Using the getter to access the name attribute
print(person.name)  # Outputs "Alice"

```

Dans cet exemple, `@property` est utilisé pour définir la méthode `name()` comme un getter. Ainsi, la méthode `name` peut être appelée comme un attribut, sans utiliser de parenthèses.

## Utilisation de la Décoration `@name.setter` pour un Setter

Le décorateur `@name.setter` est utilisé pour définir une méthode comme un setter. Cette méthode est appelée lorsque la propriété est assignée une nouvelle valeur. Voici un exemple :

```python
class Person:
    def __init__(self, name):
        self._name = name  # Private attribute with underscore prefix

    # Getter for the name attribute
    @property
    def name(self):
        return self._name

    # Setter for the name attribute
    @name.setter
    def name(self, new_name):
        self._name = new_name.upper()  # Convert the name to uppercase

# Creating a Person object
person = Person("Alice")

# Using the setter to modify the value of the name attribute
person.name = "Bob"

# Using the getter to access the new value of the name attribute
print(person.name)  # Outputs "BOB"
```

Dans cet exemple, `@name.setter` est utilisé pour définir la méthode `name()` comme un setter. Cette méthode est appelée lorsque la propriété `name` est assignée une nouvelle valeur.
