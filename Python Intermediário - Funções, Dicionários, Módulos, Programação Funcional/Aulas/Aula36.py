# Try, except, else e finally

string = 'Luiz'

try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1')
    c = a/b
    print('Linha 2')

except ZeroDivisionError:
    print('Dividiu por 0 ')
    
except NameError:
    print('Nome b não está Definido')

except (TypeError, IndexError) as error:
    print('TypeError + Index Error')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
    
except Exception:
    print('Erro Desconhecido')
    
print('Continua')