# Set (Listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index

# set1 = {"a", "b", "c"}
# set2 = {"a", "d", "e"}
# set3 = {"c", "d", "f"}

# # set4 = set1.union(set2)
# # set4 = set1.difference(set3)
# # set4 = set1.intersection(set2)
# set4 = set1.symmetric_difference(set3)

# print(set4)


###############################################################################

amigos1 = {"Goku", "Vegeta", "Bulma", "Ulon", "Kame"}
amigos2 = {"Yancha", "Kame", "Kuririn", "Vegeta", "Numero18"}

result = amigos1.intersection(amigos2)
# result = amigos1.union(amigos2)
# result = amigos1.difference(amigos2)
print(result)