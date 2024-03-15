valorDigitado = input("Digite alguma coisa: ")

print("A variável é do tipo: ", type(valorDigitado))
print("É uma variável numérica? ",valorDigitado.isnumeric())
print("É uma variável do tipo String? ", valorDigitado.isalpha())
print("É uma variável alfa numérica? ", valorDigitado.isalnum())
print("Está com as letras maiúsculas? ", valorDigitado.isupper())
print("Está com as letras minúsculas? ", valorDigitado.islower())
print("É uma variável decimal?", valorDigitado.isdecimal())