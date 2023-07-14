print('''5. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine 
quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.\n''')

lst = []
tp = ()

for i in range(10):
    print(f'\nDados do {i+1}º aluno')
    idade = int(input('Digite a idade: '))
    altura = float(input('Digite a altura: '))

    tp = (idade, altura)

    lst.append(tp)
# Calculo Média de altura
soma = 0
for i in range(len(lst)):
    soma = soma + (lst[i][1])
media = soma/10

# Calculo de idade e média
aluno = 0
for i in range(len(lst)):
    if lst[i][1] < media and lst[i][0] > 13:
        aluno +=1

print(f'\nLista de dados: {lst}')
print(f'Média altura: {media:.2f}')
print(f'O n° de alunos acima de 13 com altura menor que a média é: {aluno}')
