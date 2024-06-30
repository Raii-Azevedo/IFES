print ('''8. Fibonacci: Dado um número n, retorne uma lista com os n primeiros elementos da sequência de Fibonacci. 
Obs.: Cada elemento da sequência é obtido através da soma dos dois elementos anteriores:''')

def fibonacci():
    n = int (input ('Quantos elementos deseja mostrar? '))
    t1 = 0
    t2 = 1
    print (f'{t1} - {t2}',end= '')
    cont = 2
    while cont < n:
        t3 = t1 + t2
        print (f' - {t3}',end = '')
        t1 = t2
        t2 = t3
        cont += 1

fibonacci()
