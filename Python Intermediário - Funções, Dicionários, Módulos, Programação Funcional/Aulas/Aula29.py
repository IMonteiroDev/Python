'''

isinstance -> Para saber se o Objeto é de determinado tipo
No caso o isinstance percorre a lista e vê qual é igual ao tipo que esta sendo procurado
'''

lista = [
    'a', 1, 1.1, True, [0,1,2], (1,2),
    {0,1}, {'nome': 'Luiz'},
]


for item in lista:
    if isinstance(item,set):
        item.add(5)
        print(item, isinstance(item, set))