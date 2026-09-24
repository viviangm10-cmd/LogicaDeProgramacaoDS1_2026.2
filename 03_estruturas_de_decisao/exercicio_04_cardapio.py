"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
case = (input("Digite o código do item: "))      
quantity = int(input("Digite a quantidade: "))  

if case == "1":
    total = 4.00 * quantity
    print(f"Total a pagar: R$ {total:.2f}")
elif case == "2":
    total = 4.50 * quantity
    print(f"Total a pagar: R$ {total:.2f}")
elif case == "3":
    total = 5.00 * quantity
    print(f"Total a pagar: R$ {total:.2f}")
elif case == "4":
    total = 2.00 * quantity
    print(f"Total a pagar: R$ {total:.2f}")
elif case == "5":
    total = 1.50 * quantity
    print(f"Total a pagar: R$ {total:.2f}")
else:  
 print("Código inválido")