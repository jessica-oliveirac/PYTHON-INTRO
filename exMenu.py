N1=int(input("Digite um n°:"))
N2=int(input("Digite outro n°: "))

print("OPÇÕES: ")
print("1 - Soma(+)")
print("2 - Subtração(-)")
print("3 - Multiplicação(*)")
print("4 - Divisão(/)")

opcao=int(input("Digite o n° correspondente á opção ecolhida: "))

if opcao==1:
	conta=N1+N2
if opcao==2:
	conta=N1-N2
if opcao==3:
	conta=N1*N2
if opcao==4:
	conta=N1/N2

print("Resultado: ", conta)
