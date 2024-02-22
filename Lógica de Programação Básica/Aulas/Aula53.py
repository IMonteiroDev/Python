"""

Enumerate - Enumera iteráveis (índices)

"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)

#De forma geral, quando utiliza enumerate criamos uma lista encadeada aonde será apontava para um local e conseguindo ligar um ao outro!
    # Podendo ser utilizado com for mas a melhor forma utilizando a propria biblioteca utilizando lista, aonde você percorrerá o ponteiro é apontaram ao fim para nulo!

# print(next(lista_enumerada))

# for item in lista_enumerada: #para cada Item q tenha Lista_enumerada
#     print(item) #imprima
    

print(lista_enumerada)


lista_enumerada = list(enumerate(lista))

print(lista_enumerada)

