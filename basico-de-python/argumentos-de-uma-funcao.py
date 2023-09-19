# functions (Funções)
    # DRY - Don't repeat yourself.
    # Parametros --> Argumentos

def boas_vindas(nome, quantidade):
    print(f"Olá {nome}.")
    print(f"Temos {str(quantidade)} laptops em estoque")

boas_vindas("Goku", 5)
boas_vindas("Vegeta", 3)
boas_vindas("Freeza", 2)

'''
def boas_vindas_Goku():
    print("Olá Goku")
    print("Temos 5 leptops em estoque")

def boas_vindas_Vegeta():
    print("Olá Vegeta")
    print("Temos 3 leptops em estoque")

def boas_vindas_Freeza():
    print("Olá Freeza")
    print("Temos 2 leptops em estoque")

boas_vindas_Goku()
boas_vindas_Vegeta()
boas_vindas_Freeza()
'''