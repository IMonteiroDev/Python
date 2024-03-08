'''

Sets - Conjuntos em Python(tipo set)
Conjuntos são ensinados na matemática

Representados graficamente pelo Diagrama de Venn
Sets em Pythib são mutáveis, porém aceitam apenas 
tipos imutáveis como valor interno

'''

#set(itéravel) ou {1,2,3}

# s1 = {'Luiz',1,2,3} #set com Dados
# s1 = set('') #set Vazio

# print(s1)

'''

Sets são eificientes para remover valores duplicados de iteráveis.
Não aceitam valores mutáveis;
Seus valores serão sempre únicos;
Não tem índexes;
Não garantem Ordem;
São Iteráveis (for, in ,not in)

'''
# l1 = {1,2,3,4,4,4,4,4,1}

# s1 = set(l1)
# l2 = list(s1)

# s1 = {1,2,3}

# print(3 not in s1) #possibilidade de iteraveis para averiguação de valores internos salvos no set!

# for numero in s1:
#     print(numero)

# s1 = set()
# s1.add('Luiz')
# s1.add(1)
# s1.update(('Olá Mundo',1,2,3,4)) #Aqui estamos passando tudo como iteravel
# # s1.clear()
# s1.discard('Olá Mundo')
# print(s1)

# Métodos Úteis:
# add, update, clear, discard

# Operadores Úteis:
#     União | união (union) - une
# Intersecção & (intersection) - Itens presentes em ambos
# Diferença - Itens presentes apenas no set da esquerda
# Diferença Simétrica ^ - Itens que não estão em ambos

s1 = {1,2,3}
s2 = {2,3,4}
# s3 = s1|s2
# s3 = s1 & s2
# s3 = s1 - s2
s3 = s1^s2

print(s3)