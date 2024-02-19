""" Calculado com While """


informe =''
while informe!='s':
    
    num1 = input('Informe um valor: ')
    num1_int = int(num1)
    num2 = input('Informe outro valor: ')
    num2_int = int(num2)
    operacao = input('Qual operação: ')
    
    if(operacao=='+'):
        print('O resultado é: ',num1_int+num2_int)
        
    elif(operacao=='-'):
        print('O resultado é: ',num1_int-num2_int)
        
    elif(operacao=='*'):
        print('O resultado é: ',num1_int*num2_int)
        
    elif(operacao =='/'):
        print('O resultado é: ',num1_int/num2_int)
        
    else:
        print('Operação Informada incorreta!')
    
    informe = input('Deseja Sair: s/n ').lower().startswith('s')
    
    
print('Acabou')


# Forma com o Professor Resolveu


""" Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    ###

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break


