import random

# Exercício 1
print("\nExercício 1")


def advinhar(): 
    num = int(input("Informe um valor entre 1 a 5: "))
    numRdm = random.randint(1,5)
    
    while tudoCerto:
        if num == numRdm:
            tudoCerto = False
            return "\nVocê acertou o número!\n"
        elif num > numRdm:
            return "\nO número é maior que o número pensado.\n"
        else:
            return "\nO número é menor que o número pensado."

print(advinhar())

# Exercício 2
print("\n-----------------------------------------------\nExercício 2")
velocidade = float(input("Informe a velocidade do carro: "))

if (velocidade > 80):
    print(f"A velocidade do seu carro ultrapassou 80km/h, você deve pagar uma multa de: R$ {((velocidade-80)*7)}")
else:
    print("Você está livre da multa.")
    
# Exercício 3
print("\n-----------------------------------------------\nExercício 3")
num = int(input("Informe um valor: "))

if num%2 == 0:
    print("O valor digitado é par.")
else:
    print("O valor digitado é ímpar.")
    
# Exercício 4
print("\n-----------------------------------------------\nExercício 4")
distancia = int(input("Informe a distância da viagem: "))

if distancia <= 200:
    print(f"Valor por KM para pagar: R$ {(distancia*0.5)}")
else:
    print(f"Valor por KM para pagar: R$ {(distancia*0.45)}")

# Exercício 5
print("\n-----------------------------------------------\nExercício 5")
ano = int(input("Digite um ano qualquer: "))

if ano%4 == 0:
    print("\nO ano digitado é bissexto")
else:
    print("\nano digitado não é bissexto")

# Exercício 6
print("\n-----------------------------------------------\nExercício 6")
num1 = int(input("Informe o primeiro número: "))
num2 = int(input("\nInforme o segundo número: "))
num3 = int(input("\nInforme o terceiro número: "))

if num1 > num2 and num1 > num3:
    resultado = "\nO primeiro número digitado é o maior."
elif num2 > num1 and num2 > num3:
    resultado = "\nO segundo número digitado é o maior."
elif num3 > num1 and num3 > num2:
    resultado = "\nO terceiro número digitado é o maior."
else:
    resultado = "\n Alguns dos números são iguais."

print(resultado)

# Exercício 7
print("\n-----------------------------------------------\nExercício 7")
salario = float(input("Digite o seu salário: R$ "))

if salario > 1250:
    salarioAumentado = salario + (salario*0.1)
else:
    salarioAumentado = salario + (salario*0.15)

print(f"\nO salário foi aumentado para: R$ {salarioAumentado}")

# Exercício 8
print("\n-----------------------------------------------\nExercício 8")
a = int(input("Informe o primeiro comprimento: "))
b = int(input("\nInforme o segundo comprimento: "))
c = int(input("\nInforme o terceiro comprimento: "))

if (a+b>c) and (a+c>b) and (b+c>a):
    print("\nOs valores dos lados forma um triângulo.\n")
else:
    print("\nOs valores dos lados não forma um triângulo\n")
