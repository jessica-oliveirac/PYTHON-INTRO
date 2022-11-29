#1 -Qual a saída do seguinte código?
valueOne = 5**2
valueTwo = 5**3
print(valueOne)    #25
print(valueTwo)    #125
----------------------------------------------------------------------------
#2 - Qual é a saída do seguinte código?
salary=8000
def printSalary():
    salary = 12000
    print("Salary:",salary)   #Salary: 12000
printSalary()
print("Salary:", salary)      #Salary: 8000
----------------------------------------------------------------------------
#3 - Podemos usar o bloco "else" para for loop?
for i in range(1,5):
    print(i)
else:
    print("this is else block statement")
#SAÍDA
1
2
3
4
this is else block statement
---------------------------------------------------------------------------
#4 - Qual o valor de x  após a execução do trecho de código abaixo?
x=0
while x < 10:
    x = x+1
print(x)

#SAÍDA 
10
--------------------------------------------------------------
#5 - Faça um programa que leia um vetor de 5 números inteiros e mostre-os
valores =[]
for x  in range(0,5):
    valores.append(int(input("Entre com o nº: ")))
print(valores)
#SAÍDA
Entre com o nº: 20
Entre com o nº: 4
Entre com o nº: 8
Entre com o nº: 9
Entre com o nº: 7
[20, 4, 8, 9, 7]
---------------------------------------------------------------------------
#6 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
valor=int(input("Digite uma nota entre 0 e 10: "))
while(valor<0) or (valor>10):
        valor=int(input("Informe um valor válido: "))
print("Valor válido!: ", valor)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#7 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
num=int(input("Digite um nº: "))
if num>0:
    print("Valor positivo!")
else:
    print("Valor Negativo!")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#8 - Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
letra=input("Nome: ")
for i in letra:
    print(i)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#9 - Converta as seguintes expressões matemáticas para que possam ser calculadas usando o interpretador Python. 10 + 20 x 3042/30(94+2) x 6 - 1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#10 - Defina uma função recursiva que calcule o maior divisor comum (M.D.C.) entre dois números a e b, em que a>b.
