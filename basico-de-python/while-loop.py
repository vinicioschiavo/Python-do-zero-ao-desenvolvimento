# == While Loops ==

# Excelete para loops dependentes de uma condição.

#  Criar uma promoção para um produto no valor de R$100.

# valor = 100
# dia = 0
# while valor > 20:
#     dia += 1
#     print(f" No dia {dia} o produto vai ser vendido por R${valor}")
#     valor -= 5

########################################################################

while True:
    fruta = input("Digite o nome da fruta certa: ")
    if fruta.lower() == "abacate":
        break
print("Parabens você acertou o nome da Fruta!")