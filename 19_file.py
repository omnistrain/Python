"""
base
"""
import csv

# j'importe ici des modules qui vont m'être utile pour acceder au systeme de fichier
import os
import os.path

#### Gestion basique

# je me position sur un dossier
os.chdir(".")
# permet de voir le le chemin de rep de travail
print(os.getcwd())


##### Ouverture de fichier en ecriture (ajoute si il n'existe pas)
file = open("exercices.txt", "w")
# j'ajoute une ligne
file.write("#ajoute un commentaire")
# je referme mon fichier
file.close()

with open("", mode="w") as file:
    file.write("ddd")
    pass


####Lecture du fichier

file = open("exercices.txt", "r")
texte = file.read()
# file.readlines() retourne sous forme de liste de ligne
print(texte)
file.close()


# poid d'un fichier
# os.path.getsize(fichier)


# Mode : w, r, x, +, a, b, t


# exercice creer un editeur simple de texte
# afficher le nombre de mots dans un fichier
# connaitre le nombre de caracteres et de ligne


# recherche de fichier
import glob

ensemble = glob.glob("*.py")
ensembleRecursif = glob.glob("**/*.py", recursive="True")

print(ensemble)


# fichier CSV
# en lecture une ligne du CV génère un tableau
import csv

with open("fichier.csv") as fichier:
    lec = csv.reader(fichier)
    for lig in lec:
        print(lig)
