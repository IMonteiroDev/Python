'''

Generator expression, Iterables e Iterators em Python

Generator são funções que sabem pausar em certa parte



Diferença entre Lista e Generator:
    - Lista vc já possui todos os indices disponivel na memória do computador por já ter sido criado quando executado o código diferentemente do *Generator*
    
    - Generator é uma função que pausa e vai acompanhando cada execução



'''

import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) #tem __iter__ e __next__

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator)) #O iterador nesse caso tem o mesmo valor que possui na lista, a diferença é q a lista está toda na memória enquanto o generator espera a solicitação para o retorno

