# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# arquivo: intparatxt.py
# converte um inteiro para a forma textual, com a descrição do valor.
# Exercício de fixação de dicionários em Python.
#
# Data: 13/04/2023
# Ambiente: Replit
# Local: lab 205
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def converte_2_txt(dicc,n):
  if n in dicc:
    return dicc[n]
  else:
    aux = n
    if n < 0:
      n = -1 * n
    
    dezena = n//10 * 10
    unidade = n % 10

    txtdezena = dicc[dezena]
    txtunidade = dicc[unidade]

    saida = ""

    if aux < 0:
      saida = "menos "

    saida = saida + txtdezena + " e " + txtunidade

    return saida
# fim converte_2_txt 

def main():
  d = { 0:"zero",1:"um",2:"dois",3:"três",4:"quatro",5:"cinco",6:"seis",7:"sete",\
        8:"oito",9:"nove",10:"dez",11:"onze",12:"doze",13:"treze",14:"quatorze",\
        15:"quinze",16:"dezesseis",17:"dezessete",18:"dezoito",19:"dezenove",20:"vinte",\
        30:"trinta",40:"quarenta",50:"cinquenta",60:"sessenta",70:"setenta",80:"oitenta",\
        90:"noventa"}
  
  num = int(input("Digite um número inteiro positivo: "))
  print(converte_2_txt(d,num))
# fim main

main()