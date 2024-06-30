#  
# CONSTRUA UMA FUNÇÃO QUE RECEBE UMA STRING CONTENDO UM TEXTO QUALQUER
# E RETORNA UMA LISTA DAS PALAVRAS ENCONTRADAS NO TEXTO.
#
def remove_repetidas(lst):
	lst_sr = []
	for palavra in lst:
		if not palavra.lower() in lst_sr:
			lst_sr.append(palavra.lower())
	return lst_sr
# fim remove_repetidas

def faxina(palavra):
	# Faxina no final da palavra
	while (palavra != "") and (not palavra[-1].isalnum()):
		palavra = palavra[:-1]	
		
	# Faxina no inicio da palavra
	if len(palavra) > 0:
		while not palavra[0].isalnum():
			palavra = palavra[1:]
		
	return palavra
# fim de faxina

def separa_pals(txt):
	lst = txt.split() # Assume que o separador é o espaço, 1 caractere espaço.
	
	for i in range(len(lst)):
		if len(lst[i]) != 0:
			lst[i] = faxina(lst[i])
	
	return lst
# fim separa_pals
	
def print_lst_palavras(lista):
	for palavra in lista:
		print(palavra)
# fim print_lst_palavras

def main(args):
	s = open("biblia-em-txt-conv.txt","rt").read()
    
	lst_palavras = remove_repetidas(separa_pals(s))      
	
	# print_lst_palavras(lst_palavras)
	
	print("\nForam encontradas",len(lst_palavras),"palavras na lista.")
	
	return 0
# main

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
