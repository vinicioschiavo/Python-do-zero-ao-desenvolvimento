# Desafio com If, Elif, Else

'''
Criar um programa que dependendo da temperatura (em celsius) da Carne ele retorna o ponto
de cozimento em portugues. O usuário deverá fornecer a temperatura.

Temperaturas - Cozimento
120°F ou 48°C - Rare (Selada)
130°F ou 54°C - Medium rare (Ao ponto para o mal)
140°F ou 60°C - Medium (Ao ponto)
150°F ou 65°C - Medium well (Ao ponto para o bem)
160°F ou 71°C - Well done (Bem passada)
'''

tem_cel = int(input("Qual é a temperatura da carne ?"))

if tem_cel < 48:
    print("Cozinhar a carne por mais alguns minutos")
elif tem_cel in range(48, 53):
    print("Selada")
elif tem_cel in range(54, 59):
    print("Ao ponto para o mal")
elif tem_cel in range(59, 64):
    print("Ao ponto")
elif tem_cel in range(65, 70):
    print("Ao ponto para o bem")
elif tem_cel >=71:
    print("Bem passada")
