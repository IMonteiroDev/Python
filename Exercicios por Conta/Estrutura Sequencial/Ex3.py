# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.


litrosTinta = 18
valor = 80.00

informe= int(input('Informe o metro quadrado a ser pintado: '))
qtdLitros = informe/3

print(f'Para a àrea pintada em questão, será necessaria: {qtdLitros:.2f} litros.')
print(f'Algo entorno de {qtdLitros/litrosTinta:.1f} latas, que serão em torno de R$ {(qtdLitros/litrosTinta)*valor:.2f}')