#  
# CONSTRUA UMA FUNÇÃO QUE RECEBE UMA STRING CONTENDO UM TEXTO QUALQUER
# E RETORNA UMA CONTAGEM DE TODAS AS PALAVRAS ENCONTRADAS NO TEXTO.
#
#
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
	lst = txt.split() # assume que o separador é o espaço, 1 caractere espaço.
	
	for i in range(len(lst)):
		if len(lst[i]) != 0:
			lst[i] = faxina(lst[i])
	
	return lst
# fim separa_pals
	
def print_tab_contagem(lst_ps,lst_ctgs):
	for i in range(len(lst_ps)):
		print("%50s%8d" % (lst_ps[i],lst_ctgs[i])) 
# fim print_tab_contagem

def main(args):
	doc = open("biblia-em-txt-conv.txt","rt").read()
	lst_biblia = separa_pals(doc)    
	
	lst_palavras = []
	lst_contagens = []
	
	for palavra in lst_biblia:
		if lst_palavras != []:
			indice = lst_palavras.index(palavra.lower())
		else:
			indice = -1
		
		if indice == -1:
			lst_palavras.append(palavra.lower())
			lst_contagens.append(1)
		else:
			lst_contagens[indice] = lst_contagens[indice] + 1
	# for palavra ...
	
	#print_tab_contagem(lst_palavras,lst_contagens)
	
	index_jesus = lst_palavras.index("jesus")	
	index_diabo = lst_palavras.index("diabo")	
	
	print("Jesus apareceu",lst_contagens[index_jesus],"vezes.")
	print("Diabo apareceu",lst_contagens[index_diabo],"vezes.")
	
#	print("\nForam encontradas um total de",len(lst_biblia),"palavras.")
	
	return 0
# main

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))











