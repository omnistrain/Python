"""
BASE
"""


# definition du fonction de base
def say_hello():
    print("Hello, the world")


# appel d'une fonction dans une fonction
def fonction_dans_fonction():
    say_hello()


# appel
say_hello()
fonction_dans_fonction()

"""
Il existe une fonction avec le meme nom dans le programme
si vous en definissez 2 c'est la derniere qui prend le pas
c'est la redéfinition

une variable dans une fonction a une portée locale, elle ne pourra pas etre appele à l'exterieur.

"""


"""
Fonction avec parametre
"""


def say_hello_with_name(name):
    print(name)


say_hello_with_name("freddy")


# Exercice :
# proposer 3 programmes
# calculer l'air d'un carre
# le volume d'une sphere
# le volume d'un parallépipède
# help (il faut importer math avec l'utilisation de math.pi)

# le progamme demande les valeurs (attention au cast)
# ils doivent executable avec l'interpreteur.


"""
Fonction avec retour
"""


def say_hello_with_return():
    return "Hello, the world"


print(say_hello_with_return())


# une fonction ne retourne qu'une seule valeur, il n'a qu'un seul retour

"""
Fonction avec variable globale
"""

une_var = 0


def fonction_var_globale():
    global une_var
    une_var = 10
    return une_var


print(une_var)
print(fonction_var_globale())
print(une_var)


"""
fonction lamba
"""

bonjour = lambda a, b: a * b
print(bonjour(3, 4))


# le mot clef pass permet d'avoir une fonction vide.


# utiliser un parametre avec * permet de creer une liste de parametres
def exemple(*elements):
    for ele in elements:
        print(ele)


# utilisation de valeur par defaut pour les arguments


def autre(param=1):
    print(param)
