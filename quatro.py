produtos = []
precos = []

produto = input("Produto: ")
while produto != "fim":
    preco = float(input("Preço: "))
    produtos.append(produto)
    precos.append(preco)
    produto = input("Produto (fim para parar): ")

total = 0
for i in range(len(produtos)):
    print(f"{produtos[i]}: R$ {precos[i]}")
    total += precos[i]

print("Total: R$", total)
