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
    
    def __init__(self, nome, constelacao, data_nascimento):
        self.nome = nome
        self.constelacao = constelacao
        self.data_nascimento = data_nascimento
    
    def nome_completo(self):
        return self.nome + " " + self.constelacao

# criar o objeto
usuario1 = Funcionarios("Seya", "Pegasus", "12/02/1992")
usuario2 = Funcionarios("Yoga", "Cisne", "21/04/1992")
usuario3 = Funcionarios("Iki", "Fenix", "05/09/1990")

# print
# print(usuario1.nome + " " + usuario1.constelacao)
# print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario1))
