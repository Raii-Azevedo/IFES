#
# Exercicio Farrer 1.12.30
# Série MacLaurin
#
# Data 09/02/2023
# Local: lab 205
# Autor: Ernani Ribeiro
#
import math

def fatorial(n):
	if n in [0,1]:
		return 1
	
	fat = 1
	
	for f in range(1,n+1):
		fat = fat * f
	return float(fat)
# fim fatorial

def seno(A):
	A = math.radians(A)
	senoA = A - (A**3/fatorial(3)) + (A**5/fatorial(5)) - (A**7/fatorial(7))
	return senoA
# fim seno

def seno2(A,quanttermos):
	A = math.radians(A)
	y = 1
	sinal = 1
	senoA = 0
	for cont in range(quanttermos):
		termo = (A**y/fatorial(y)) * sinal
		senoA = senoA + termo
		y = y + 2
		sinal = sinal * -1
	# for cont ..
		
	return senoA
# fim seno

def main():
	for angulo in range(361):
		senopy = math.sin(math.radians(angulo))
		senoprog2 = seno2(angulo,8)
		dif = abs(senopy - senoprog2)		
		print("%3d%10.2f%10.2f%10.2f" % (angulo,senopy,senoprog2,dif))	
	# for angulo..	
# fim main

main()








