"""
base
"""

# declaration
dico = {}
dico2 = {"clef": "valeur", "clef2": "valeur"}
dico3 = dict(zip(["clef", "clef2"], ["valeur", "valeur"]))
dico4 = dict({"clef": "valeur", "clef2": "valeur"})


# creation clef - valeur
dico["prenom"] = ("fred", "karl")
dico["nom"] = ("Heb", "marcel")
dico["taille"] = (180, 130, 110)

# acceder à un élément

print(dico["prenom"])
print(dico2["clef2"])
print(dico3["clef2"])
print(dico4["clef2"])


# création complexe
x1, y2 = 10, 100
coor = {}

coor[(x1, y2)] = "maison"

print(coor.keys(), coor.values())


# acceder à une valeur de clef
print(dico["prenom"])
print(dico.get("prenom"))

# modification possible
dico["prenom"] = "autre"

# effacer une clef
del dico["prenom"]

# effacer en recup la valeur
value = dico.pop("prenom")

# longueur
len(dico3)


# liste des clefs
dico4.keys()
# liste des value
dico4.values()


# iteration sur les dico

for clef in dico4.keys():
    print(clef)

for valeur in dico4.values():
    print(valeur)

for clef, valeur in dico4.items():
    print(clef, valeur)
