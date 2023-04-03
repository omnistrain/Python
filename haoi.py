"""
Exemple de la tour d'Hanoi
"""

tour = 1


def TowerOfHanoi(n, source, destination, auxiliary):
    global tour
    if n == 1:
        print("Déplace palet 1 depuis ", source, "vers", destination)
        return
    tour += 1
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print("Déplace palet", n, "depuis", source, "vers", destination)
    tour += 1
    TowerOfHanoi(n - 1, auxiliary, destination, source)


n = 4
TowerOfHanoi(n, "A", "B", "C")
print(tour)
