# TODO: Crie a função lambda aqui
calcular_acrescimo = lambda valor, percentual: valor * (percentual / 100)
float_valor = float(input("Digite o valor do produto: "))
percentual_acrescimo = float(input("Digite o percentual de acréscimo: "))   
acrescimo = calcular_acrescimo(float_valor, percentual_acrescimo)
print(f"O acréscimo é de R$ {acrescimo:.2f}")
