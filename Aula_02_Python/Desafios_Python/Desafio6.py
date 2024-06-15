valorMetros = float(input("Digite o valor em metros: "))

def converterCm():
    return valorMetros*100

def converterMl():
    return valorMetros*1000

print(f"O valor em centímetros é {converterCm()}")

print(f"O valor em milímetros é {converterMl()}")