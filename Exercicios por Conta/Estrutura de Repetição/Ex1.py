# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

multa = 4.00
pesoLimite = 50.00

peso = float(input('Informe o peso do Peixe: '))

if peso<=pesoLimite:
    print('Para esse peixe não haverá multa a ser paga!')
    
else:
    pesoPeixe=float(peso-pesoLimite)
    
    print(f'Esse peixe está acima do limite em {pesoPeixe}.\n'\
        f'O valor da multa a ser paga será de: R$ {multa*pesoPeixe:.2f}')