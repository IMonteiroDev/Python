texto = 'Python'

# indice = 0

# tamanho_string = len(texto)

# while indice<tamanho_string:
#     print(texto[indice], indice)
    
#     indice +=1
    
# Ao invés de montar o código acima, pode-se utilizar o for in como abaixo

#Para cada letra no texto faça


novo_texto = ''
for letra in texto:
    novo_texto+=f'*{letra}'
    print(letra)
    

print(novo_texto+'*')