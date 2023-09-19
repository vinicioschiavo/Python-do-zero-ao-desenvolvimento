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
    pass

# criar o objeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()

# criar os parametros do usaurio1
usuario1.nome = "Seya"
usuario1.constelacao = "Pegasus"
usuario1.data_nascimento = "12/02/1990"

# criar os parametros do usaurio2
usuario2.nome = "Yoga"
usuario2.constelacao = "Cisne"
usuario2.data_nascimento = "21/04/1990"

# print
print(usuario1.nome)
print(usuario2.nome)