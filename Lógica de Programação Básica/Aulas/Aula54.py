"""
Faça uma lista de compas com listas o usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programe quebre com erros de índices inexistentes na lista.
"""


# forma que eu fiz:

# import os

# inserir=[]

# while True:
#     print('Selecione uma opção:')
#     opcao = input('[i]nserir [a]pagar [l]istar [s]air: ')
    
#     if opcao=='i':
#         os.system('clear')
#         valor = input('O que você deseja adicionar: ')
#         inserir.append(valor)
        
#     elif opcao=='a':
#         valor = input('Qual ingrediente: ')
        
#         for valor in valor:
#             inserir.pop(valor)
    
#     elif opcao=='l':
#         for indice, nome in valor:
#             print(indice, nome)
        
#     else:
#         print('Foi informado uma opção valida!')

#resolução d aula

import os

lista=[]

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')