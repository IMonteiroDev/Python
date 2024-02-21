# Um posto está vendendo combustíveis com a seguinte tabela de descontos:

# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro

# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro 
# 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

print('Bom dia, Meu querido o que vai ser abastecido? ')
informe = input('A - álcool\nG - Gasolina\n').upper()
qtd = int(input('Legal. Qual a quantidade? '))
alcool = 1.90
gasolina = 2.50

if qtd>0:
    if informe=='A':
        if qtd<=20:
            valor = float((alcool*qtd)*0.97)
        
        else:
            valor = float((alcool*qtd)*0.95)
        
    elif informe=='G':
        if qtd<=20:
            valor = float((gasolina*qtd)*0.96)
        
        else:
            valor = float((gasolina*qtd)*0.94)
        
    else:
            print('Não tenho esse combustivel não em!')
            
    
    print(f'Prontinho chefia, o valor há ser pago será R$ {valor:.2f}')
    
else:
    print('Valor invalido!')
    
    