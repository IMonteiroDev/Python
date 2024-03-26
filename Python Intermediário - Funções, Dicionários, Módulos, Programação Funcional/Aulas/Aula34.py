'''

Introdução às Generator functions em Python
Generator = (n for n in range(1000000))

'''
# Toda função geradora usa a palavra Yield(return)
def generator(n=0):
    yield 1 #Pausou nessa Execução
    print('Continuando')
    yield 2 #Pause
    print('Será q chega?')
    yield 3
    print('Fim')
    return 'Fim'

gen = generator(n=0)

# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)