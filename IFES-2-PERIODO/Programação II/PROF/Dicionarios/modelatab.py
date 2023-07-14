# Modela o base de dados de ceps e ruas como uma lista de dicionarios tipo registro.
def main():
  arqcep = open("./bdcepsruas.txt", "rt")
  linha = arqcep.readline().strip()

  lstdicceps = []

  while linha != "":
    lst = linha.split(",")
    d = {"logradouro":lst[0],"num":lst[1],"cep":lst[2],"bairro":lst[3],"muni":lst[4],"uf":lst[5]}
    lstdicceps.append(d)
    linha = arqcep.readline().strip()
  # fim while

  arqcep.close()

#  for di in lstdicceps:
#    print(di)
# fim main

main()