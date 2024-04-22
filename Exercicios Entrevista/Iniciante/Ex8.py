# Converter temperatura de Celsius para Fahrenheit: Escreva um programa que converta uma temperatura em graus Celsius para Fahrenheit.

import os

while True:
    resposta = input("Informe a Temperatura em ºC:\n")
    number = float(resposta)
    
    try:
        os.system("cls")
        fahr = (number*9/5)+32
        print(f'A temperatura {resposta}ºC é {round(fahr, 2)}º Fahrenheit')
    except ValueError:
        print("Você passou valor Invalido!")