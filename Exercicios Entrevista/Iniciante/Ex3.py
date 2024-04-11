# Escreva uma função para calcular o fatorial de um número.

def fatorial(numero):
    if numero == 0:
        return 1
    else:
        qtd=1
        for i in range(1, numero+1):
            qtd*=i
        return qtd


num = int(input('Informe um número para Fatorar:\n'))

print(fatorial(num))