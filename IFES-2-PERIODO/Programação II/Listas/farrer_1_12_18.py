#
# Exercicio Farrer 1.12.18
# Rally Regularidade
#
# Data 14/02/2023
# Local: lab 205
# Autor: Ernani Ribeiro
#
def main(args):
	print("Farrer 1.12.18: O Problema do Rally\n")
	
	print("ENTRANDO COM OS TEMPOS PADRõES")
	tp1 = float(input("Entre com o tempo padrão 1: "))
	tp2 = float(input("Entre com o tempo padrão 2: "))
	tp3 = float(input("Entre com o tempo padrão 3: "))
	
	inscwinner = 0
	pontoswinner = 0
	
	print()
	print("ENTRANDO COM OS DADOS DAS EQUIPES")
	
	inscricao = input("Entre com o numero de inscrição da equipe:")
	
	while inscricao != "9999":
		te1 = float(input("Entre com o tempo etapa 1: "))
		te2 = float(input("Entre com o tempo etapa 2: "))
		te3 = float(input("Entre com o tempo etapa 3: "))
		
		pe1 = pontos1etapa(tp1,te1)
		pe2 = pontos1etapa(tp2,te2)
		pe3 = pontos1etapa(tp3,te3)
		totalpts = pe1 + pe2 + pe3
		
		print ("%s %10d %10d %10d %10d" % (inscricao,pe1,pe2,pe3,totalpts))
		
		if totalpts > pontoswinner:
			pontoswinner = totalpts
			inscwinner = inscricao	
		
		print()
		inscricao = input("Entre com o numero de inscrição da equipe:")		
	# fim while
	
	print("\nEQUIPE VENCEDORA")
	print("inscricao:",inscwinner)
	print("pontuação:",pontoswinner)
	
	return 0
# fim main


def pontos1etapa(tp,te):
	D = abs(tp - te)

	if D < 3:
		return 100
	elif (D >= 3 and D <= 5):
		return 80
	else:
		return 80 - (D - 5)/5
# fim pontos1etapa

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
