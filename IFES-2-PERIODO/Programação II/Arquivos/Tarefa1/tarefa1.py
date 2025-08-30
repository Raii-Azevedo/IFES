def loadmat(nomearq):
  arq = open(nomearq,"rt")

  lstmat = []
  linha = arq.readline()

  while linha != "":
    lst = linha.split()
    for i in range(len(lst)):
      lst[i] = int(lst[i])
    lstmat.append(lst)
    linha = arq.readline()
  # while
  arq.close()

  return lstmat
# fim loadmat

def somamat(ma,mb):
  linhas = len(ma)
  colunas = len(ma[0])
  ms = []

  for i in range(linhas):
    lst_linha_ms = []
    for j in range(colunas):
      soma = ma[i][j] + mb[i][j]
      lst_linha_ms.append(soma)

    ms.append(lst_linha_ms)
  # fim for i
  return ms
# fim somamat

def salvamat(nomearq,mat):
  arq = open(nomearq,"wt")

  linhas = len(mat)
  colunas = len(mat[0])
  
  for i in range(linhas):
    for j in range(colunas):
      arq.write("%4d" % mat[i][j])
    arq.write("\n")

  arq.close()
# fim salvamat

def main():
  A = loadmat("matA5x10.txt")
  B = loadmat("matB5x10.txt")
  S = somamat(A,B)
  salvamat("matS.txt",S)
# fim main

main()