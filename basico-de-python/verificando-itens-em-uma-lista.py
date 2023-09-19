# Listas
    #  Armazenar mais de uma informação em variáveis
    #  Manter a sequencia dos dados em uma variável

cor_cliente = input("digite a cor desejada: ")
cores = ["amarelo", "verde", "azul", "branco"]

if cor_cliente.lower() in cores:
    print("Em estoque")
else:
    print("Não temos esta cor em estoque")