"""

Tipo tupla - Uma Lista Imutável
    Quando for realizar uma lista de coisas Permanentes Utilize sempre Tupla, por ser mais rápido.
    
"""

nomes = ['Maria', 'Helena', 'Luiz']

#para converter um array para tupla

nomes = tuple(nomes)

#Ao contrario tbm há desta forma voltando a tupla para array
nomes = list(nomes)

print(nomes[-1])
print(nomes)
