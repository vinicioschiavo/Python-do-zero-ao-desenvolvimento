# Erros
    # Excelente para testes
    # Não realiza o "stop" no progrma
    # Mensagens customizadas quando encontra um erro

try:
    valor = int(input("Digite o valor do seu produto: "))
    print(valor)
except ValueError:
    print("Favor digitar o valor do protudo em numeros")
finally:
    print("Codigo OK")
# else:
#     print("Valor final do protudo")
#     resultado = valor * 2
#     print(resultado)

print("mais codidos abaixo")