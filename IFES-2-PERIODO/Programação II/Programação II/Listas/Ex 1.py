print ('''1. Regressiva: Faça uma função que crie e retorne uma lista com todos os números pares de 1 a 100, porém na ordem regressiva.''')
def Pares ():
    l = []
    for c in range (100, 0, -2):
        if c%2 == 0:
            l.append (c)
    print (l)
   

Pares()



