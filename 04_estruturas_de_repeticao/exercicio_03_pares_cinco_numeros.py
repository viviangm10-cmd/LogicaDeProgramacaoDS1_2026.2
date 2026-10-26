"""
EXERCÍCIO 03: Pares entre Cinco Números
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite 5 números inteiros ao usuário.
Utilize uma estrutura de repetição e um contador para verificar quantos números pares
foram digitados. Ao final, imprima a quantidade total.
"""

<<<<<<< HEAD
# TODO: Desenvolva o algoritmo abaixo:
contador = 0
for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        contador += 1
print(f"Quantidade de números pares: {contador}")
=======
# TODO: Desenvolva o algoritmo abaixo: 
contador_pares = 0

for _ in range(5):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        contador_pares += 1

print(f"Quantidade de números pares digitados: {contador_pares}")
>>>>>>> 0c3d8b63a287f8e7c815c276ae1ad60d6cfdc3e8
