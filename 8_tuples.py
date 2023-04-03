"""
Base :

Quand on utilise des tuples ou des listes :

Listes : données sont homgènes
Tuples : données hétérogènes

le tuple est plius rapide à executer que la liste
un tuple est NON MODIFIABLE
"""

# déclaration permissive
un_tuple = ()
print(un_tuple)

# unpacking

valeur1, valeur2 = (1, 2)

tuple2 = (1, 2, 3)
tuple3 = (1, "d")
tuple4 = 5, 6, 4, "eee"
tuple5 = (5, 6, 6, "a", "python3")

print(tuple2)
print(type(tuple2))

print(tuple3)
print(type(tuple3))

print(tuple4)
print(type(tuple4))

print(tuple5)
print(type(tuple5))


# recuperation par index comme avec les listes
# on ne peut pas modifier des tuples !!!
# fonctionne apres comme les listes.
