"""

Iterando Strings com While

"""
#-------012345678910111213
nome = 'Igor Monteiro' #iteráveis = percorrer até o fim da string


tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)

# print(nome[3])

# Como eu Fiz

qtd = 0;

# while qtd<tamanho_nome:
#     print(f'*{nome[qtd]}*')
#     qtd+=1
    
# print('Acabou')

#A forma como o Professor resolveu

qtd = 0;
novo_nome = ''

while qtd<tamanho_nome:
    novo_nome += (f'*{nome[qtd]}')
    
    qtd+=1
    

novo_nome+='*'

print(novo_nome)

print('Acabou')