# Desafio 01:
nomeCompleto = (input("Digite o seu nome completo: "))

arrayNome = nomeCompleto.split()

print(f"Seu nome com todas as letras maiúsculas: {nomeCompleto.upper()}\n")
print(f"Seu nome com todas as letras minúsculas: {nomeCompleto.lower()}\n")
print(f"Quantidade de letras em seu nome: {len(nomeCompleto.replace(" ",""))}\n")
print(f"Quantidade de letras no seu primeiro nome: {len(arrayNome[0])}\n")

# Desafio 02:
valor = (input("Digite um valor entre 0 e 9999: "))
uMedida = ["Unidade","Dezena","Centena","Milhar"]

for i in range(4):
    print(uMedida[i] + ": " + valor[i])

# Desafio 03:
cidade = (input("Digite uma cidade: "))
arrayCidade = cidade.split()

if arrayCidade[0] == "Santo":
    print(f"A cidade {cidade} possuí 'Santo' no seu primeiro nome")
else:
    print(f"A cidade {cidade} não possuí 'Santo' no seu primeiro nome")

# Desafio 04
nome = (input("Digite o seu nome completo: "))

if "Silva" in nome:
    print("Seu nome possuí 'Silva'.")
else:
    print("Seu nome não possuí 'Silva'.")

# Desafio 05
frase = (input("Digite a Frase: "))

print(f"A quarta palavra é: {frase.count("o")}")

