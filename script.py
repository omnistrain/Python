# _*_ coding:Utf8 _*_


"""

Nom : Premier script en python
Nom du projet : ${PROJECT_NAME}
fichier : ${NAME}

Date de la dernière révision : ${MOUTH_NAME_FULL}, ${YEAR},${MONTH},${DAY},${TIME}

AUTEUR : Freddy    #le choix
Auteurs : ${USER}  #le choix

Rev : v1.0

IDE : ${PRODUCT_NAME}



"""
import Compte

####################
# PROGRAMME PRINCIPAL
####################

# -------------------
# Import des modules
# -------------------


# -------------------
# Declaration des var
# -------------------

# -----------------------------------
# Declaration des modules / functions
# -----------------------------------

# -----------------------------------
# PROGRAMME
# -----------------------------------


class Personnage(object):
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def getter_nom(self):
        return self.nom

    def setter_nom(self, nom):
        self.nom = nom

    def sayHello(self):
        print(f"bonjour {self.nom} {self.prenom}")

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    def __repr__(self):
        return f"objet = Personnage(nom='{self.nom}',prenom='{self.prenom}')"

    def __add__(self, attr):
        self.nom += attr
