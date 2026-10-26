"""
EXERCÍCIO 01: Pontuação OBI (Astro Lume Devs)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma função nomeada `calcular_pontuacao_total(fase1, fase2, fase3)` com a diretiva `def`
que receba as 3 notas como parâmetros e retorne a pontuação total da equipe.
"""

# TODO: Desenvolva a função e os testes abaixo:
<<<<<<< HEAD

def calcular_pontuacao_total(fase1, fase2, fase3):
    return fase1 + fase2 + fase3  
fase1 = float(input("digite a primeira pontuação: "))                                                                    
fase2 = float(input("digite a segunda pontuação: "))                                                                    
fase3 = float(input("digite a terceira pontuação: "))
print(calcular_pontuacao_total(fase1, fase2, fase3))                                                                   
=======
def calcular_pontuacao_total(fase1, fase2, fase3):
    return fase1 + fase2 + fase3
fase1 = float(input("digite a primeita nota: "))
fase2 = float(input("digite a segunda nota: "))
fase3 = float(input("digite a terceira nota: "))

pontuacao_total = calcular_pontuacao_total(fase1, fase2, fase3)
print(f"a pontação total é: {pontuacao_total}")
>>>>>>> 0c3d8b63a287f8e7c815c276ae1ad60d6cfdc3e8
