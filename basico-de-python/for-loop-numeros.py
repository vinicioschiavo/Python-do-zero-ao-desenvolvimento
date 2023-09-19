# For Loops (Looping)

# imprimir de 1 a 5
# O programa sempre começa a conta pelo 0, entao sempre acrescetar um numero a mais do que o desejado.

for numero in range(6):
    print(numero)

#Caso não deseje o numero 0, informar o começo e fim da numeração.
for numero in range(1, 6):
    print(numero)


#### ou pode ser feito ###########

# 1 é start, 11 é o stop e 1 é o step "encremento", se colocar 2 pula de 2 em 2 ...
for i in range(1, 11, 1):
    print(i)