"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
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
else:
    print("Nenhum número positivo foi digitado.")