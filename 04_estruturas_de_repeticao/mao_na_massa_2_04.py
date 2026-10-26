# TODO: Desenvolva o acumulador com parada no 0
soma = 0

# Escreva a estrutura de repetição while
while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    if numero == 0:
        break
    soma += numero

print(f"A soma dos números digitados é: {soma}")
