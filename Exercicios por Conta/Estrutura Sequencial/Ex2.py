# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

salBruto = float(input('Valor recebido por hora: '))
qtdHorasMes = float(input('Quantidade de horas trabalhadas ao Mês: '))

salario = float(salBruto*qtdHorasMes)
inss = float(salario*0.08)
sindicato = float(salario*0.05)
iR = float(salario*0.11)
descontoTotal = float(inss+sindicato+iR)
liquido = salario - descontoTotal
print()
print(f'Salário Bruto: R$ {salario:.2f}')
print(f'Valor pago ao INSS: R$ {inss:.2f}')
print(f'Valor pago ao Sindicato : R$ {sindicato:.2f}')
print(f'Valor pago no Imposto de Renda: R$ {iR:.2f}')
print(f'Valor do Salário Líquido : R$ {liquido:.2f}')
print(f'Desconto Total: R$ {descontoTotal:.2f}')