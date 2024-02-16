"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Olá, que horas são meu caro: ')

if hora.isdigit():
    horaInt = int(hora)
    
    if horaInt<=11:
        print('Bom dia Senhor(a)!')
    elif horaInt<17:
        print('Boa Tarde Senhor(a)!')
    else:
        print('Boa Noite Senhor!')
else:
    print('Senhor, você não informou um valor correto')

