# Try, except, else e finally



try:
    a = 18
    b = 0
    print('Linha 1')
    c = a/b
    print('Linha 2')

except ZeroDivisionError:
    print('Dividiu por 0 ')
    
except NameError:
    print('Nome b não está Definido')

except (TypeError, IndexError):
    print('TypeError + Index Error')
    
except Exception:
    print('Erro Desconhecido')
    
print('Continua')