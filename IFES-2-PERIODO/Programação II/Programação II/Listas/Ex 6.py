print ('6. Posição do Máximo: Dada uma lista de números, faça uma função que encontre e retorne o ı́ndice do maior deles.')
l = []
def maximo():
    x = 1
    while x != 0:
        x = int(input('Digite um número: '))
        l.append(x)
    return l


maximo()
print (l)
print (f'O maior número digitado foi {max(l)}')

