"""

Introdução ao Try/except
try -> Tentar exercutar o código
except -> mensagem de algum erro ao tentar exercutar

"""
numero = input('Vou dobrar o valor que for informado: ')


try:    
    print(f'String: {numero}')
    numeInt = int(numero);
    print(f'Int: {numeInt}')
    print(f'O dobro do valor {numeInt} é {numeInt*2}') 

except:
    print('O valor mencionado não é um Número!')