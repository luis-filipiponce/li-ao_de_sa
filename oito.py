filmes = []

filme = input("Filme: ")
while filme != "fim":
    ano = input("Ano: ")
    filmes.append(filme + " (" + ano + ")")
    filme = input("Filme (fim para parar): ")

filmes.sort()
for f in filmes:
    print(f)
