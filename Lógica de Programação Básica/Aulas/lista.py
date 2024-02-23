'''
Lista realizada após um dia da correção da mesma para afim de fixação
'''


import os

lista= []

while True:
    print('Escolha Opção')
    opcao = input('[i]nserir [a]pagar [l]istar\n')
    
    if opcao =='i':
        os.system('clear')
        
        valor = input('Valor: ')
        lista.append(valor)
    
    elif opcao=='a':
        indice = int(input('Informe o Indice: '))
            
        try:
            del lista[indice]
            print(f'O indice {indice} foi apagado!')
        except IndexError:
            print('Não há este indice')
            
    
    elif opcao=='l':
        if not lista:
            os.system('clear')
            print('Não há nada na lista atual!')
            
        
        else:
            for indice, nome in enumerate(lista):
                print(indice, nome)
                
    elif opcao =='s':
        print('Aqui finaliza o programa!')
        os.system('clear')
        break
    
    else:
        print('Essa opção não existe bb')