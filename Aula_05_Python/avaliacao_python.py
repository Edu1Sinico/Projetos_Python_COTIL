import re # Importação da módulo RE (Permite com que utilizemos o método Match)

# Método de Validar Nome
def validarNome(validarNome):
    validarNome = validarNome.title().lstrip().rstrip() # Deixa as primeiras letras de cada palavra em maiúsculas e remove os espaços inúteis da direita e esquerda.
    if re.match(r'^[a-zA-Z\s]+$',validarNome): # Verifica se o nome possui apenas letras e espaços
        if len(validarNome) > 2: # Verifica se o nome possuí mais de dois caracteres
            if len(validarNome.split()) > 1: # Verifica se o nome possui mais de um sobrenome
                nome = validarNome.split()
                if len(nome) == len(set(nome)): # Verifique se todos os nomes são únicos
                    return True
                else:
                    return "\nPor favor, não repita o seu nome/sobrenome!\n"
            else:
                return "\nPor favor, insira o seu sobrenome!\n"
        else:
            return "\nPor favor, seu nome deve conter mais de duas letras!\n"
    else:
        return "\nPor favor, utilize apenas letras para compor o seu nome!\n"
                
# Método de verificar CPF
def verificarCPF(verificarCPF):
    if re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}$',verificarCPF): # Validação de CPF
        return True
    else:
        return "\nCPF Inválido. Por favor, informe o seu número CPF novamente.\n"

# Método de verificar Telefone
def verificarTelefone(vericarTelefone):
        
    if re.match(r'\(\d{2}\)\d{5}-\d{4}$',vericarTelefone): # Validação de Telefone
        return True
    else:
        return "\nTelefone Inválido. Por favor, informe o seu número de telefone novamente.\n"

# Método de verificar CEP
def verificarCEP(verificarCEP):
    
    if re.match(r'\d{5}-\d{3}$',verificarCEP): # Validação de CEP
        return True
    else:
        return "\nCEP Inválido. Por favor, informe o seu CEP novamente.\n"
    
# Método de verificar Email
def verificarEmail(verificarEmail):
    emailFormatado = verificarEmail.lstrip().rstrip().replace(" ","").lower() #Formata o email recebido como parâmetro

    if emailFormatado.find("@gmail.com") != -1 and emailFormatado.count("@") == 1: # Validação de Email
        return True
    else:
        return "\nE-mail Inválido. Por favor, informe o seu E-mail novamente.\n"

# Método de realizar emprestimo
def realizarEmprestimo(valor_emprestimo, salario, meses):
    prestacao = valor_emprestimo / meses

    if prestacao > (salario * 0.3):
        return "\nO valor da prestação excede 30% do seu salário!"
    else:
        return (f"\nvalor da prestação será: R$ {prestacao}")

continuar = 1
continuar2 = 1
continuar3 = 1

while continuar == 1:
# Paínel principal
    print("\n===================================================\n")
    print("Bem-Vindo ao Software de Empréstimo\n")
    print("O que você gostaria?\n")
    print("    1. Realizar um empréstimo")
    print("    2. Sair")

    escolha = int(input("\nDigite sua escolha: "))

    if escolha == 1:
        while continuar2 == 1:
            print("\n===================================================\n")
            print("Por favor, preencha as seguintes informações:\n")
            nomeCompleto = input("    - Por favor, informe o seu nome completo: ")
            cpf = input("    - Informe o número do seu CPF (Segue o padrão: 123.456.789-10): ")
            telefone = input("    - Informe o seu número de telefone (Segue o padrão: (99)99999-9999): ")
            endereco = input("    - Informe o seu endereço: ")
            cep = input("    - Informe o seu CEP (Segue o padrão: 12345-678): ")
            email = input("    - Digite o seu E-mail (Segue o padrão: SeuEmail@gmail.com): ")

            if validarNome(nomeCompleto) is True:
                if verificarCPF(cpf) is True:
                    if verificarTelefone(telefone) is True:
                        if verificarCEP(cep) is True:
                            if verificarEmail(email) is True:
                                while continuar3 == 1:
                                    print("\n===================================================\n")
                                    print(f"Bem vindo: {nomeCompleto.title()}!\n")
                                    print("Por favor, preencha as seguintes informações:\n")
                                    salario = float(input("    - Informe o seu salário: R$ "))
                                    valor_emprestimo = float(input("    - Informe o valor do emprestimo: R$ "))
                                    meses = int(input("    - Informe a quantidade de meses: "))
                                    print(realizarEmprestimo(valor_emprestimo,salario,meses))
                                    continuar3 = int(input("\nDeseja Continuar?\n(Precione 1 para 'SIM' ou qualquer outro número para 'NÃO'.): "))
                                    continuar2 = continuar3
                            else:
                                print(verificarEmail(email))
                        else: 
                            print(verificarCEP(cep))
                    else:
                        print(verificarTelefone(telefone))
                else:
                    print(verificarCPF(cpf))
            else:
                print(validarNome(nomeCompleto))
                

    elif escolha == 2:
        print("\nObrigado por utilizar o meu programa!\n")
        continuar = escolha
    else:
        print("\nPor favor, informe um desses valores!\n")
        continuar = int(input("Deseja Continuar?\n(Precione 1 para 'SIM' ou qualquer outro número para 'NÃO'.): "))