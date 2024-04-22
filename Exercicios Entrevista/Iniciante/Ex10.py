# Encontrar o maior elemento em uma lista: Escreva um programa que encontre o maior elemento em uma lista de números.

import os

elementList = []

def comp(x):
    os.system("clear")
    
    maior =0
    menor =0
    for num in x:
        if num>maior:
            maior = num
            
        if num<menor:
            menor = num
            
    print(f'O Maior número é: {maior}')
    print(f'O Maior número é: {menor}')
    
    print(*sorted(x))


while True:
    valor = input("Valor:\n")
    
    if valor == 'n' or valor =='':
        if not elementList:
            print("Nenhum valor foi passado")
            break
        
        else:
            comp(elementList)
        
    
    else:
        number = int(valor)
        elementList.append(number)
