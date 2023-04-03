"""
base
"""

# iteration simple
liste = [1, 2, 3, 4]

for x in liste:
    print(x)


# CRéation d'un iterateur
class IterInvers(object):
    # initialisation de la data et de l'index
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        print(self.index)

    # l'iteration
    def __iter__(self):
        return self

    # parcours inverse
    def __next__(self):
        if self.index == 0:
            # quand j'arrive a zero j'arrete l'iteration
            raise StopIteration
        else:
            # je decremente a chaque fois
            self.index = self.index - 1
        # je retourne la lettre
        return self.data[self.index]


monIter = IterInvers("Un exemple de programme")
for x in monIter:
    print(x)


# ecriture plus compact avec yeld pour cet iterateur
def v2(donnee):
    for index in range(0, len(donnee) - 1, 1):
        yield donnee[index]


monIter = v2("Un exemple de programme")
for x in monIter:
    print(x)
