# Set (Listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index

list1 = ([1, 2, 3, 4, 5, 6])
s1 = {1, 2, 3, 4, 5, 6}
s1.update([6, 7, 8, 9, 10])
s1.remove(10) # gera um erro se não existir um numero
s1.discard(9) # não gera um erro se não existir o numero


print(list1)
print(s1)
print(type(list1))
print(type(s1))