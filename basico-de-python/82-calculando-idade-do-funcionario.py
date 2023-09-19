from datetime import datetime

# Python object-Oriented Programming

# Classes
    # Utilizadas para criar Objetos (instances)
    # Objetos são partes de dentro de uma Class (instancias)
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar
    # ====
    # Class: Frutas
    # Objects: Abacate, Banana...

#  criar uma classe
class Funcionarios:
    
    def __init__(self, nome, constelacao, ano_nascimento):
        self.nome = nome
        self.constelacao = constelacao
        self.ano_nascimento = ano_nascimento
    
    def nome_completo(self):
        return self.nome + " " + self.constelacao
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento

# criar o objeto
usuario1 = Funcionarios("Seya", "Pegasus", 1992)
usuario2 = Funcionarios("Yoga", "Cisne", 1991)
usuario3 = Funcionarios("Iki", "Fenix", 1990)

# print
print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.idade_funcionario(usuario2))
print(Funcionarios.idade_funcionario(usuario3))
