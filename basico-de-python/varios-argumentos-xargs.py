# functions (Funções)
    # DRY - Don't repeat yourself.
    # Varios Argumentos (Xargs)

# Criar uma função que soma vários números.

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

x = soma(2,3,4,7)

print(x)