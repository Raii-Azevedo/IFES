print('''2. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa
lista a média de cada aluno. Ao final. imprima o número de alunos com média 
maior ou igual a 7.0\n''')

lst = []
aluno = 0

for i in range (10):
    print(f'Notas do {i+1}° aluno')
    nota1 = float(input('\nDigite a nota: '))
    nota2 = float(input('Digite a nota: '))
    nota3 =float(input('Digite a nota: '))
    nota4 = float(input('Digite a nota: '))
    
    media = (nota1 + nota2 + nota3 + nota4)/4

    lst.append(media)

print(f'Lista de médias: {lst}')

for i in range (len(lst)):
    if lst[i] >= 7.0:
        print(f'Média acima de 7: {lst[i]}')
        aluno += 1 
print(f'O N° de alunos com média acima de 7 é {aluno}')
