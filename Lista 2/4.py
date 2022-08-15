#Ler um vetor de números inteiros de 30 posições. Depois, ler um número inteiro X,
#imprimir quantas vezes o número X aparece no vetor.

vet = []
somaX = 0

for i in range(0,30):
    vet.append(input('Número: '))

x = int(input('Buscar número: '))
for j in range(0,30):
    if x == vet[j]:
        somaX += 1
print('O número',x,'aparece',somaX,'vezes no vetor')