

N1=int(input("Digite um nº: "))
N2=int(input("Digite outro nº: "))
N3=int(input("Digite mais um nº: "))

if (N1>N2) and (N1>N3): 
    print ('Maior nº: ', N1)
    if (N2>N1) and (N3>N1):
        print ('Maior nº: ', N2)
        if (N3>N1 and N3>N2):
            print ('Maior nº: ', N3)

if (N1<N2) and (N1<N3):
    print('Menor nº: ', N1) 
    if (N2<N1) and (N3<N1):
        print('Menor nº: ', N2)
        if (N3<N1) and (N3<N2):
            print('Menor nº: ', N3)
        
