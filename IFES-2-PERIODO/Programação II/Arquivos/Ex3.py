def mat_para_str(m): # Função parar transformar os N de dadosmat em uma string formarada para matriz
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
    if cont == 10: # Função para contar 10 elementos em cada linha
      mat.append(lstmat)
      cont = 1
      lstmat = []
    else:
      cont = cont + 1

    lstmat.append(int(linha.strip())) 
    linha = arqmat.readline()


  mat.append(lstmat)

  arqmat.close()

  arqmat = open("mat5x10.txt", "wt")

  arqmat.write(mat_para_str(mat))

  arqmat.close()


if __name__ == '__main__':
    main()
