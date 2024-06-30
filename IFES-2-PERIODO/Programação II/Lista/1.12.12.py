print('''1.12.12. O sistema de avaliação de uma determinada disciplina obedece aos seguintes 
critérios:
- durante o semestre são dadas três notas;
- a nota final é obtida pela média aritmética das notas dadas durante o curso;
- é considerado aprovado o aluno que obtiver a nota final superior ou igual a 60 e que tiver 
comparecido a um mínimo de 40 aulas.
Fazer um algoritmo que:
a) Leia um conjunto de dados contendo o número de matrícula, as três notas e a frequência
(número de aulas frequentadas) de 100 alunos.
b) Calcule:
- a nota final de cada aluno;
- a maior e menor nota da turma;
- a nota média da turma;
- o total de alunos reprovados;
- a porcentagem de alunos reprovados por infrequência;
c) Escreva:
- para cada aluno, o número de matrícula, a frequência, a nota final e o código (aprovado ou 
reprovado);
- o que foi calculado no item b (2,3,4 e 5).\n''')


def main():
    print(' - BOLETIM ESCOLAR - \n')

    aluno = 0
    A = 'Aprovado'
    B = 'Reprovado'

    matricula = int (input(' Nº matrícula: '))
    while matricula !=0:
        frequencia = int(input(' Frequência: '))
        n1 = float(input('Nota 1: '))
        n2 = float(input('Nota 2: '))
        n3 = float(input('Nota 3: '))

        media = (n1+n2+n3)/3
        
        aluno += 1

        print(f'\nN° de alunos {aluno}')

        if frequencia >= 40:
            if media >= 60:
                print(f'\nMatricula: {matricula}\n Nota: {media:.2f}\n Situação: APROVADO\n')
            else:
                print(f'\nMatricula: {matricula}\n Nota: {media:.2f}\n Situação: REPROVADO por nota\n')
        else:
                print(f'\nMatricula: {matricula}\n Nota: {media:.2f}\n Situação: REPROVADO por Frequência\n')

        matricula = int (input(' Nº matrícula: '))

print('\nFinalizar esse exercício')
if __name__ == '__main__':
    main()
