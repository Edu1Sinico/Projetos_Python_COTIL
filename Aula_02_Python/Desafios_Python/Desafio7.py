valor = int(input("Digite um número: "))
listaTabuada = []

def tabuada():
    for i in range(11):
        listaTabuada.append(valor*i)
    return listaTabuada

print(f"A tabuada do {valor} é: {tabuada()}" )
