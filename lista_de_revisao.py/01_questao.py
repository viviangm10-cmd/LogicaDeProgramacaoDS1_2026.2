import string


def calcular_valor_frete(distancia, tipo_de_cliente):
    """Calcula o valor do frete com base na distância percorrida."""
    if distancia < 0:
        raise ValueError("A distância não pode ser negativa")

    valor_frete = distancia * 0.5
    if distancia > 100:
        valor_frete += 15.00

    if tipo_de_cliente == "vip":
        valor_frete *= 0.8

    return valor_frete 

dis = float(input("digite a distancia(km): "))
tipo = str(input("digite o tipo de cliente(vip ou padrão): "))

if dis < 0:
    print("a distancia não pode ser negativa")
else: 
    resultado = calcular_valor_frete(dis, tipo)
    print(f"o valor total é: {resultado:.2f}")





