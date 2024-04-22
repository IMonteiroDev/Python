# Contar a quantidade de vogais em uma palavra: Desenvolva uma função que receba uma palavra como entrada e retorne a quantidade de vogais presentes na palavra

vogal = 0

while True:
    resposta = input("Informe a Palavra: \n")
    lowerLetter = resposta.lower()
    vowel = 'aeiou'
    vogais = []
    
    for letra in lowerLetter:
        if letra in vowel:
            vogal+=1
            vogais.append(letra)
        
    
    print("Total de vogais:", vogal)
    for a in vogais:
        print(a)
