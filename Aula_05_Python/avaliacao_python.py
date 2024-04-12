# Método de Validar Nome
def validarNome(validarNome):
    validarNome = validarNome.capitalize().lstrip().rstrip()
    if len(validarNome) > 2:
        if len(validarNome.split()) > 1:
            for nome in validarNome.split():
                if nome in validarNome.split():
                    return "Por favor, não repita o seu nome/sobrenome!"
                else: 
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
        return "\nCPF Inválido. Por favor, informe o seu número CPF novamente.\n"

# Método de verificar Telefone
def verificarTelefone(vericarTelefone):
    telefoneFormatado = vericarTelefone.replace("(","").replace(")","").replace("-","").replace(" ","")
        
    if len(telefoneFormatado) == 11:
        return True
    else:
        return "\nTelefone Inválido. Por favor, informe o seu número de telefone novamente.\n"

# Método de verificar CEP
def verificarCEP(verificarCEP):
    cepFormatado = verificarCEP.replace(" ","").replace("-","")
    
    if len(cepFormatado) == 8:
        return True
    else:
        return "\nCEP Inválido. Por favor, informe o seu CEP novamente.\n"
    
# Método de verificar Email
def verificarEmail(verificarEmail):
    emailFormatado = verificarEmail.lstrip().rstrip().replace(" ","").lower()

    if emailFormatado.find("@gmail") != -1:
        return True
    else:
        return "\E-mail Inválido. Por favor, informe o seu E-mail novamente.\n"
    
def realizarEmprestimo():
    
    
# Paínel principal
print("\n===================================================\n")
print("Bem-Vindo ao Software de Empréstimo\n")
print("O que você gostaria?\n")
print("    1. Realizar um empréstimo")
print("    2. Sair")

escolha = int(input("\nDigite sua escolha: "))

if escolha == 1: 
    print("\n===================================================\n")

    print("Por favor, preencha as seguintes informações:\n")
    nomeCompleto = input("    - Por favor, informe o seu nome completo: ")
    cpf = input("    - Informe o número do seu CPF: ")
    telefone = input("    - Informe o seu número de telefone: ")
    endereco = input("    - Informe o seu endereço: ")
    cep = input("    - Informe o seu CEP: ")
    email = input("    - Digite o seu E-mail: ")

    if validarNome(nomeCompleto):
        if verificarCPF(cpf):
            if verificarTelefone(telefone):
                if verificarCEP(cep):
                    if verificarEmail(email):
                        print("\n===================================================\n")
                        print(f"Bem vindo: {nomeCompleto}!\n")
                        
                    else:
                        print(verificarEmail(email))
                else: 
                    print(verificarCEP(cep))
            else:
                print(vericarTelefone(telefone))
        else:
            print(verificarCPF(cpf))
    else:
        print(validarNome(nomeCompleto))
            

elif escolha == 2:
    print("\nObrigado por utilizar o meu programa!")
else:
    print("\nPor favor, informe um desses valores!")