'''

Filter em list comprehension

'''
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

novos_produtos = [
    {**produto, 'preco': produto['preco']*1.05}
    if produto['preco']>20 else {**produto}
    for produto in produtos
]

# print(novos_produtos)
# print(*novos_produtos, sep='\n')

# p(novos_produtos)
# lista = [n for n in range(10) if n < 5] #if do filtro se for verdadeira
# print(lista)

novos_produtos = [
    {**produto, 'preco': produto['preco']*1.05}
    if produto['preco']>20 else {**produto}
    for produto in produtos
    if produto['preco']>10
]
#o que vem a esquerda do for é Mapeamento, o que fica a direita do for é filtro

p(novos_produtos)

