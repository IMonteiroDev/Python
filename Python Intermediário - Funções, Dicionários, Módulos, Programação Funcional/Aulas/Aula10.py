'''

Closure e funções que retornam funções

'''

def createSalute(msg):
    def salute(name):
        return f'{msg}, {name}!'
    return salute

saidGoodMorning = createSalute('Good Morning')
haveGoodEvening = createSalute('Good Evening')

for name in ['Maria', 'Joana', 'Luiz']:
    print(saidGoodMorning(name))
    print(haveGoodEvening(name))