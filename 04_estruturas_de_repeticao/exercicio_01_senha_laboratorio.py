"""
EXERCÍCIO 01: Senha Fixa do Laboratório
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Repita a leitura da senha até que o usuário digite a senha correta (2002).
Para cada tentativa incorreta, imprima "Senha Invalida".
Ao acertar, imprima "Acesso Permitido" e finalize o programa.
"""

<<<<<<< HEAD
# TODO: Desenvolva o algooritimo aqui em baixo:
=======
# TODO: Desenvolva o algoritmo abaixo:
>>>>>>> 0c3d8b63a287f8e7c815c276ae1ad60d6cfdc3e8
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
