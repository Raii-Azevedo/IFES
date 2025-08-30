#  
# CONSTRUA UMA FUNÇÃO QUE RECEBE UMA STRING CONTENDO UM TEXTO QUALQUER
# E RETORNA UMA CONTAGEM DE TODAS AS PALAVRAS ENCONTRADAS NO TEXTO.
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
		print("%s,%d" % (lst_ps[i],lst_ctgs[i])) 
# fim print_tab_contagem

def main(args):
	doc = open(args[1],"rt").read()
	lst_biblia = separa_pals(doc)    
	
	lst_palavras = []
	lst_contagens = []
	
	for palavra in lst_biblia:
		if palavra.lower() not in lst_palavras:
			lst_palavras.append(palavra.lower())
			lst_contagens.append(1)
		else:
			indice = lst_palavras.index(palavra.lower())
			lst_contagens[indice] = lst_contagens[indice] + 1
	# for palavra ...
	
	print_tab_contagem(lst_palavras,lst_contagens)
	
	return 0
# main

main()

