#9)Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por diass e R$0,15 por km rodado.

km=int(input("Km: "))
dia=int(input("Dias: "))

valor=60*dia+0,15*km

print("Preço: ",valor)
