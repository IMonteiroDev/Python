"""

Introdução ao Desempacotamento 
    Trata-se de ser um desempacotamento de array referenciando o seu indice nas variaveis criada anteriormente

"""

nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']

print(nome2)



# para desempacotar uma quantidade maior de informações na lista em uma variavel criando uma outra lista fica:

# *_ utilizado como convenção no local d resto

nome1, *_ = ['Maria', 'Helena', 'Luiz']

print(nome1, *_, sep=', ')

#caso queira o valor do indice 2 utilizamos assim:

_, nome2,*_ = ['Maria', 'Helena', 'Luiz']

print(nome2, *_, sep=', ')