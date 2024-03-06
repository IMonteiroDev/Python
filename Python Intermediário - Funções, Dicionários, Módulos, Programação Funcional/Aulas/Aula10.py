'''

Closure e funções que retornam funções

'''

def createSalute(msg, name):
    def salute():
        return f'{msg}, {name}!'
    return salute

s1 = createSalute('Good Morning', 'Lucas')
s2 = createSalute('Good evening', 'Luiz')

print(s1())
print(s2())