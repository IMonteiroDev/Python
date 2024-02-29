"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao Final
    insert - Adiciona um Item no índice Escolhido
    pop - Remove do final ou do índice escolhido
    del - Apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena Lista
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)


Cuidados com Dados Mutáveis
= - copiado o valor(imutáveis)
= - aponta para o mesmo valor na memória (mutável)


"""

# Exemplos

# #        0   1   2   3   4   5
# lista = [10, 20, 30, 40]
# #       -4  -3  -2  -1

# lista.append('Igor')
# nome = lista.pop()
# lista.append(1233)
# del lista[-1]
# # lista.clear()
# lista.insert(0, 'Igor') #mesmo a posição q foi passada sendo inexistente o programa jogara na última posição 
# print(lista)


# lista_a= [1,2,3]
# lista_b= [4,5,6]
# lista_c= lista_a+lista_b

# lista_a.extend(lista_b) #com está função vc adiciona tudo oq estiver na lista extendida, lista_b, para a Lista em questão lista_a

# print(lista_a)

lista_a = ['Luiz', 'Maria', 1 , True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'

print(lista_b) 