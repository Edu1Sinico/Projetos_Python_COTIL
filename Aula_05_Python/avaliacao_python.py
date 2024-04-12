
# Método de Validar Nome
def validarNome(validarNome):
    if len(validarNome) > 2:
        if validarNome.strip() > 0:
            for nome in validarNome.split():
                if validarNome.split().find(validarNome.split(nome)):
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

if emailFormatado.find("@") != -1 and verificarEmail.find("gmail") != -1:
    return True
else
    

    

numeroTelefone = input("Digite um número de telefone: ")

if vericarTelefone(numeroTelefone):
    print("\nTelefone com formatação correta.")
else:
    print("\nTelefone com formatação incorreta.")
