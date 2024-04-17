# Funções Decoradores e decoradores
# Decorar = Adicionar / remover/ restringir / alterar
# Funçoes decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# Usar as funções decoradoras em outras funções
# Decoradores são "Syntax Sugar" (Açucar Sintático) significa q a linguagem possuem recurso q facilita o uso das funções decoradoras, sem a necessidade de rescreever o código

def createFunction(funct):
    def inter(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            isString(arg)
        resultado = funct(*args, **kwargs)
        print(f'O seu resultado foi {resultado}')
        print('Ok, agora você foi decorada!')
        return resultado
    return inter

@createFunction #Syntax Sugar aqui.
def inverteString(string):
    print(f'{inverteString.__name__}')
    return string[::-1]

def isString(param):
    if not isinstance(param, str):
        raise TypeError('Parametro deve ser uma String')

invertida = inverteString('Olá Mundo') 
print(invertida)