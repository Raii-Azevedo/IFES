print ('4. Ocorrências: Dada uma lista e um elemento, retorne o número de ocorrências do elemento na lista.')
def ocorrencias (x, l):
    n = 0
    for elem in l:
        if elem == x:
            n += 1
        return n

        
l = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 4, 3, 3, 3, 2, 1]
print ( ocorrencias (3, l))
