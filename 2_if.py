"""
Les bases
"""

# Input permet la saisie utilisateur et le résulat est une chaine de caracteres.
insertion = input("indiquez une valeur => ")
# Pour l'utiliser autrement que comme un string il faut le caster
valeur = int(insertion)


# L'indentation en python est une fonctionnalité
if valeur < 0:
    print("La valeur est plus petite que Zero\n")


if valeur < 0 or valeur > 10:
    print("il n'est pas dans la borne 0 - 10\n")

if (valeur < 5) and (valeur > 3):
    print("le nombre est inferieur a 5 et supérieur à 3")

if valeur != 0:
    print("ce n'est pas 0\n")

if valeur == 8:
    print("la valeur vaut 8")


# les comparateurs : == < > <= >= !=      and et or


################################################
# EXO : Chiffre mystère
################################################


"""
if / elseif / else
"""

# else
if valeur < 0:
    print("plus petit que zero")
else:
    print("plus grand que zero")


# elseif
if valeur == 0:
    print("c'est zero")
elif valeur == 1:
    print("c'est 1")
else:
    print("c'est autre chose")

# Ternaire

a = 1 if 1 <= 1 else 0
