# Escreva um programa que verifique se um número fornecido pelo usuário é primo ou não.

def primo(n):
    int(n)
    mult = 0
    
    if(n <=1 ):
        return False
    
    for i in range(2, int (n**0.5)+1):
        if n% i ==0:
            return False
    return True

numero = int(input("Digite um número inteiro positivo: "))

if primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
    