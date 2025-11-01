usuarios = []

nome = input("Nome (sair para parar): ")
while nome != "sair":
    senha = input("Senha: ")
    usuarios.append(nome)
    nome = input("Nome (sair para parar): ")

print("Total:", len(usuarios))
for usuario in usuarios:
    print(usuario)
