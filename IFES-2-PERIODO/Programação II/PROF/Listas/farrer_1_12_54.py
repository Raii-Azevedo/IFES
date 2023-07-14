#
# Exercicio Farrer 1.12.54, 
# Método aprox Newton p\ raiz quadrada.
#
# Data 17/02/2023
# Local: lab 205
# Autor: Ernani Ribeiro
#

def raiznewton(Y,aprox):
	x = Y/2
	
	for i in range(aprox):
		x = (x**2 + Y)/(2 * x)
	
	return x
# fim raiz newton

def main(args):
	for i in range(1,51):
		raizpy = i ** 0.5
		raiznw = raiznewton(i,10)
		dif = abs(raizpy - raiznw)
		print("%2d%10.3f%10.3f%14.5f" % (i,raizpy,raiznw,dif))
	# fim for ..
		
	return 0
# fim main

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
