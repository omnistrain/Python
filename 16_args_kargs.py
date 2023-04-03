"""
Base de l'operateur * et **
"""


def exemple(param1, param2):
    print(param1, param2)


# utilisation de *args
def exemple_suite(*args):
    if len(args) > 0:
        print(args)
    else:
        print("il n'y a pas assez d'arguments")


# utilisation de **kargs
def exemple_suite_kargs(**kargs):
    if len(kargs) > 0:
        for clef, valeur in kargs.items():
            print("%s %s" % (clef, valeur))
    else:
        print("il n'y a pas assez d'arguments")


exemple(1, 2)

# avec l'operateur * si je suis homogene dans ma liste
# avec le nombre de parametre il unpackera les valeurs
# *args
exemple(*[1, 2])

# idem avec les dictionnaires
# mais j'utilise ici ** pour indiquer que c'est un dictionnaire
# Attention : les parametres doivent avoir le meme nom que les params.
dico = {"param1": "valeur", "param2": "valeur"}
exemple(**dico)


# utilisation *args et **kargs
# ca va permettre de definir dynamiquement des parametres de fonction
exemple_suite(1, 2)
exemple_suite_kargs(exemple="dd")
