# Dicionário
    #  Utiliza index no formato de Keys e Values
    #  Aceita string, integer, float, boolean...

aluno = {"nome": "Bulma",
          "idade": 16,
          "nota_final": "A",
          "aprovação": True,
          "Materias": ["Fisica", "Matematica", "Ingles"]
}

# print(aluno)
# print(aluno.get("Materias"))
# print(len(aluno))

print(aluno.items())
print(aluno.keys())
print(aluno.values())