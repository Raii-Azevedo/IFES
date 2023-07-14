# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# arquivo: intparatxt.py
# converte um inteiro para a forma textual, com a descrição do valor.
# Exercício de fixação de dicionários em Python.
#
# Data: 13/04/2023
# Ambiente: Replit
# Local: lab 205
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def converte_2_txt(dicc, n):
  if n in dicc:
    return dicc[n]
  else:
    aux = n
    if n < 0:
      n = -1 * n

    dezena = n // 10 * 10
    unidade = n % 10

    txtdezena = dicc[dezena]
    txtunidade = dicc[unidade]

    saida = ""

    if aux < 0:
      saida = "menos "

    saida = saida + txtdezena + " e " + txtunidade

    return saida


# fim converte_2_txt


def converte_dec_para_txt(d, num):
  numtxt = str(num)
  lst = numtxt.split('.')

  txt_antes_do_ponto = converte_2_txt(d, int(lst[0]))

  if len(lst) == 1:
    return txt_antes_do_ponto
  else:
    aux = ""
    txt_depois_do_ponto = lst[1]
    for i in range(len(txt_depois_do_ponto)):
      if txt_depois_do_ponto[i] == '0':
        aux = aux + "zero "
      else:
        break
    # fim for i

    parte_dec_txt = converte_2_txt(d, int(lst[1]))

    return txt_antes_do_ponto + " ponto " + aux + parte_dec_txt
# fim converte_dec_para_txt


def main():
  d = { 0:"zero",1:"um",2:"dois",3:"três",4:"quatro",5:"cinco",6:"seis",7:"sete",\
        8:"oito",9:"nove",10:"dez",11:"onze",12:"doze",13:"treze",14:"quatorze",\
        15:"quinze",16:"dezesseis",17:"dezessete",18:"dezoito",19:"dezenove",20:"vinte",\
        30:"trinta",40:"quarenta",50:"cinquenta",60:"sessenta",70:"setenta",80:"oitenta",\
        90:"noventa"}

  num = float(input("Digite um número inteiro positivo: "))
  print(num)
  print(converte_dec_para_txt(d, num))
# fim main

main()
