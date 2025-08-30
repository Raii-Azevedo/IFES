# Constroi um dicionário com chave composta cep/rua.
import json

def main():
  arqcep = open("./bdcepsruas.txt", "rt")
  linha = arqcep.readline().strip()

  dicceps = {}

  while linha != "":
    lst = linha.split(",")
    cep = lst[2].strip()
    num = int(lst[1].split()[-1].strip())
    t = (cep, num)
    dicceps[t] = [lst[0], lst[3], lst[4], lst[5]]
    linha = arqcep.readline().strip()
  # fim while

  arqcep.close()

  client_JSON = json.dumps(dicceps)

  print(client_JSON)

#  for k in dicceps.keys():
#    print(k," * ",dicceps[k])
# fim main

main()
