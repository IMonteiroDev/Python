'''

Argumentos Nomeados e não nomeados em Funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)

'''

def soma(x, y, z=0):
    print(f'A soma de {x} + {y} é: {x+y}')

soma(15, 20)

soma(y=30, x=15)
