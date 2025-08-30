print ('5. Máximo: Dada uma lista de números, faça uma função que encontre e retorne o maior deles.')
def maior(l):
    maior = l[0]
    for elem in l:
        if elem > maior :
            maior = elem
    return maior

l = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 4, 3, 3, 3, 2, 1]
print (maior(l))