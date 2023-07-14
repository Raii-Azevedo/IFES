#
# Exercicio de fixação: arquivos
# Exercicio 2: concatenação de 2 arquivos
#
# Data 24/03/2023
# Local: lab 205
# Autor: Ernani Ribeiro
#
def main(args):
  arq_in_1 = open("A.txt", "rt")
  arq_out = open("concatenado-2.txt", "at")

  linha = arq_in_1.readline()

  while linha != "":
    arq_out.write(linha)
    linha = arq_in_1.readline()
  # while ..

  arq_in_1.close()
  arq_out.close()

  arq_in_2 = open("B.txt", "rt")
  arq_out = open("concatenado-2.txt", "at")

  linha = arq_in_2.readline()

  while linha != "":
    arq_out.write(linha)
    linha = arq_in_2.readline()
  # while ..

  arq_in_2.close()
  arq_out.close()

  print("Concatenação concluida!!!")

  return 0


# main

if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))
