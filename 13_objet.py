class Compte(object):
    """Exemple de class:
    Commentaire docstring
    commentaire editable grace à help
    """

    # le mot clef self permet d'indiquer : j'appartient à cette même classe et j'ai acces aux attributs
    # c'est une méthode
    def __init__(self, initial):
        # permet d'acceder // definir à un attribut d'instance
        self.solde = float(initial)

    """
        getter : permet de recuperer la valeur d'un attribut
        setter : permet de modifier un attribut 
    """

    # getter de l'attribut solde
    def getter_solde(self):
        return self.solde

    # setter de l'attribut solde
    def setter_solde(self, solde):
        self.solde = solde

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

    # builtins surchage d'operateur +
    def __add__(self, somme):
        self.solde += somme

    def __sub__(self, somme):
        self.solde -= somme
