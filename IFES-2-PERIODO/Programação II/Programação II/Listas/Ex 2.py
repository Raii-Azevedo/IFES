print ('2. Metade: Faça um procedimento que leia 10 números digitados pelo usuário, armazene a metade de cada um deles numa lista, e depois imprima esta lista')
print ('')
l = []


def Metade():
    for c in range (10):
        n = float (input ('Digite um Nº: '))
        l.append(n/2)
    
    for n in l:
        print (n)



Metade()

