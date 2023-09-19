# Functions (Funções)
    # DRY - Don't repeat yourself.
    # Realizam uma tarefa
    # Calcula e retorna um Valor

def cliente1(nome):
    print(f"Olá {nome}")

def cliente2(nome):
    return f"Olá {nome}"

x = cliente1("Vegeta")
y = cliente2("Bulma")

print(x)
print(y)