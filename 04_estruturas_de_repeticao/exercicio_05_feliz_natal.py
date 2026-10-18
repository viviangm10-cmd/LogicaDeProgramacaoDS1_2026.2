"""
EXERCÍCIO 05: Feliz Nataaal!
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba um número inteiro I (nível de empolgação).
Utilize repetição para exibir a frase "Feliz natal!" repetindo a letra 'a'
da palavra natal exatamente I vezes (ex: I=5 -> "Feliz nataaaal!").
"""

# TODO: Desenvolva o algoritmo abaixo:
I = int(input("Digite o nível de empolgação (número inteiro): "))

frase = "Feliz natal!"
for _ in range(I):
    frase = frase.replace("a", "aaa", 1)

print(frase)
