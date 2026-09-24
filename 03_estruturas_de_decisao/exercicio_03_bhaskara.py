"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
valor_A = float(input("digite o valor de A: "))
valor_B = float(input("digite o valor de B: "))
valor_C = float(input("digite o valor de C: "))
if valor_A == 0:
    print("Impossivel calcular") 
elif (valor_B ** 2 - 4 * valor_A * valor_C) < 0:
    print("Impossivel calcular")
else:
    delta = valor_B ** 2 - 4 * valor_A * valor_C
    R1 = (-valor_B + delta ** 0.5) / (2 * valor_A)
    R2 = (-valor_B - delta ** 0.5) / (2 * valor_A)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")                     


