"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
<<<<<<< HEAD
numeros = []
for i in range(6):
    numero = float(input("Digite um número: "))
    if numero > 0:
        numeros.append(numero)

quantidade = len(numeros)
if quantidade > 0:
    media = sum(numeros) / quantidade
    print(f"Quantidade de números positivos: {quantidade}")
    print(f"Média dos números positivos: {media:.1f}")
=======
contador_positivos = 0
soma_positivos = 0

for _ in range(6):
    numero = float(input("Digite um número: "))
    if numero > 0:
        contador_positivos += 1
        soma_positivos += numero

if contador_positivos > 0:
    media = soma_positivos / contador_positivos
    print(f"Quantidade de números positivos: {contador_positivos}")
    print(f"Média aritmética dos números positivos: {media:.1f}")
>>>>>>> 0c3d8b63a287f8e7c815c276ae1ad60d6cfdc3e8
else:
    print("Nenhum número positivo foi digitado.")