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
frase = input("Digite uma frase: ")

contador_A = 0
primeira_posicao = None
ultima_posicao = None

for i in range(len(frase)):
    if frase[i] == 'A' or frase[i] == 'a':
        contador_A += 1
        if primeira_posicao is None: 
            primeira_posicao = i + 1 
        ultima_posicao = i + 1

print("Quantidade de vezes que 'A' aparece:", contador_A)
if contador_A > 0:
    print("Posição da primeira ocorrência de 'A':", primeira_posicao)
    print("Posição da última ocorrência de 'A':", ultima_posicao)
else:
    print("A letra 'A' não foi encontrada na frase.")

# Desafio 06
nome_completo = input("Digite o nome completo: ")

partes_nome = nome_completo.split()
primeiro_nome = partes_nome[0]
ultimo_nome = partes_nome[-1]

print("Primeiro nome:", primeiro_nome)
print("Último nome:", ultimo_nome)
