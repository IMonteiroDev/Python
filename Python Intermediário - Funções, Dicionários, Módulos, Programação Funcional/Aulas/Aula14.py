'''

Métodos úteis do dicionários em Python
len -> Quantas chaves
keys -> Iteraveis com chaves
values -> Iteravel com os valores
items ->  Iteravel com chaves e valores
setdefault -> adiciona valor se a chave não existe
copy -> retorna uma cópia rasa(shallow copy)
get -> obtém uma chave
pop -> Apaga um item com a chave especificada
popitem -> Apaga o último item adicionado
update -> Atualiza um dicionário com outro

'''

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    # 'idade': 900,
}

pessoa.setdefault('idade',None) #defini caso não criado a key 

print(pessoa.get('idade'))


# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))


# for chave in pessoa:
#     print(chave)

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)