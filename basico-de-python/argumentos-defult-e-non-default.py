# functions (Funções)
    # DRY - Don't repeat yourself.
    # Parametros --> Argumentos
    # Default = Aquele que você define o valor no parametro
    # Non-Default = Aquele que você não define o valor no parametro

def boas_vindas(quantidade, nome= "Goku"):
    print(f"Olá {nome}.")
    print(f"Temos {str(quantidade)} laptops em estoque")

boas_vindas(5)