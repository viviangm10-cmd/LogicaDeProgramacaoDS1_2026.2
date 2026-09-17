"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
nota1 = float(input("qual sua nota1?"))
nota2 = float(input("qual sua nota2?"))
nota3 = float(input("qual sua nota3?"))
nota1 = nota1 * 2
nota2 = nota2 * 3
nota3 = nota3 * 5
media_ponderada = (nota1 + nota2 + nota3) / (3)
print(f"sua media ponderada é: {media_ponderada}")