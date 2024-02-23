'''

Desempacotamento em chamadas
de métodos e funções

'''

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    #0         1 
    ['Maria', 'Helena', ], #0 Indidice 0
    
    #0
    ['Elaine', ], #1 indice 1
    
    #0        1        2
    ['Luiz', 'João', 'Eduarda', (0,10,20,30,40)], #2 indice
]


# a, b, *_,ap, u = lista
# print(a, ap)

# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')