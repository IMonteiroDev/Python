def executa (funcao, *args):
    return funcao (*args)


def soma(x,y):
    return x+y

def criaMulti(multiplicador):
    def multi(num):
        return num*multiplicador
    return multi




print(
    executa(
        lambda x,y:x+y,
        2,3
    )    
)

print(
    executa(
        
    )
)