frase = 'O Python é uma linguagem de programação '\
        'multiparadigma. '\
        'Python foi criado por Guido van Rossum'
        

indice = 0

apareceuMais = 0
letraApare = ''

while indice<len(frase):
    letra_atual = frase[indice]
    
    if letra_atual == ' ':
        indice+=1
        continue
    
    qtd = frase.count(letra_atual)
    
    if(apareceuMais<qtd):
        apareceuMais = qtd
        letraApare = letra_atual
    
    indice+=1
    
print('A letra que apareceu mais vezes foi '
      f'"{letraApare.upper()}" que a pareceu ' f'{qtd} x')