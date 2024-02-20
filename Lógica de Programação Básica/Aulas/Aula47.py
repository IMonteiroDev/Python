"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

letraAcertada = '' #realizou a variavel fora do loop para manter sem alteração seu resultado

palavraSecreta= 'Indianapolis'
qtd = len(palavraSecreta)
palavraTenta= qtd*'*'
tentativa =0

while True:
    
    informe = input('Digite um letra: ')
    qtdletra=len(informe)
    tentativa+=1
    
    if qtdletra>1:
        print('Informa apenas uma letra por vez')
        tentativa+=1
        
    if informe in palavraSecreta:
        letraAcertada+=informe
        
    palavraFormada = ''
    
    for letraSecreta in palavraSecreta: #foi realizado aqui uma matriz para conseguir percorrer o array afim de achar um char compativel ao informado pelo usuário!
        if letraSecreta in letraAcertada:
            palavraFormada+=letraSecreta
                        
        else:
            palavraFormada+='*'
    
    print(palavraFormada)
    
    if palavraFormada == palavraSecreta:
        os.system('clear')
        print('Você acerto a palavra!')
        print('A palavra era', palavraSecreta)
        print('Tentativas: ',tentativa)
        break
    