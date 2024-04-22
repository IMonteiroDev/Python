# Verificar se um número é par ou ímpar: Desenvolva um programa que receba um número como entrada e determine se ele é par ou ímpar.
import os


while True:
    resposta = input("Informe um número: \n")
    
    try:
        os.system("cls")
        number = int(resposta)
        if number % 2==0:
            print(f'O número {number} é Par')
        else:
            print(f'O número {number} é Impar')
        
    except ValueError:
        print("Informe um valor valido")
        break
    