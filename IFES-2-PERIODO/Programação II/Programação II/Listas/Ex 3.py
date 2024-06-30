print ('''3. Leitura: Dado um número n, faça uma função que leia n números inteiros, e retorne uma lista com esses números.''')
l = []
n = int (input ('Quantos números deseja salvar? '))

def Números():
    for c in range (1,n+1):
        num = int (input (f'Digite o {c}° número: '))
        l.append(num)
    print (l)


Números()