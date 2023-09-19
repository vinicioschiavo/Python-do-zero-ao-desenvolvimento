# Tuples
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável
    # Não pode ser alteradas (Immutable)

# cores_list = ["amarelo", "verde", "azul", "braco"]
# cores_tuple = ("amarelo", "verde", "azul", "braco")

# print(type(cores_list))
# print(type(cores_tuple))

# duas_listas = cores_tuple * 2
# print(duas_listas)

#  Para obter resultados melhores em uma lista que não vai ser mudada usar TUPLES de preferencia.

##############################################################################

cidades = ("São Paulo", "Jundiaí", "Itu")
cidades_usuario = input("Adivinha o nome da cidade: ")

if cidades_usuario in cidades:
    print("A cidade está na lista de cidades")
else:
    print("A cidade não está na lista de cidades") 

# como a lista é uma tuple não pode ser mudada.