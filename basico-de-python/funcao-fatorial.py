# def fatorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fatorial(n - 1)
    
# user_number = int(input("Digite um número: "))
# print(f"O fatorial de {user_number} é {fatorial(user_number)}")

################################################################################

def dobrar(num):
    return num * 2

def quadrado(num):
    return dobrar(num) ** 2

user_number = int(input("Digite o número desejado: "))
print(f"O quadrado do dobro do número {user_number} é {quadrado(user_number)}")