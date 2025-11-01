estoque_nomes = []
estoque_qtde = []

opcao = ""
while opcao != "3":
    print("1-Adicionar 2-Mostrar 3-Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Produto: ")
        qtde = int(input("Quantidade: "))
        estoque_nomes.append(nome)
        estoque_qtde.append(qtde)
    elif opcao == "2":
        for i in range(len(estoque_nomes)):
            print(f"{estoque_nomes[i]}: {estoque_qtde[i]}")
