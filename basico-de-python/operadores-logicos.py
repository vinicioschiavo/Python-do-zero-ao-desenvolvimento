# Logical Operators (Operadores Logicos)

# renda_acima_5mil = False
renda_acima_5mil = True
# nome_limpo = True
nome_limpo = False


## "and ou or" "And os dois fatores devem ser iguais pra a aprovar e OR apenas um fator deve ser verdadeiro para aprovar"

if renda_acima_5mil and nome_limpo:
    print("Financimento Aprovado")
else:
    print("Financiamento Negado")