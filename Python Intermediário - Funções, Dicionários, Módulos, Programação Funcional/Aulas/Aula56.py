'''

split e join com listas e strings

    Split -> Divide uma string
    Join -> Une como string

'''
frase = '          Olha só,             que coisa      interessante!'
lista_frases_cruas = frase.split(',') #Deixa separado apartir dos espaços que a frase possue


lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip()) #strip corta os espaços da frase


print(lista_frases_cruas) #Crua e com espaço
print(lista_frases)

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)