#  Enviar um email com os detalhes da compra online (maximo de 3 tentativas)
#  para compras confirmadas.

# compras_confirmada = True
# #compras_confirmada = False
# dados_compra = "Compra no valor e R$12.50 e entrega confirmada"

# for enviar in range(3):
#     if compras_confirmada:
#         print(dados_compra)
#         print("Detahes enviado para o seu email")
#         break
# else:
#     print("Falha na compra")

#####################################################################

print("Loop com o break:")
for numero in range(1, 11):
    if numero > 5:
        break
    print(numero)

print("Loop com continue:")
for numero in range(1, 11):
    if numero == 5:
        continue
    print(numero)