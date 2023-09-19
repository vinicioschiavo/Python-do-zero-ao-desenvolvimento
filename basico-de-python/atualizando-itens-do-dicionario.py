#Dicionários
    # Utiliza index no formato de Keys e Values
    # Aceita string, integer, float, boolean...

#          key    value
aluno = {"nome": "Bulma", "idade": 16, "nota_final": "A", "aprovação": True}

# aluno["nome"] = "Goku" # Primeira forma de atualizar
# aluno.update({"nome": "Goku", "nota_final": "B"})  # Segunda forma de atualizar
aluno.update({"endereco": "Rua Copororação Capsula"}) # Pode ser adicionado tambem mas informações

# print(aluno.get("endereco", "Não existe"))
# print(aluno)

del aluno["idade"]
print(aluno)
