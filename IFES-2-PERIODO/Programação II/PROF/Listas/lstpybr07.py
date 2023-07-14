#
# Exercicio 7 Lista PythonBr
#
# Data 28/02/2023
# Local: lab 205
# Autor: Ernani Ribeiro
#
# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um
# crime. As perguntas são:
#
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
#
# O programa deve no final emitir uma classificação sobre a participação da pessoa no
# crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada
# como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, 
# ele será classificado como "Inocente".
#

def main(args):
	lstperguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?",
	                "Devia para a vítima?", "Já trabalhou com a vítima?"]
	lstrespostas = []
	                
	for pergunta in lstperguntas: # iterator
		resposta = input(pergunta + " (sim/não): ")
		lstrespostas.append(resposta)
	# for pergunta ..
	
	lstveredicto = ["Inocente!","Inocente!","Suspeito!","Cúmplice!","Cúmplice!","Assassino!"]
	
	contsim = 0
	
	for i in range(len(lstrespostas)): # indexado
		if lstrespostas[i] == "Sim":
			contsim = contsim + 1
			
	print("\n",lstveredicto[contsim])	
	
	return 0
# fim 

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))






