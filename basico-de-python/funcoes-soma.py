# Functions (Funções)
    # DRY - Don't repeat yourself.

def somar_dois_numeros():
    numero1 = 10
    numero2 = 5
    resultado = numero1 + numero2
    print(resultado)

def somar_dois_numeros1():
    numero1 = 10
    numero2 = 2
    resultado = numero1 + numero2
    print(resultado)

somar_dois_numeros()
somar_dois_numeros1()

############################################################################

def quadrado(numero):
    return numero ** 2

num = int(input("Digite o numero desejado: "))
print(f"O quadrado de {num} é {quadrado(num)}")

#############################################################################

def soma(num1, num2):
    return num1 + num2

user_num1 = int(input("Digite o primeiro numero: "))
user_num2 = int(input("Digite o segundo numero: "))

print(f"A soma dos dois numeros é igual a: {soma(user_num1, user_num2)}")

# Ou pode ser feito dessa forma tambem

def subtracao(num1, num2):
    result = num1 - num2
    print(f"A subtracao dos dois numeros é igual a: {result}")

user_num1 = int(input("Digite o primeiro numero: "))
user_num2 = int(input("Digite o segundo numero: "))

subtracao(user_num1, user_num2)

######################################################################

def potencia(base, expoente=2):
    return base ** expoente

user_number = int(input("Digite o numero base: "))
user_exponente = input("Digite um expoente (default 2): ")

if user_exponente:
    print(f"O resultado é: {potencia(user_number, int(user_exponente))}")
else:
    print(f"O resultado é: {potencia(user_number)}")

