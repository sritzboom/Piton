#Leia uma frase e imprima o total de vogais, o total de brancos e o total do resto
somaV = 0
somaB = 0
somaR = 0

frase = input('Frase: ')

for i in range(0,len(frase)):
    if frase[i] == 'a' or frase[i] == 'e' or frase[i] == 'i' or frase[i] == 'o' or frase[i] == 'u':
        somaV += 1
    elif frase[i] == ' ':
        somaB += 1
    else:
        somaR += 1

print('Vogais: ',somaV)
print('brancos: ',somaB)
print('resto: ',somaR)