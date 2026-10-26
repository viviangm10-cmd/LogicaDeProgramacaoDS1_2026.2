"""

EXERCÍCIO 02: Resto da Divisão por 5

Disciplina: Lógica de Programação com Python


ENUNCIADO:

Leia dois valores inteiros X e Y.

Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)

cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

<<<<<<< HEAD
# TODO: Desenvolva o algoritmo abaixo:
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

for i in range(x, y + 1):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
=======

# Leia os dois valores inteiros.
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

# Percorra os valores em ordem crescente, mesmo que sejam informados invertidos.
inicio = min(x, y)
fim = max(x, y)

for i in range(inicio, fim + 1):
    if i % 5 == 2 or i % 5 == 3:
        print(i)

>>>>>>> 0c3d8b63a287f8e7c815c276ae1ad60d6cfdc3e8
