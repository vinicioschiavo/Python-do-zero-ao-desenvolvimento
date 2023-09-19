# def par_ou_impar(num):
#     if num % 2 == 0:
#         return "Par"
#     else:
#         return "Impar"
    
# user_number = int(input("Digite um número: "))
# print(f"O Número {user_number} é {par_ou_impar(user_number)}")

# A mesma função so que escrita em formato lambda

par_ou_impar = lambda num: "Par" if num % 2 == 0 else "Impar"
    
user_number = int(input("Digite um número: "))
print(f"O Número {user_number} é {par_ou_impar(user_number)}")