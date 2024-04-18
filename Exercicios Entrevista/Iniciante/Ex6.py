#   Palíndromo

frase = input('Informe uma frase para ver se é palindromo:\n').lower()

frase_sem_Pontuacao = ''.join(letras for letras in frase if letras.isalnum())

if(frase_sem_Pontuacao == frase_sem_Pontuacao[::-1]):
    print("É Palindromo!")
    
else:
    print("Não é Palíndromo!")