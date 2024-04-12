# Package, começando a útilizar Pacotes para programar.

from sys import path

import aula42_package.modulo
from aula42_package import modulo
from aula42_package.modulo import falaOi, soma_do_modulo, variavel,nova_variavel

# from aula99_package.modulo import soma_do_modulo

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(aula42_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)
falaOi()