# Seleciona as 4 letras do inicio da palavra/frase
frase = (input("Digite a Frase: "))
converteFrase = frase[:4]
print(f"A quarta palavra é: { converteFrase}")

# Seleciona as 4 letras do fim da palavra/frase
frase = (input("Digite a Frase: "))
converteFrase = frase[4:]
print(f"A quarta palavra é: { converteFrase}")

# Seleciona os elementos em dois em dois da palavra/frase
frase = (input("Digite a Frase: "))
converteFrase = frase[2:8:2]
print(f"A quarta palavra é: { converteFrase}")

# Informa a quantidade de caracteres da String
frase = (input("Digite a Frase: "))
converteFrase = len(frase)
print(f"A quarta palavra é: { converteFrase}")

# Informa a quantidade de vezes que aparece o caracter da letra "o" da String
frase = (input("Digite a Frase: "))
converteFrase = frase.count("o")
print(f"A quarta palavra é: { converteFrase}")

# Verica se a palavra "cotil" está na frase, verifica a posição do elemento. Caso contrário, retorna -1.
frase = (input("Digite a Frase: "))
converteFrase = frase.find("cotil")
print(f"A quarta palavra é: { converteFrase}")

# Verica se a palavra "cotil" está na frase. Retorna True ou False.
frase = (input("Digite a Frase: "))
converteFrase = "Cotil" in frase
print(f"A quarta palavra é: { converteFrase}")

#####################################################################################################

frase = (input("Digite a Frase: "))
converteFrase = frase.upper()
print(f"A quarta palavra é: { converteFrase}")

frase = (input("Digite a Frase: "))
converteFrase = frase.lower()
print(f"A quarta palavra é: { converteFrase}")

# Coloca a primeira letra maiúscula.
frase = (input("Digite a Frase: "))
converteFrase = frase.capitalize()
print(f"A quarta palavra é: { converteFrase}")

# Coloca a primeira letra de cada palavra em maiúscula.
frase = (input("Digite a Frase: "))
converteFrase = frase.title()
print(f"A quarta palavra é: { converteFrase}")

frase = (input("Digite a Frase: "))
converteFrase = frase.replace("Javascript","Python")
print(f"A quarta palavra é: { converteFrase}")

