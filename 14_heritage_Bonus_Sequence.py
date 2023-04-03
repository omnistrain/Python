"""Classe garage."""


from collections.abc import Sequence


class Voiture(object):
    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleur = couleur

    def afficher(self):
        print("%s %s" % (self.nom, self.couleur))


class Garage(Sequence):
    """Classe iterable."""

    def __init__(self, *voitures):
        """Constructeur."""
        for v in voitures:
            if isinstance(v, Voiture):
                pass
            else:
                raise TypeError(f"{v!r} n'est pas une voiture.")

        self.voitures = voitures

    def __getitem__(self, index):
        """Trouve la voiture à l'index 'index'."""
        return self.voitures[index]

    def __len__(self):
        """Retourne le nombre de voitures."""
        return len(self.voitures)

    def afficher(self):
        """Affiche toutes les voitures du garage."""
        for v in self.voitures:
            v.afficher()


v1 = Voiture("BMW", "Noir")
v2 = Voiture("Subaru", "Bleu")
v3 = Voiture("Dacia", "Rouge")

# On place les voitures dans un garage.
g = Garage(v1, v2, v3)

# On affiche le garage (toutes les voitures qu'il contient)
g.afficher()
