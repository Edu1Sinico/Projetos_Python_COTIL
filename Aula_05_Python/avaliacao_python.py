
# Método de Validar Nome
def validarNome(validarNome):
    if len(validarNome) > 2:
        if validarNome.strip() > 0:
            for nome in validarNome.split():
                if validarNome.split().find(validarNome.split(nome) != -1):
                    return "Por favor, não repita o seu nome/sobrenome!"
                else: 
                    # nomeMinusculo = validarNome.lower().lstrip().rstrip()
                    return True  
        else:
            return "Por favor, insira o seu sobrenome!"
    else:
        return "Por favor, seu nome deve ter mais de duas letras!"
                
# Método de verificar CPF
def verificarCPF(verificarCPF):
    cpfFormatado = verificarCPF.replace(".","").replace("-","").replace(" ","")
    if len(cpfFormatado) == 11:
        return True
    else:
        return False

# Método de verificar Telefone
def vericarTelefone(vericarTelefone):
    telefoneFormatado = vericarTelefone.replace("(","").replace(")","").replace("-","").replace(" ","")
        
    if len(telefoneFormatado) == 11:
        return True
    else:
        return False

# Método de verificar CEP
def verificarCEP(verificarCEP):
    cepFormatado = verificarCEP.replace(" ","").replace("-","")
    
    if len(cepFormatado) == 8:
        return True
    else:
        return False
    
# Método de verificar Email
def verificarEmail(verificarEmail):
    emailFormatado = verificarEmail.lstrip().rstrip().replace(" ","").lower()

    if emailFormatado.find("@gmail") != -1:
        return True
    else:
        return False    

# Paínel principal
print("\n===================================================\n")
print("Bem-Vindo ao Software de Empréstimo\n")
print("O que você gostaria?\n")
print("    1. Realizar um empréstimo")
print("    2. Sair")

escolha = int(input("\nDigite sua escolha: "))

if escolha == 1: 
    print("\n===================================================\n")
    # numeroTelefone = input("Digite um número de telefone: ")
    # if vericarTelefone(numeroTelefone):
    #     print("\nTelefone com formatação correta.")
    # else:
    #     print("\nTelefone com formatação incorreta.")

elif escolha == 2:
    print("\nObrigado por utilizar o meu programa!")
else:
    print("\nPor favor, informe um desses valores!")