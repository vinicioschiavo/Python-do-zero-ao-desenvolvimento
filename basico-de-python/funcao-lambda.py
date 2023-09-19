# Lambda Function
    # É uma função (pequena) sem nome
    # Pode ter vários argumentos mas somente 1 expressão
    # Muito utilizada dentro de outras funções
    # Código mais "Clean"

# def somar(x):
#     return x + 10

# print(somar(2))

somar10 = lambda x, y: x + y + 10
print(somar10(2, 4))

#################################################################

# def cubo(num):
#     return num ** 3

# Para criar a função lambda é necessario o nome da função o parametro e o que ela faz.
# nome(cubo) --> parametro(num) --> o que ela faz(num ** 3)
cubo = lambda num: num ** 3

user_number = int(input("Digite um número: "))
print(f"O cubo de {user_number} é {cubo(user_number)}")

####################################################################
# FUNÇÂO CLASSICA

# def multiplicar(num1, num2):
#     return num1 * num2         

# FUNÇÂO LAMBDA
multiplicar = lambda num1, num2: num1 * num2      

user_number1 = int(input("Digite o primeiro número: "))
user_number2 = int(input("Digite o segundo número: "))

print(f"A multiplicação de {user_number1} e {user_number2} é {multiplicar(user_number1, user_number2)}")