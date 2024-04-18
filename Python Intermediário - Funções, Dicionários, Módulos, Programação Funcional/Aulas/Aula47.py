#Decoradores com parâmetros

def factoryDecorators(nome):
    def factoryFunctions(func): #usada para criar funcoes ou factory functions
        print('Decorador: ', nome)
        
        def aninhada(*args, **kwargs):
            res = func(*args, **kwargs) # Isso permite que a função aninhada passe esses argumentos diretamente para a função original. Resumindo porcamente, Essa função res passa todas as factorydecorators a função soma e realiza a mesma.
            final = f'{res} {nome}'
            print(final)
            return final
        return aninhada
    return factoryFunctions


@factoryDecorators(nome='5')
@factoryDecorators(nome='4')
@factoryDecorators(nome='3')
@factoryDecorators(nome='2')
@factoryDecorators(nome='1')
def soma(x,y):
    return x+y

dez_mais_cindo = soma(10,5)
print(dez_mais_cindo)
