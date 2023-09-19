# List Comprehension
    # Mais simples de se escrever
    # Utilizando quando você precisa criar uma nova lista a partir de uma existente
    # [expressao for iten in itens]

frutas1 = ["abacate", "banana", "morango", "kiwi", "abacaxi"]
# frutas2 = []

# for iten in frutas1:
#     if "b" in iten:
#         frutas2.append(iten)

frutas2 = [iten for iten in frutas1 if "n" in iten]

print(frutas2)

# print(f"A primeira fruta é: {frutas1[0]}")
# print(f"A ultima fruta é: {frutas1[-1]}")