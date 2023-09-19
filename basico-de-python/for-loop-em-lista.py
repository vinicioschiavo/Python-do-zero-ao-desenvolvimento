# frutas = ["maça", "banana", "maça", "maça", "abacate", "uva"]
# contador = 0

# for frutas in frutas:
#     if frutas == "maça":
#         contador += 1
# print("numero de maças na lista: ", contador)


###################################################################

# numeros = [1,2,3,4,5,6,7,8,9,10]
# Ou
numeros = list(range(1,16))

for i in numeros:
    if i % 2 == 0:
        print(f"O numero {i} é par!")
    else:
        print(f"O numero {i} é impar!")