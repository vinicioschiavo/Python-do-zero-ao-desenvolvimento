# functions (Funções)
    # DRY - Don't repeat yourself.
    # Varios Argumentos (Xargs) identificando o Parametro.

# Criar uma função que armazena numeros e strings (dados)

def agencia(**carro):
    return carro

print(agencia(modelo="Gol", cor="Branca", motor=1.0))
print(agencia(modelo="Gol", cor="Preto"))
print(agencia(modelo="Gol", cor="Azul", motor=1.0, placa=1234))