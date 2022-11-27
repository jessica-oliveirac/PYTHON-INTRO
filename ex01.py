#1)Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.

N1=int(input('Digite um nº: '))
N2=int(input('Digite outro nº: '))

SOMA=N1+N2
print("Total: ", SOMA)

#2)Escreva um programa que converta uma temperatura digitasa em °C em °F. A fórmula para essa conversão é:
C=int(input("°C: "))
F=(9*C)/5+32
print("Convertido para °F: ", F)

#3)Escreva um programa que leia três números e que imprima o maior e o menor.

N1=int(input("Digite um nº: "))
N2=int(input("Digite outro nº: "))
N3=int(input("Digite mais um nº: "))

print('Maior Nº: ',max(N1,N2,N3))
print('Menor Nº: ', min(N1, N2, N3))
