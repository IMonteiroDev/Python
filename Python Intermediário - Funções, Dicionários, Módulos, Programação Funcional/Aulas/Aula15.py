# Utilizando o Input para receber informações do usuario

nome = input('Qual o seu nome? ')

print(f'Olá {nome} Tudo bem?')

# da forma abaixo demonstra qual variavel esta armazenado e que expressa seu valor

print(f'Olá {nome=} tudo bem?')

# Para utilizar o input como int/float deve-se utilizar o casting

num1 = input('Informe um número: ')
num2 = input('Informe outro: ')

num1_int=int(num1)
num2_int=int(num2)

print(f'A soma dos numeros {num1} e {num2} é de {num1_int+num2_int}')