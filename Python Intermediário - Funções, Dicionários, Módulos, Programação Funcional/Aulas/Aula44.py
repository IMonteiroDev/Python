#Exercicios - Adiando Execução de Funções
# Utiliza o Yield maybe

def soma(x, y):
    return x+y

def multiplica(x,y):
    return x*y


# Utilizado aqui Closure para ter uma recursão interna e adiar o processo
def criar_funcao(funcao, x):
    def adiar(y):
        return funcao(x,y)
    return adiar

# De forma banal, a função acima realiza a função e deixa armazenado na memoria o valor de x que foi passado primeiramente e para no return adiar, esperando assim a continuação quando for invocado na segunda vez para complementar o resto da mesma

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(3))
print(multiplica_por_dez(2))