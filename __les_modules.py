"""
Base
"""


# importation
import sys, os, math, random, datetime, calendar, collections

from random import random, random


from exemple import sayHello


"""
Tout fichier peut être utilisé comme un module

ex :
un fichier helper.py :
    def add():
    def sous():
    
from helper import add, sous

##############
création d'un module executable 

utilisation de la structure if avec __main__

if __name__ == "__main__":
    pass


##############

Creer un module à partir d'un répertoire

un repertoire qui fera office de module doit contenir l'ensemble des script
et un fichier __init__.py

soit on le laisse vide et l'import se fera par from <module>.<fichier> import <def>
Soit on fait les imports dans __init__.py :
from <module>.<fichier> import <def>

et on pourra directement appeller la <def> en important juste le module.



################

On peut rendre un module repertoire executable en rajoutant un fichier __main__.py
et en utilisant la command python3 -m <module>



########
Package : arborescence

"""
