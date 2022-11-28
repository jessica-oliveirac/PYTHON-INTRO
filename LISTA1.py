#1)Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.

N1=int(input('Digite um nº: '))
N2=int(input('Digite outro nº: '))

SOMA=N1+N2
print("Total: ", SOMA)

-------------------------------------------------------------------------------------------------------------------
#2)Escreva um programa que converta uma temperatura digitasa em °C em °F. A fórmula para essa conversão é:
C=int(input("°C: "))
F=(9*C)/5+32
print("Convertido para °F: ", F)
-------------------------------------------------------------------------------------------------------------------
#3)Escreva um programa que leia três números e que imprima o maior e o menor.

N1=int(input("Digite um nº: "))
N2=int(input("Digite outro nº: "))
N3=int(input("Digite mais um nº: "))

print('Maior Nº: ',max(N1,N2,N3))
print('Menor Nº: ', min(N1, N2, N3))
-------------------------------------------------------------------------------------------------------------------
#4)Faça um programa que leia duas listas e que gere umma terceira com os elementos das duas primeiras
-------------------------------------------------------------------------------------------------------------------
# 5)Escreva uma função que retorne o maior de dois números.
# máximo(5, 6) == 6
# máximo(2, 1) == 2
# máximo(7, 7) == 7
print(max(5,6))
print(max(2,1))
print(max(7,7))
-------------------------------------------------------------------------------------------------------------------
#6)Converta as seguintes expressões matemáticas para que possam ser calculadas usando o interpretador Python.
#10+20x30
#42/30
#(94+2)x6-1
-------------------------------------------------------------------------------------------------------------------
#7)Escreva um programa que calcule a soma de três variáveis e imprima o resultado na tela.
n1=4
n2=20
n3=15
soma=n1+n2+n3
print("Soma: ", soma)
-------------------------------------------------------------------------------------------------------------------
#8)Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores que 7. 
#Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintees variáveis: matéria1, matéria2 e matéria3

materia1=8
materia2=5
materia3=7

media=(8+5+7)/3

if media>7:
    print("Aprovado")
else:
    print("Reprovado")
-------------------------------------------------------------------------------------------------------------------
#9)Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por diass e R$0,15 por km rodado.

km=int(input("Km: "))
dia=int(input("Dias: "))

valor=60*dia+0,15*km

print("Preço: ",valor)
