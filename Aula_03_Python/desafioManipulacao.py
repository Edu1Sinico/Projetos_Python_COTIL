# Desafio 01
nomeCompleto = (input("Digite o seu nome completo: "))

arrayNome = nomeCompleto.split()

print(f"Seu nome com todas as letras maiúsculas: {nomeCompleto.upper()}\n")
print(f"Seu nome com todas as letras minúsculas: {nomeCompleto.lower()}\n")
print(f"Quantidade de letras em seu nome: {len(nomeCompleto.replace(" ",""))}\n")
print(f"Quantidade de letras no seu primeiro nome: {len(arrayNome[0])}\n")

# Desafio 02
valor = (input("Digite um valor entre 0 e 9999: "))

print(f"Unidade: {valor[0]}")
print(f"Dezena: {valor[1]}")
print(f"Centena: {valor[2]}")
print(f"Milhar: {valor[3]}")