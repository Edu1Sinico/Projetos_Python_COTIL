nota1 = float(input("Digite a nota 1 do aluno: "))
nota2 = float(input("Digite a nota 2 do aluno: "))

def calcularMedia():
    return (nota1+nota2)/2

print(f"A média do aluno é: {calcularMedia()}")