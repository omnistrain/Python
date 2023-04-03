class Compte(object):
    """Exemple de class:
    Commentaire docstring
    commentaire editable grace à help
    """

    # le mot clef self permet d'indiquer : j'appartient à cette même classe et j'ai acces aux attributs
    # c'est une méthode
    def __init__(self, initial):
        self.solde = float(initial)

    def soldeDuCompte(self):
        """
        Permet de connaitre le solde du compte
        :return:
        """
        return self.solde

    def nouveauSolde(self, somme):
        self.solde = somme

    def creditDuCompte(self, somme):
        self.solde += somme
        return self.solde

    def debitDuCompte(self, somme):
        self.solde -= somme
        return self.solde

    def __add__(self, somme):
        self.solde += somme

    def __sub__(self, somme):
        self.solde -= somme

    def __str__(self):
        return "yo"

    def __repr__(self):
        return "repr"
