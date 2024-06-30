#
# Exercicio de fixação: arquivos
# Exercicio 1: copia de arquivo.
#
# Data 24/03/2023
# Local: lab 205
# Autor: Ernani Ribeiro
#
def main(args):
  arq_in = open("arq-original.txt", "rt")
  arq_out = open("copia-2-arq-original", "wt")

  linha = arq_in.readline()

  while linha != "":
    arq_out.write(linha)
    linha = arq_in.readline()
  # while ..

  arq_in.close()
  arq_out.close()

  print("Cópia concluida!!!")

  return 0
# main

if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))
