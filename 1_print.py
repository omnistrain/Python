# opérations simples
print("Hello")
print("Hello")
print("Hello \n")
print("Hello \n plus long\n")
print("\tHello" + " plus long \n")


# Avec des opérations et des variables
print("La somme de 1+2 : ", 1 + 2)
somme = 1 + 2
print("La somme de 1+2 : ", somme)

# Utiliser des parametres
print("hello", "the", "world", sep="_espace_", end="END")
# + et , même chose (, rajoute un espace et ne necessite pas de cast)
print("\nhello" + "the" + "world", sep="_espace_", end="END")

# Format
print("\n{0} {1} {2}".format("hello", "the", "world"))
# Format avancé
print("\n%s %f %.3f %d" % ("Hello the world", 4.3, 4.12345, 10))

une_variable = 1
print("\nLe type de ma variable ", type(une_variable))

une_variable_2 = "Hello, the world"
print("\n" + une_variable_2[0], une_variable_2[1])
print("\n" + une_variable_2[0:5])
print("\n" + une_variable_2[-3])
