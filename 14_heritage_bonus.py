"""

BONUS : class abstraite en python
utilisation des methodes abstraites

"""


import abc


class Shape(metaclass=abc.ABCMeta):
    """Shape est une classe abstraite."""

    # Méthode abstraite car les formes ont différentes manière de calculer leur aire.
    @abc.abstractmethod
    def calculateArea(self):
        pass

    def element(self):
        print("ddd")


class Rectangle(Shape):
    """Rectangle hérite de Shape."""

    def __init__(self, hauteur, largeur):
        """Initialisation des attributs."""
        self.hauteur = hauteur
        self.largeur = largeur

    def calculateArea(self):
        """Calcul l'aire d'un rectangle."""
        return self.hauteur * self.largeur


class Triangle(Shape):
    """Triangle hérite de Shape."""

    def __init__(self, hauteur, base):
        """Initialisation des attributs."""
        self.hauteur = hauteur
        self.base = base

    def calculateArea(self):
        """Calcul l'aire d'un triangle."""
        return self.hauteur * self.base / 2


shape = Triangle(5, 10)
shape.element()
