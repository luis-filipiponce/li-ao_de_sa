carrinho = []
precos = []

opcao = ""
while opcao != "4":
    print("\n1-Adicionar ")
    print("2-Remover ")
    print("3-Mostrar")
    print("4-Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        produto = input("Produto: ")
        preco = float(input("Preço: "))
        carrinho.append(produto)
        precos.append(preco)
    elif opcao == "2":
        if carrinho:
            for i in range(len(carrinho)):
                print(f"{i+1}. {carrinho[i]}")
            num = int(input("Número: ")) - 1
            if 0 <= num < len(carrinho):
                carrinho.pop(num)
                precos.pop(num)
    elif opcao == "3":
        total = 0
        for i in range(len(carrinho)):
            print(f"{carrinho[i]}: R$ {precos[i]}")
            total += precos[i]
        print("Total: R$", total)
