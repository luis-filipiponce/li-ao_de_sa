estoque_nomes = []
estoque_qt = []

opcao = ""
while opcao != "3":
    print("\n1-Adicionar")
    print("2-Mostrar")
    print("3-Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Produto: ")
        qtde = int(input("Quantidade: "))
        estoque_nomes.append(nome)
        estoque_qt.append(qtde)
    elif opcao == "2":
        for i in range(len(estoque_nomes)):
            print(f"{estoque_nomes[i]}: {estoque_qt[i]}")
