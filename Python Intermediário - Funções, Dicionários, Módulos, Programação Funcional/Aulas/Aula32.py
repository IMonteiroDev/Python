'''

Generator expression, Iterables e Iterators em Python

'''

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()

print(next(iterator))

for iter in iterator:
    print(iter)