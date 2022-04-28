#email prof miguel.figueiredo@uva.br

#PAREI EM FLAG E RODAR SOMA(SEM PRINT DA SOMA)

#soma, subtrai, divide, determina se um número é positivo ou negativo ou se é zero

#MENU PRINCIPAL DA ULA
# 1 DEFINIR REGISTRADOR A
# 2 DEFINIR REGISTRADOR B
# 3 LER A
# 4 LER B
# 5 LER REGISTRADOR DE FLAGS (flag tem que ser menor que 30 (?))
# 6 DEFINIR OPERACAO (MIN 4)
# 7 EXECUTAR ULA
# 8 SAIR


registradorA = 0
registradorB = 0
registradorFlag = 0
varInput = ''
varOperacao = ''

#definir funcoes ULA

def soma(regA, regB):
    return regA+regB

def sub(regA, regB):
    return regA-regB

def mult(regA, regB):
    return regA*regB

def div(regA, regB):
    return regA/regB

def verificaFlag(regFlag):
    if(regFlag >= 30):
        print('Erro Flag - maior ou igual a 30. Valor atual: '+registradorFlag)
    else:
        return 0


def switchFuncao(varInput):
    global registradorA
    global registradorB
    global registradorFlag

    if(varInput == '1'):
        registradorA = input('DEFINIR REGISTRADOR A\n')
        print('regA: '+registradorA)
    elif(varInput == '2'):
        registradorB = input('DEFINIR REGISTRADOR B\n')
        print('regB: '+registradorB)
    elif(varInput == '3'):
        print('test - 3 LER A\n')
        print(registradorA)
    elif(varInput == '4'):
        print('test - 4 LER B\n')
        print(registradorB)
    elif(varInput == '5'):
        #flag
        print('test - 5 LER REGISTRADOR DE FLAGS\n')
        flagCheck = verificaFlag(registradorFlag)
        if(flagCheck == 0):
            print('Flag OK\n')
        else:
            print(registradorFlag)
        #flag
    elif(varInput == '6'):
        print('test - 6 DEFINIR OPERACAO\n')
        varOperacao = input('DEFINA A OPERACAO\n1. SOMA\n2. SUBTRACAO\n3. MULTIPLICACAO\n4 .DIVISAO\n')
    elif(varInput == '7'):
        print('test - 7 EXECUTAR ULA\n')
        switchOperacao(varOperacao)
    elif(varInput == '8'):
        print('test - 8 SAIR\n')
        exit()
    else:
        print('valor de input nao definido.\n')
        return 0


def switchOperacao(op):
    if(op == '1'):
        print(soma(registradorA, registradorB))
    elif(op == '2'):
        print(sub(registradorA, registradorB))
    elif(op == '3'):
        print(mult(registradorA, registradorB))
    elif(op == '4'):
        print(div(registradorA, registradorB))
    else:
        print('valor de operacao nao definido\n')
        return 0



#rodar ULA



while(varInput != '8' or varInput.lower() != 'sair'):
    varInput = input('MENU PRINCIPAL DA ULA\ndigitar apenas os numeros\n\n1. DEFINIR REGISTRADOR A\n2. DEFINIR REGISTRADOR B\n3. LER A\n4 LER B\n5 LER REGISTRADOR DE FLAGS (flag tem que ser menor que 30 (?))\n6 DEFINIR OPERACAO (MIN 4)\n7 EXECUTAR ULA\n8 SAIR\n')    
    switchFuncao(varInput)




