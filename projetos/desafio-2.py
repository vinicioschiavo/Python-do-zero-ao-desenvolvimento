# Desafio com Funções

'''
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede.
O usuário deverá fornecer as seguintes informações: Rendimento, Altura e Largura.
O programa deve mostrar na tela a mensagem "Você necessita de x latas de tinta".
'''

rendimento = int(input("Qual é o rendimento da lata ? "))
altura = int(input("Qual é a altura da parece ? "))
largura = int(input("Qual é a largura da parede ? "))

def calculo_tinta():
    area = altura * largura
    total = area / rendimento
    print(f"Você precisa de {total} latas de tinta")

calculo_tinta()