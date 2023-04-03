"""
Base

une liste en python est modifiable
"""

list1 = ["a", "b", "b"]
list2 = [1, 2]
list3 = [1.3, 3.5]
list4 = ["a", 1.5]

print(list1)
print(list2)
print(list3)
print(list4)
print(type(list4))

# Récuperer un elem de la liste par index (commence par zero)
print(list1[0])
# partant de la fin
print(list1[-1])
# les dernieres occurance
print(list1[-3:])
# de x à y
print(list1[1:4])

# Supprimer un élément dans la liste
del list1[0]

# Supprimer par valeur
list1.remove("b")

# connaitre la taille d'une liste
len(list1)

# connaitre l'iteration d'une valeur dans une liste
print(list1.count("b"))

# connaitre l'index d'un element // renvoie uniquement le premier trouvé.
list1.index("b")

# Ajouter dans une liste
list1.append(3)
print("list1 => ", list1)


# connaitre si une valeur est dans la liste renvoie un bool
print("a" in list1)

# creer une liste à partir d'une chaine
nelle_liste = "hello, the world".split(" ")

# transformer une liste en string
retour_string = "".join(nelle_liste)


# enumerer une liste (attention donne un tuple)
for occurence in enumerate(list3):
    print(occurence)
print("\n")


# etendre une liste à une autre
list1.extend(list4)


# une liste peut contenir une autre liste
liste = [list1, list2, "autre"]

print(liste)


ma_liste = [i * 56 for i in range(30)]
