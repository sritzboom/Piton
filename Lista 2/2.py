#Leia um vetor de 40 posições e conte quantos elementos pares se encontram no
#vetor.

vet = []
cont = 0

for i in range(0,10):
    n = int(input('Valor no vetor: '))
    vet.append(n)
for j in range(0,10):
    if vet[j] % 2 == 0:
        cont += 1
print('Números de números pares: ',cont)
