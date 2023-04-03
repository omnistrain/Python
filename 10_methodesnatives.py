"""
base

les builtins


On peut importer un ensemble de bibliotheques en python
les builtins sont déjà présent

pour voir l'ensemble des possibilités disponibles : print(help(builtins))
"""
import random

# quelques exemples

print(abs(-1))
print(random.choice([1, 2, 3, 4, 5]))
print("chaine".count("a"))

print(round(2.4))
print(sorted((2, 4, 5, 10, 9)))

print("allo".find("l"))
print("1".isalpha())
print("allo".endswith("o"))

print("HELLO".isupper())
print("HELLO".islower())
print("HELLO".lower())

exe = "Ajouter une chaine à une chaine".__add__("nouvelle")
# fonction avec join() aussi
# on a vu le pendant avec split

autre = "hello".replace("ll", "xx")

print(autre)

# une majuscule par mot
print("hello, the world".title())
