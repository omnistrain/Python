"""
BASE
"""


# j'écrris une fonction qui prend en argument fonction
def verif(fonction):
    # on redefinit une fonction qui s'appelle wrapper on ne connait pas les arg, le nombre etc...
    def wrapper(*args, **kargs):
        # je parcours les arguments et si je n'ai pas un entier j'informe l'utilisateur avec un raise
        for valeur in args:
            if type(valeur) is not int:
                raise TypeError("l'un des params n'est pas un entier")
        # si c'est ok je retourne forcement ma fonction avec les arguments
        return fonction(*args, **kargs)

    return wrapper


# je decore avec le decorateur
@verif
def addition(a, b):
    return a + b


try:
    print(addition(1, 2))
    print(addition(1, "2"))
except TypeError:
    print("attention")
