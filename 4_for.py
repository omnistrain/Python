"""
Les bases
"""


# simple range
for increment in range(10):  # de 0 à 9
    print("c'est %d" % (increment))

# range complexe
for increment in range(10, 20, 2):  # de 10 à 20 avec un pas de 2
    print("c'est %d" % (increment))


# avec une chaine
for lettre in "exemple":  # lettre à lettre
    print("c'est %s" % (lettre))

# avec une liste
for champ in ["python", "java"]:  # dans une liste, enumeration de champ
    print("c'est %s" % (champ))

# Exercice : donner une phrase, demander une lettre, iterer sur la phrase lettre a lettre si la lettre est egale a la lettre choisi
# le programme remplace par X dans l'affichage help : (for lettre in "l":)

# Exercice : table de multiplication avec un for
# Exercice : ecrire une factorielle en iteratif


# creer un programme qui s'execute sur le systeme directement.
# import os / os.system("pause")
