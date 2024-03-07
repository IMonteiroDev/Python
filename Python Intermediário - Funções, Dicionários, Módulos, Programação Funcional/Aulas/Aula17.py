# Exercício - sistema de perguntas e respostas
import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtdAcertos = 0

for quest in perguntas:
    print(f'Pergunta: {quest['Pergunta']}')
    print()
    
    opcoes = quest['Opções']
    for i, choice in enumerate(opcoes):
        print(f'{i})', choice)
    print()
    
    escolha = input('Escolha uma opção: ')
    
    acertou = False
    escolha_int = None
    qtdOpcoes = len(opcoes)
    
    if escolha.isdigit():
        escolha_int = int(escolha)
        
    if escolha_int is not None:
        if escolha_int>=0 and escolha_int< qtdOpcoes:
            if opcoes[escolha_int]== quest['Resposta']:
                acertou = True
    
    print()
    if acertou:
        os.system('clear')
        print('Você acertou ')
        qtdAcertos+=1
    else:   
        os.system('clear')
        print('Errou')
        
    print()
    
    
print(f'Você acertou {qtdAcertos}')