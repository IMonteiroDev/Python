"""

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Funções de primeira classe

"""


def saudacao(msg, nome):
    return f'{msg}, {nome}!'

#tenta descrever oq está a ocorrer nesse código
# De forma geral no print estamos chamando uma função que usará outra para resultar em seu bom dia, e de forma a discriminar oq já foi passado temos as tuplas para empacotar tudo é ser considerado


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)