# Escreva um programa que calcule a média de uma lista de números.

import os

def media (numero):
    soma = sum(numero)
    return soma/len(numero)

listaNumero = []

while True:
    resposta = input('Deseja adicionar um número?\n')
    
    if resposta== 'n':
        os.system("cls")
        break
    
    else:
        valor = int(resposta)
        listaNumero.append(valor)
        

print(f'A Média foi de {round(media(listaNumero),2)}')