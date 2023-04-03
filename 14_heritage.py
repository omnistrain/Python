"""
BASE DE l'héritage
"""


# Creation de la class mere qui hérite par défaut de objet
class Personnage:
    # on determine le constructeur par defaut
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.personnage = "personnage"

    @property
    def nomComplet(self):
        """NomComplet"""
        return f"{self.nom} {self.prenom}"

    @nomComplet.setter
    def nomComplet(self, nomComplet):
        self.nom, self.prenom = nomComplet.split(maxsplit=1)

    @nomComplet.deleter
    def nomComplet(self):
        self.nom = self.prenom = ""

    # une methode
    def sayHello(self):
        print("hello %s %s" % (self.nom, self.prenom))

    # un getter sur un attribut

    def get_personnage(self):
        return self.personnage


class Autre(object):
    pass


# implementation de la class enfant
"""
Class Orc qui herite de Personnage
"""


class Orc(Personnage, Autre):
    # definition du constructeur
    def __init__(self, nom, prenom):
        # on appel le constructeur parent pour ne pas avoir à refaire le travail
        # on veille a BIEN PASSER SELF
        Personnage.__init__(self, nom, prenom)
        # super().__init__(selft, nom, prenom)

        # on peut jouer avec les attributs existants
        self.personnage = "orc"

    def sayHello(self):
        super().sayHello(self)
        print("Ragnaraaaakk")


class Guerrier(Personnage, Autre):
    # definition du constructeur
    def __init__(self, nom, prenom):
        # on appel le constructeur parent pour ne pas avoir à refaire le travail
        # on veille a BIEN PASSER SELF
        Personnage.__init__(self, nom, prenom)
        # super().__init__(selft, nom, prenom)

        # on peut jouer avec les attributs existants
        self.personnage = "guerrier"

    def sayHello(self):
        super().sayHello(self)
        print("ahhhh")


# INITIALISATION
listePersonnage = [Orc("Tulok", "Marak"), Guerrier("truc", "machin")]


class Vehicule:
    def __init__(self):
        self.vitesse = 100


class Motorise(Vehicule):
    def accelerer(self):
        self.vitesse += 1

    def machin(self):
        print("action particuliere")


class Autre(Vehicule):
    def truc(self):
        self.vitesse -= 1

    def machin(self):
        print("autre action action particuliere")


class Moto(Motorise, Autre):
    pass
