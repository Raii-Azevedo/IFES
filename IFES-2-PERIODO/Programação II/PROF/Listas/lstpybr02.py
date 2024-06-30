#
# Exercicio 2 Lista PythonBr
#
# Data 28/02/2023
# Local: lab 205
# Autor: Ernani Ribeiro
#
# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa
# lista a média de cada aluno. Ao final, imprima o número de alunos com média
# maior ou igual a 7.0.
#
def main(args):
	lstmedias = []
	
	for i in range(5):
		nota1 = float(input("Entre com a nota 1 do aluno %d: " % (i+1)))
		nota2 = float(input("Entre com a nota 2 do aluno %d: " % (i+1)))
		nota3 = float(input("Entre com a nota 3 do aluno %d: " % (i+1)))
		nota4 = float(input("Entre com a nota 4 do aluno %d: " % (i+1)))
		
		media = (nota1 + nota2 + nota3 + nota4)/4
		lstmedias.append(media)		
		
		print()
	# for i ..
	
	cont = 0
	
	for i in range(len(lstmedias)):
		if lstmedias[i] >= 7:
			cont = cont + 1

	print("A quantidade de notas >= a média 7 é %d" % cont)
	
	return 0
# fim main

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
















