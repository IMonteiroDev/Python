# Escreva um programa que calcule a média de uma lista de números.


def media (numero):
    soma = sum(numero)
    return soma/len(numero)

listaNumero = []

while True:
    resposta = input('Deseja adicionar um número?\n')
    
    if resposta== 'n':
        break
    
    else:
        valor = int(resposta)
        listaNumero.append(valor)
        

print(f'A Média foi de {media(listaNumero)}')