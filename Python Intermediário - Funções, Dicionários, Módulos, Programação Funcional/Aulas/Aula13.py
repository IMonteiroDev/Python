'''

Manipulando Chaves e valores em dicionários

'''

pessoa ={}


chave = 'nome'

pessoa[chave] = 'Igor Monteiro'
pessoa['sobrenome'] = 'Monteiro'
lista = []


# del pessoa['sobrenome']
print(pessoa)
print(pessoa[chave])

if pessoa.get('sobrenome') is None :
    print('NÃO EXISTE')
else:
    print('Existe')
    print(pessoa['sobrenome'])
    
# print('ISSO NÃO EXISTE')