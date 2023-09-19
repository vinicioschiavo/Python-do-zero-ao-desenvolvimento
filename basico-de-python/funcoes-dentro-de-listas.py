# Listas
    # Armazenar mais de uma informação em variáveis 
    # Manter a sequencia dos dados em uma variável

cidade1 = "São Paulo"
cidade2 = "Jundiaí"
cidade3 = "Eloyork"

cidades = ["São Paulo", "Jundiaí", "Eloyork", "Campinas"]
#               0           1          2           3

cidades.append("Itupeva")
cidades.remove("São Paulo")
cidades.insert(0, "Itu")
cidades.pop(1)
cidades.sort()
del cidades[-1] # remove sempre o ultimo item da lista.

print(cidades)

###############################################################################


