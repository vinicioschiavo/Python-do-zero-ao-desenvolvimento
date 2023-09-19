# Erros
    # Excelente para testes
    # Não realiza o "stop" no progrma
    # Mensagens customizadas quando encontra um erro

try:
    valor = int(input("Digite o valor do seu produto: "))
    print(valor)
except ValueError:
    print("Favor digitar o valor do protudo em numeros")

print("mais codidos abaixo")