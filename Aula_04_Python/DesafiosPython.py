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

