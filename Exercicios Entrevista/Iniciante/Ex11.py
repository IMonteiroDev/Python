# Ordenar uma lista em ordem crescente: Crie uma função que receba uma lista de números como entrada e retorne a mesma lista ordenada em ordem crescente.

import os

arrayNumber = []

while True:
    try:
        resposta = input("Número:\n")
        number = int(resposta)
        arrayNumber.append(number)
        
    except ValueError:
        print("Passe o valor valido")
    
    if resposta == 'n':
        os.system("clear")
        break

print(sorted(arrayNumber))