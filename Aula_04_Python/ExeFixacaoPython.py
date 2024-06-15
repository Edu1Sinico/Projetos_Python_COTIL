# Exercício 1
print("\nExercício 1")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("\nDigite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6:
  print("\nAluno aprovado com média", media)
else:
  print("\nAluno reprovado com média", media)

# Exercício 2
print("\n-----------------------------------------------\nExercício 2")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

if num1 > num2:
  print("\nO maior número é ", num1)
  print("O menor número é ", num2)
else:
  print("\nO maior número é ", num2)
  print("O menor número é ", num1)

# Exercício 3
print("\n-----------------------------------------------\nExercício 3")

num = int(input("Digite um número inteiro: "))

if num % 2 == 0:
  print("\nO número ", num, " é par.")
else:
  print("\nO número", num, " é ímpar.")

# Exercício 4
print("\n-----------------------------------------------\nExercício 4")

ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = 2024 - ano_nascimento

if idade >= 18:
  print("\nA pessoa é maior de idade.")
else:
  print("A pessoa é menor de idade.")

# Exercício 5
print("\n-----------------------------------------------\nExercício 5")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

if num1 == num2:
  print("\nOs números são iguais.")
else:
  print("\nOs números são diferentes.")
