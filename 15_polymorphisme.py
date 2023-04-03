"""
BASE
"""


# on definit une class mere
class Mere(object):
    def __init__(self):
        pass

    def sayHello(self):
        print("je suis mere")


# on definit une classe enfant
class Enfant(Mere):
    def __init__(self):
        pass

    def sayHello(self):
        print("je suis enfant")
        # je peux appeler aussi la methode redefinit en vaillant à bien passer self
        Mere.sayHello(self)


liste = [Enfant(), Enfant(), Mere()]


# un enfant peut se comporter comme un parent
for elem in liste:
    print(f"Enfant : {isinstance(elem, Enfant)}")
    print(f"Mere : {isinstance(elem, Mere)}")
    elem.sayHello()
