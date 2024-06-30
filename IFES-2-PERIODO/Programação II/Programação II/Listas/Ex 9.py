print ('''9. Ordenadas e abscissas: Defina um procedimento que receba duas listas com a mesma quantidade de números inteiros. 
A primeira lista contém as abscissas de um conjunto de pontos, e a segunda contém as ordenadas desses mesmos pontos.
Calcule o número a de abscissas que são pares e o número b de ordenadas que são ı́mpares. Se a ≥ b, imprima a soma''')
l1 = []
l2 = []
lp = []
li = []
def abscissas():
    for c in range (5):
        a = int (input ('Digite as Abscissas: '))
        l1.append(a)
    print (f'Abscissas = {l1}')
    return l1

def ordenadas():
    for c in range(5):
        b = int (input ('Digite as Ordenadas: '))
        l2.append(b)
    print (f'Ordenadas = {l2}')
    return l2

def ParOuImpar():
    cont = 0
    for valor in l1:
        if valor % 2 ==0:
            cont +=1
            lp.append (valor)
    print (f'Abcissas com {cont} números pares = {lp}')

    ordenadas()
    cont = 0
    for valor in l2:
        if valor % 2 ==1:
            cont +=1
            li.append(valor)
    print (f'Ordenadas com {cont} números ímpares = {li}')

abscissas()
ordenadas
ParOuImpar()
if lp >= li:
    print (f'Soma das Abcissas = {sum(l1)}')
else:
    if li > lp:
        for produto in l2:
            produto *= produto
    print (f'Produto das Ordenadas = {produto}')