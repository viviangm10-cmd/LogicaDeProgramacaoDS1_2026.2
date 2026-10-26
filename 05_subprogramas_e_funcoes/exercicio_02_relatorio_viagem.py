"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
def calcular_custo_transorte(distancia_km, consumo_kml, preco_combustivel):
    return distancia_km + consumo_kml + preco_combustivel
distancia_km = float(input("digite a distancia percorrida: "))
consumo_kml = float(input("digite o consumoo: "))
preco_combustivel = float(input("digite o total de combustivel consumido: "))

def calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao):
    return qtd_pessoas + dias + diaria_alimentacao
qtd_pessoas  = float(input("digite a quantidade de pessoas: "))
dias = float(input("digite a quantidade de dias: "))
diaria_alimentacao = float(input("digite diaria de alimentção: "))

print(calcular_custo_transorte(distancia_km, consumo_kml, preco_combustivel))
print(calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao))