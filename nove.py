candidatos = []
votos = []

candidato = input("Candidato: ")
while candidato != "fim":
    candidatos.append(candidato)
    votos.append(0)
    candidato = input("Candidato (fim para parar): ")

voto = input("Vote no candidato: ")
while voto != "fim":
    if voto in candidatos:
        pos = candidatos.index(voto)
        votos[pos] += 1
    voto = input("Vote no candidato (fim para parar): ")

for i in range(len(candidatos)):
    print(f"{candidatos[i]}: {votos[i]} votos")
