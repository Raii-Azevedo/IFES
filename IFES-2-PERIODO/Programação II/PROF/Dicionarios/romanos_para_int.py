# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# arquivo: romanos_para_int.py
# converte um valor em algarismos romanos para int (arábicos).
# Exercício de fixação de dicionários em Python.
#
# Data: 20/04/2023
# Ambiente: Replit
# Local: lab 205
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def romano_2_int(d,val_rom):
  lst = []
  subvalidos = [4,9,40,90,400,900]
  valint = 0

  for ro in val_rom:
    if ro not in d:
      return -1
    else:
      valint = d[ro]     # V-I,X-I,L-X,C-X,D-C,M-C 
      if lst == []:
        lst.append(valint)
      else:
        if lst[-1] >= valint:
          lst.append(valint)
        else: # lst[-1] < valint
          sub = valint - lst[-1]
          if sub in subvalidos:
            lst[-1] = sub       
          else:         
            return -1 # lst[-1] < valint mas a combinação 
                      # que gerou a subtração é inválida.
  # for ro

  soma = 0
  for n in lst:
    soma = soma + n

  return soma
# fim romano_2_int

def main():
  dicromanos = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
  numroman = input("Entre com um vlaor em números romanos: ").upper()
  emint = romano_2_int(dicromanos,numroman)

  if emint == -1:
    print("Valor romanos",numroman,"inválido!!!")
  else:
    print(numroman,"=",emint)
# fim main      

main()