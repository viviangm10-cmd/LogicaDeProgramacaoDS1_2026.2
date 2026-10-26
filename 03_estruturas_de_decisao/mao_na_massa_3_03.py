# TODO: Implemente o menu utilizando match-case ou elif
opcao = int(input("Digite a opção desejada (1, 2 ou 3): "))

# Desenvolva a estrutura de seleção aqui
opcao1 = 1
opcao2 = 2
opcao3 = 3

if opcao == opcao1:
    print("voce escolheu a opção consultar livros")
elif opcao == opcao2:
    print("voce escolheu a opção emprestar livros")
elif opcao == opcao3:
    print("voce escolheu a opção devolver livros") 
else:
    print("Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3).")