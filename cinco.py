alunos = []

for i in range(5):
    nome = input(f"Aluno {i+1}: ")
    alunos.append(nome)

presentes = []
for aluno in alunos:
    resp = input(f"{aluno} está presente? (s/n): ")
    if resp == "s":
        presentes.append(aluno)

print("Compareceram:", len(presentes))
print("Faltaram:")
for aluno in alunos:
    if aluno not in presentes:
        print("-", aluno)
