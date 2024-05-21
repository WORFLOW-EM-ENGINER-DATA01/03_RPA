# Introduction aux Fonctions en Python

Les fonctions sont un concept fondamental en programmation, et Python ne fait pas exception. 

🚀 Elles permettent de structurer votre code, de le rendre plus lisible, réutilisable et modulaire. 

## 1. Définition d'une Fonction

En Python, une fonction est définie à l'aide du mot-clé `def`, suivi du nom de la fonction et d'un ensemble de parenthèses qui peuvent contenir des paramètres. Le corps de la fonction est ensuite écrit en utilisant une indentation.

```python
def greet():
    print("Hello, World!")
```

Cette fonction `greet` n'a pas de paramètres et affiche simplement "Hello, World!" lorsqu'elle est appelée.

Pour appeler une fonction, il suffit d'utiliser son nom suivi de parenthèses.

```python
greet()  # Outputs: Hello, World!
```

## 2. Fonctions avec Paramètres

Les fonctions peuvent accepter des paramètres pour recevoir des données en entrée et effectuer des opérations sur ces données.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Outputs: Hello, Alice!
```

Ici, la fonction `greet` prend un paramètre `name` et l'utilise dans la chaîne de caractères à afficher.

## 3. Valeurs de Retour

Les fonctions peuvent également renvoyer des valeurs à l'aide de l'instruction `return`.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Outputs: 8
```

La fonction `add` prend deux paramètres `a` et `b`, les additionne et renvoie le résultat.

## 4. Paramètres par Défaut

Vous pouvez définir des valeurs par défaut pour les paramètres, ce qui permet de les rendre optionnels lors de l'appel de la fonction.

```python
def greet(name="World"):
    print(f"Hello, {name}!")

greet()         # Outputs: Hello, World!
greet("Alice")  # Outputs: Hello, Alice!
```

Ici, si aucun argument n'est fourni, `name` prend la valeur par défaut "World".

## 5. Fonctions avec un Nombre Variable de Paramètres

Il est possible de définir des fonctions qui acceptent un nombre variable de paramètres en utilisant `*args` pour les arguments positionnels et `**kwargs` pour les arguments nommés.

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))  # Outputs: 6

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30)
# Outputs:
# name: Alice
# age: 30
```

## 6. Portée des Variables

Les variables définies à l'intérieur d'une fonction sont locales à cette fonction et ne sont pas accessibles en dehors de celle-ci.

```python
def greet():
    message = "Hello"
    print(message)

greet()         # Outputs: Hello
# print(message)  # Raises NameError: name 'message' is not defined
```

## 7. Fonctions Lambda

Les fonctions lambda sont des fonctions anonymes définies en une seule ligne. Elles sont utiles pour des opérations simples.

```python
add = lambda a, b: a + b
print(add(3, 5))  # Outputs: 8

# Utilisation dans une fonction comme map
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Outputs: [1, 4, 9, 16, 25]
```

## 8. Documentation des Fonctions

Il est important de documenter vos fonctions pour expliquer ce qu'elles font, leurs paramètres et leurs valeurs de retour. Vous pouvez utiliser des docstrings pour cela.

```python
def add(a, b):
    """
    Adds two numbers together.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b

print(add(3, 5))  # Outputs: 8
print(add.__doc__)
```
