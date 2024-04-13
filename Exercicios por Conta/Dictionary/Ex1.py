# Exercicios da Medium
# https://medium.com/reflex%C3%A3o-computacional/6-exerc%C3%ADcios-dicion%C3%A1rios-cc226b2453cb


# 1. Faça um programa que possua um Dicionário, adicione elementos ao dicionário e os mostre na tela.

listaCompras = {}

def adcionandoCompras(produto, valor):
    preco = float(valor)
    if preco>0:
        listaCompras[produto] = preco #como estou passando variaveis e necessario utilizar a mesma 
    else:
        print('Valor incorreto')
        
    print(listaCompras)


produto= input('Informe um Produto: \n')
preco = input('Informe o Preço do Produto: \n')
print()
adcionandoCompras(produto, preco)

