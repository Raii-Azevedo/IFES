print ('''11. Média: Faça um procedimento que leia um número n e depois a notas de n alunos (0 ≤ n ≤ 100). Em seguida, 
calcule e imprima a média da turma, e o número de alunos que ficaram com nota acima de 60.''')
def Média():
    s = na = 0
    n = int (input ('N° de alunos na turma: '))
    for c in range (n):
        nota = float (input ('Nota: '))
        s += nota
        if nota > 60:
            na += 1
    media = s/n
    print (f'Média da turma = {media}')
    print (f'Alunos com nota acima de 60 = {na}')

Média()
    