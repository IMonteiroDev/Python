'''
    Formatação De Strings
    s - string
    d - int
    f - float
    
    .<número de dígitos>f
    x ou X - hexadecimal
    (caractere) (><^)(quantidade)
    > - esquerda
    < - direita
    ^ - centro
    = - Força o número aparecer antes dos zeros
    
    sinal - + ou -
    
    ex.: 0>-100 ,.1f
    conversion flags - !r !s !a

'''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}>')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.15748543181284:,.1f}')
print(f'{variavel}')