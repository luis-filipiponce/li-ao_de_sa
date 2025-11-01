tarefas = []

opcao = ""
while opcao != "4":
    print("\n1-Adicionar")
    print('2-remover')
    print('3-mostrar')
    print('4-sair')
    opcao = input("Opção: ")

    if opcao == "1":
        tarefa = input("Tarefa: ")
        tarefas.append(tarefa)
    elif opcao == "2":
        if tarefas:
            print("Tarefas:")
            for i in range(len(tarefas)):
                print(f"{i+1}. {tarefas[i]}")
            num = int(input("Número para remover: ")) - 1
            if 0 <= num < len(tarefas):
                tarefas.pop(num)
    elif opcao == "3":
        for tarefa in tarefas:
            print("-", tarefa)
