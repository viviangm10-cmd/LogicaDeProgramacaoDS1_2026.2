"""
EXERCÍCIO 05: Feliz Nataaal!
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba um número inteiro I (nível de empolgação).
Utilize repetição para exibir a frase "Feliz natal!" repetindo a letra 'a'
da palavra natal exatamente I vezes (ex: I=5 -> "Feliz nataaaal!").
"""

# TODO: Desenvolva o algoritmo abaixo:
<<<<<<< HEAD
numero = int(input("Digite um número inteiro para o nível de empolgação: "))

print("Feliz nata" + "a" * numero + "l!")
=======
I = int(input("Digite o nível de empolgação (número inteiro): "))

frase = "Feliz natal!"
for _ in range(I):
    frase = frase.replace("a", "aaa", 1)

print(frase)
>>>>>>> 0c3d8b63a287f8e7c815c276ae1ad60d6cfdc3e8
