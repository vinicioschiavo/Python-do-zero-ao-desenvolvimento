# Desafio com 'Sets'

'''
Criar um programa que gere 3 listas de acordo com a necessidade logo abaixo:

Lista1 = Funcionários que podem voar e trabalham a noite
Lista2 = Funcionários que pode voar e trabalham durante o dia
Lista3 = Funcionários que não podem voar
'''

funcionarios = ["Bulma", "Goku", "Tchitchi", "Vegeta", "Androide18", "Kame", "Videl"]
turno_dia = ["Bulma", "Goku", "Tchitchi", "Videl"]
turno_noite = ["Vegeta", "Androide18", "Kame"]
pode_voar = ["Goku", "Vegeta", "Androide18", "Videl"]

# Lista 1
lista1 = set(pode_voar).intersection(turno_noite)
print(lista1)

# Lista 2
lista2 = set(pode_voar).intersection(turno_dia)
print(lista2)

# Lista 3
lista3 = set(funcionarios).difference(pode_voar)
print(lista3)