# break
for increment in range(11):
    if increment == 3:
        break
    print(increment)

# continue
for increment in range(11):
    if increment == 3:
        continue
    print(increment)

# avec un while
print("Next exemple ----------")
increment = 0
while increment < 11:
    if increment == 5:
        break
    print(increment)
    increment += 1

print("Next exemple ----------")
increment = 0
while increment < 11:
    increment += 1
    if increment == 5:
        continue
    print(increment)


# Exercice : Nombre magique avec l'utilisation de break.... si on rentre un nombre negatif on sort du programme avec un message
# "vous avez abandonné le jeu"
