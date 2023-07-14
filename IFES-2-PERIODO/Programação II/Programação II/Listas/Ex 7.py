print ('7. Inverter: Dada uma lista, faça um procedimento que inverta a ordem de seus elementos')
l = []
def inversão():
    for c in range (10):
        n = int (input('Digite um n°: '))
        l.append(n)
    print (l)
    l.reverse()
    print (f'Elementos invertidos = {l}')
    

inversão()
