# Listas
    #  Armazenar mais de uma informação em variáveis
    #  Manter a sequencia dos dados em uma variável

#  Criar uma Lista de frutas a partir do input fornecido pelo usuário

# frutas_usuario = input("Digite o nome das frutas separados por virgula: ")

# frutas_lista = frutas_usuario.split(", ")

# print(frutas_lista)

##############################################################

pesquisa_carro = input("Digite o carro desejado: ")
estoque = ["fusca", "monza", "opala", "deyray"]

if pesquisa_carro.lower() in estoque:
    print("O carro esta disponivel no estoque.")
else:
    print("O carro não está disponivel no estoque !")

