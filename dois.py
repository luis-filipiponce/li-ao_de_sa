nomes = []
notas = []

nome = input("Nome: ")
while nome != "fim":
    nota = float(input("Nota: "))
    nomes.append(nome)
    notas.append(nota)
    nome = input("Nome (fim para parar): ")

soma = 0
for n in notas:
    soma += n

if len(notas) > 0:
    media = soma / len(notas)
    print("Média:", media)

    print("notas acima da média:")
    for i in range(len(nomes)):
        if notas[i] > media:
            print(nomes[i])
