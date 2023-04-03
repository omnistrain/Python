"""
BASE


1 fichier par class
"""


# Definition d'une classe simple
class UneClass(object):
    # Constructeur
    def __init__(self, attr):
        # methode par defaut
        print("Creation")

    # Une methode
    def fonction(self, attr):
        # une fonction
        print("une fonction")


# que faire si le fichier et le fichier principal du programme
if __name__ == "__main__":
    # initialiser un nouvel objet
    obj = UneClass("attr")
    # appeler une methode à un objet
    obj.fonction("attr")
