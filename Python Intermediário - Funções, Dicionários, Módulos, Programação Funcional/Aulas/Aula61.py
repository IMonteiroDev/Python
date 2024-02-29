'''

Exercicio proposto para realização de validação do primeiro digito

'''
cpf = '15835718845'
nove_digito = cpf[:9]
contador_regressivo = 10

resultado_dig_1 = 0
for digito_1 in nove_digito:
    resultado_dig_1 += int(digito_1)*contador_regressivo
    print(resultado_dig_1)
    contador_regressivo-=1
    
digito_1 = (resultado_dig_1*10)%11

digito_1 = digito_1 if digito_1 <=9 else 0
print(digito_1)
