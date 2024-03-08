# Exemplos de uso de sets

import os


letras = set()

while True:
    letra = input('Digite: ')
    letras.add(letra.lower())
    
    if 'l' in letras:
        os.system('clear')
        print('Parabéns')
        break
    
    print(letras) 