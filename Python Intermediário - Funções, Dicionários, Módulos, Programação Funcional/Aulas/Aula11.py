'''

Exercícios
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parametro

'''


def createMulti(result):
    def multi(num):
        return num*result
    return multi


double = createMulti(2)
triple = createMulti(3)
quadra = createMulti(4)

print(double(4))
print(triple(92))
print(quadra(14))