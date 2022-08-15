#Faça um programa para ler 50 valores de temperaturas em graus Celsius.
#Transformar essas temperaturas em Farenheit e imprimir a media das temperaturas
#em Celsius e Farenheit e quantas temperaturas ficaram acima da media em Farenheit.
somaCelsius = 0
somaFaren = 0
listF = []


for i in range(0,5):
    temp = float(input('Temperatura em graus Celsius: '))
    somaCelsius += temp
    listF.append(temp*1.8+32)
    somaFaren += listF[i]

mediaCelsius = somaCelsius/5
mediaFaren = somaFaren/5

print('Média das temperaturas em Célsius: ',mediaCelsius)
print('Média das temperaturas em Farenheit: ',mediaFaren)

ListaAcimaF = []

for j in range(0,5):
    if listF[j] > mediaFaren:
        ListaAcimaF.append(listF[j])
print('Temperaturas acima da média em Farenhite', ListaAcimaF)


