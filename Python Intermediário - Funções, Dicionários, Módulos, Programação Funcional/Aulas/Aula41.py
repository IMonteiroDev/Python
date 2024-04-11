# Utilizando Importação de outra pasta
# De forma geral quando se dá um import ele será apresentado apenas uma vez no sistema pelo motivo de ele ser um Singleton.
# A Menos que vc utilize do import importlib e sua função reload aonde que toda a vez que for chamada será realizado a execução de tudo que estiver na variavel em si

import importlib
import os

import aula41imp

print(aula41imp.variavel)

for i in range(10):
    importlib.reload(aula41imp)
    print(i)
print('Fim')