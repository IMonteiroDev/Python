# Funções Decoradores e decoradores
# Decorar = Adicionar / remover/ restringir / alterar
# Funçoes decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# Usar as funções decoradoras em outras funções

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

def inverteString(string):
    return string[::-1]

def isString(param):
    if not isinstance(param, str):
        raise TypeError('Parametro deve ser uma String')

inverteStringChecandoParametro = createFunction(inverteString)
invertida = inverteStringChecandoParametro('Olá Mundo') 
print(invertida)