"""
Base de la fragmentation d'un programme
"""


from Exemple import Exemple
from Compte import Compte
import os

if __name__ == "__main__":
    Exemple.sayHello()

    # Partie avec les objets

    compte = Compte(1000)
    print(compte.soldeDuCompte())
    compte.creditDuCompte(1000)
    print(compte.soldeDuCompte())

    compte + 3
    print(compte.soldeDuCompte())

    compte.soldeDuCompte(0)

    os.system("read")
