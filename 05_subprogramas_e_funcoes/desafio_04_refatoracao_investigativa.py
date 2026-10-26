"""
DESAFIO 04: REFATORAÇÃO INVESTIGATIVA
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O código monolítico repete cálculos de desconto e impostos várias vezes.

SUA MISSÃO:
1. Crie uma função calcular_preco_final(preco_base, taxa_desc, taxa_imp) com return.
2. Crie um procedimento exibir_relatorio_item(numero_item, preco_final) com print.
3. Teste suas funções refatoradas.
"""

# TODO: Desenvolva as funções modulares abaixo
def calcular_preco_final(preco_base, taxa_desc, taxa_imp):
    return preco_base + taxa_desc + taxa_imp
preco_base = float(input("digite o preço base: "))
taxa_desc = float(input("digite a taxa de desconto: "))
taxa_imp = float(input("digite a taxa de imposto: "))

def exibir_relatorio_item(numero__item, preco_final):
    return numero__item + preco_final
numero_item = float(input("digite o numero do item: "))
preco_final = float(input("digite o preçõ final: "))

print(calcular_preco_final(preco_base, taxa_desc, taxa_imp))
print(exibir_relatorio_item(numero_item, preco_final))