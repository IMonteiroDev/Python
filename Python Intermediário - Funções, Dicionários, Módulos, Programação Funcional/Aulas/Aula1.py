'''

Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None(nada).

Parametro => Valor que a função recebe, no caso do Exemplo oq fica dentro do Print(a, b, c)


Argumento => Varias que são recebidas no Print para a realização da Função

'''

def Print(a, b, c):
    return print(a, b, c, sep=', ')

Print(1, 2, 3)

Print(15, 30 ,40)

def saudacao(nome='Sem nome'): #Predefine na variavel um valor caso não seja passado nada pelo usúario
    return print(f'Olá, {nome}')

saudacao('Igor')
saudacao()

