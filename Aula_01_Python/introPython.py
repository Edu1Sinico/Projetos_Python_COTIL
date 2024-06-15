# Exercício 1
print("Exercício 1\n")
num = int(input("Digite um número: "))

resultQuad = num * num
print(f"\nResultado do número digitado ({num}) ao quadrado: {resultQuad}")

print("\n==========================================\nExercício 2\n")
# Exercício 2

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

print(f"\nO usuário digitou os números {num1} e {num2}")

print("\n==========================================\nExercício 3\n")
# Exercício 3

num3 = int(input("Digite um número: "))

numAnt = num3-1
numSuc = num3+1

print(f"\nO número antecessor e o sucessor do número ({num3}) são respectivamente: {numAnt} e {numSuc}")

print("\n==========================================\nExercício 4\n")
# Exercício 4

altura = float(input("Digite a altura do retângulo: "))
base = float(input("Digite a base do retângulo: "))

print(f"\nA área do retângulo é: {altura*base} m²\nO perímetro do retângulo é {(altura*2)+(base*2)} m")

print("\n==========================================\nExercício 5\n")
# Exercício 5

valor = float(input("Digite o Valor: "))
taxa = float(input("Digite o Taxa: "))
tempo = float(int("Digite o Tempo: "))

prestacao = valor + (valor*(taxa/100)*tempo)
print(f"\nvalor da Prestação: {prestacao}")

