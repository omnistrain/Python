"""
base

les exceptions en python : https://docs.python.org/fr/3/library/exceptions.html

exemple avec la division / 0
exemple avec le depassement de liste
avec un dico mal construit sans valeur
3+"3"
"""


# lever les exceptions
def une_fonction(parametre):
    if parametre not in (1, 2, 3):
        # permet de lever une exception
        raise ValueError("parametre n'est pas dans la liste")


# le bloc try except permet de gerer les exceptions
try:
    une_fonction(6)
# je leve ici c'est une exeption par valueError ou ZeroDevisionError
except (ValueError, ZeroDivisionError):
    print("ca ne fonctionne pas")
except Exception:
    print("si c'est un type exception lambda")
# j'execute ceci si ca se passe bien
else:
    print("j'execute ceci si il n'y a pas d'exception")
# quoi qu'il advienne j'execute ceci
finally:
    print("j'execute toujours ceci peut importe si il y a une exception ou non")
