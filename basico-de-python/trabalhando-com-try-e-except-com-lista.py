# Erros
    # Excelente para testes
    # Não realiza o "stop" no progrma
    # Mensagens customizadas quando encontra um erro

# letras = ["a", "b", "c"]
# print(letras[3])

# O erro existe mais não é mostrado no console e é possivel continuar mostrando o index error.
try:
    letras = ["a", "b", "c"]
    print(letras[3])
except IndexError:
    print("index não existe")