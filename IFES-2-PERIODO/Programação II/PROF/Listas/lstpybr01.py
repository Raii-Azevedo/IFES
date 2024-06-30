#
# Exercicio 1 Lista PythonBr
#
# Data 24/02/2023
# Local: lab 205
# Autor: Ernani Ribeiro
#
# Faça um Programa que leia 20 números inteiros e armazene-os em uma lista. Após a
# leitura, percorra a lista original e armazene os números PARES em uma segunda
# lista e os números IMPARES em uma terceira lista. Ao final imprima as três listas.

def main(args):
	QUANT = 7
	
	lst = []
	for i in range(QUANT):
		num = int(input("Entre com um inteiro:"))
		lst.append(num)
	# for i ..
	
	lstpares = []
	lstimpares = []
	
	# forma indexada
	for i in range(QUANT):
		if lst[i]%2 == 0:
			lstpares.append(lst[i])
		else:
			lstimpares.append(lst[i])
		
#	print(lst)
#	print(lstpares)
#	print(lstimpares)
	
	print("-" * 30)
	
	for k in range(QUANT):
		print("%5d" % lst[k],end="")
		if k < len(lstpares):
			print("%5d" % lstpares[k],end="")
		if k < len(lstimpares):
			print("%5d" % lstimpares[k],end="")
		print()
	# for k 
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
