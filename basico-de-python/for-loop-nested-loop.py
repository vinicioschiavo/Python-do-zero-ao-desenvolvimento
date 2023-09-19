#  == for loop nested ==

# Outer loop
# Inner loop

for numero1 in range(1, 6):
    print("Produto" + str(numero1))
    for numero2 in range(11):
        print(numero1, numero2)

###########################################################
# ou pode ser feito esse outro for loop usando nested

# frutas = ["banana", "maça", "morango"]
# legumes = ["couve", "cenoura", "batata"]

# for fruta in frutas:
#     for legume in legumes:
#         print(fruta, legume)