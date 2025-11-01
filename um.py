alunos = []

nome = input("Digite um nome: ")
while nome != "sair":
    alunos.append(nome)
    nome = input("Digite um nome ou insira sair para parar: ")

print("Alunos:", alunos)
print("Total:", len(alunos))
