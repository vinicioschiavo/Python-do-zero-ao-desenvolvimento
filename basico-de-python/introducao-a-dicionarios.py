#Dicionários
    # Utiliza index no formato de Keys e Values
    # Aceita string, integer, float, boolean...

# #          key    value
# aluno = {"nome": "Bulma", "idade": 16, "nota_final": "A", "aprovação": True}

# # print(aluno)
# print(aluno["nome"]) # se por acaso quiser buscar só o nome da aluna.


###########################################################################

capitais = {
    "Brasil": "Brasília",
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Australia": "Camberra",
    "Canada": "Ottawa"
}

pais_usuario = input("Digite o nome do país: ")

if pais_usuario in capitais:
    print(f"A capital de {pais_usuario} é {capitais[pais_usuario]}")
else:
    print(f"Não temos informações sobre a capital desse país.")