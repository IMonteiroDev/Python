#Decoradores com parâmetros

def factoryDecorators(a=None, b=None, c=None):
    def factoryFunctions(func): #usada para criar funcoes ou factory functions
        print('Decoradora 1')
        
        def aninhada(*args, **kwargs):
            print('Parâmetros do Decorador, ',a,b,c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return factoryFunctions


@factoryDecorators(1,2,3)
def soma(x,y):
    return x+y

decoradora = factoryDecorators()
multiplica = decoradora(lambda x,y: x*y)

dez_mais_cindo = soma(10,5)
dez_vez_cinco = multiplica(10,5)
print(dez_mais_cindo)
print(dez_vez_cinco)
