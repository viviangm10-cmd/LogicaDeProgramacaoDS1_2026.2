"""
EXERCÍCIO 05: Acesso à Bilheteria do Parque
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba a idade do visitante (valor base do ingresso: R$ 100,00):
- Menor que 12 anos: "Infantil" (50% de desconto -> R$ 50,00)
- Maior ou igual a 60 anos: "Melhor Idade" (Gratuidade -> R$ 0,00)
- Demais idades: "Integral" (R$ 100,00)

Imprima o tipo de bilhete e o valor final a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
idade = int(input("Digite a idade do visitante: "))
if idade < 12:      
    tipo_bilhete = "Infantil"
    valor_final = 100 * 0.5
elif idade >= 60:
    tipo_bilhete = "Melhor Idade"
    valor_final = 0
else:
    tipo_bilhete = "Integral"
    valor_final = 100

print(f"Tipo de bilhete: {tipo_bilhete}")
print(f"Valor final a pagar: R$ {valor_final:.2f}") 