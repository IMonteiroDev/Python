"""
Flag - Marcar um local
None = não Valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""

v1 = 'a'
v2 = 'b'

condicao = False
passou_no_if = None

if condicao:
    passou_no_if=True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')