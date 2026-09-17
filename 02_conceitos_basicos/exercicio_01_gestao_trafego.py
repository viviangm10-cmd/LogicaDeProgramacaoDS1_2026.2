"""
EXERCÍCIO 01: Gestão de Tráfego Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
A loja Casas Paulino está veiculando anúncios no Meta Ads em Tianguá.
Escreva um programa que leia:
1. O valor total investido na campanha (em R$).
2. O número total de cliques obtidos.

Calcule e mostre na tela o Custo Por Clique (CPC) médio da campanha formatado em reais.
"""

# TODO: senvolva o algoritmo abaixo:
valor_total_investido = input("Digite o valor total investido na campanha (em R$): ")
valor_total_investido = float(valor_total_investido)
numero_total_cliques = input("Digite o número total de cliques obtidos: ")
numero_total_cliques = int(numero_total_cliques)
cpc_medio = valor_total_investido / numero_total_cliques
print(f"O CPC médio da campanha é: R$ {cpc_medio:.2f}")