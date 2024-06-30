#
# Exercicio de fixação: arquivos
# Exercicio 3: matriz linear para matriz linha coluna.
#
# Data 28/03/2023
# Local: lab 205
# Autor: Ernani Ribeiro
#
def mat_para_str(m):
  s = ""
  for i in range(len(m)):
    for j in range(len(m[0])):
      s = s + ("%5d" % m[i][j])
    s = s + "\n"
  return s

def main():
  arqmat = open("dadosmat.txt", "rt")
  mat = []
  lstmat = []

  linha = arqmat.readline()

  cont = 0
  while linha != "":
    if cont == 10:
      mat.append(lstmat)
      cont = 1
      lstmat = []
    else:
      cont = cont + 1

    lstmat.append(int(linha.strip()))
    linha = arqmat.readline()
  # while ..

  mat.append(lstmat)

  arqmat.close()

  arqmat = open("mat5x10.txt", "wt")

  arqmat.write(mat_para_str(mat))

  arqmat.close()

# fim main

main()
