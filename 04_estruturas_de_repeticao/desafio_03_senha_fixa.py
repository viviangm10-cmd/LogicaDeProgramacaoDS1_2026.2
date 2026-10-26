"""
DESAFIO 03: O BUG DA SENHA FIXA DO LABORATÓRIO
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O laço de repetição do login está em loop infinito mesmo quando o usuário acerta a senha.

SUA MISSÃO:
1. Identifique por que o laço não encerra.
2. Aplique o comando adequado de quebra de fluxo (break).
"""

# CÓDIGO ORIGINAL COM LOOP INFINITO:
# senha_correta = "2002"
# while True:
#     tentativa = input("Digite a senha de acesso: ")
#     if tentativa == senha_correta:
#         print("Acesso Permitido")
#     else:
#         print("Senha Invalida")

# TODO: Escreva aqui a versão corrigida:
senha_correta = "2002"
while True:
    tentativa = input("Digite a senha de acesso: ")
    if tentativa == senha_correta:
        print("Acesso Permitido")
<<<<<<< HEAD
        break  # Encerra o loop quando a senha correta é digitada
    else:
        print("Senha Invalida") 
=======
        break
    else:
        print("Senha Invalida")

>>>>>>> 0c3d8b63a287f8e7c815c276ae1ad60d6cfdc3e8
