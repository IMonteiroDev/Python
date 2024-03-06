'''

Exercícios com funções

Crie uma função que multiplica todos os argumentos
Não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável.

Crie uma função fala se um número é par ou impar
Retorne se o número é par ou ímpar

'''


def multiplicar(*args):
    total = 0
    for numero in args:
        total *=numero
        
    return total

def dedos(numero):
        multiplo = numero%2==0
    
        if multiplo:
            return('Resultado é Par')
        else:
            return('Resultado é Impar')
    

multiplicacao = multiplicar(0,4,4,2,8,5,6,9,8)
print(multiplicacao)

print(dedos(13))

