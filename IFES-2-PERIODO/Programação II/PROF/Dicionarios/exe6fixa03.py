import json

def linha_to_dic(linha_arq):
  lst = linha_arq.split(",")
  diccpruas = {
    "logradouro": lst[0].strip(),
    "numero": lst[1].strip(),
    "cep": lst[2].strip(),
    "bairro": lst[3].strip(),
    "municipio": lst[4].strip(),
    "uf": lst[5].strip()
  }
  return diccpruas
# fim linha_to_dic

def main():
  arqcepsruas = open("bdcepsruas.txt", "rt")
  linha = arqcepsruas.readline().strip()

  lst = []

  while linha != "":
    dic = linha_to_dic(linha)
    lst.append(dic)
    linha = arqcepsruas.readline().strip()
  # while ..
  arqcepsruas.close()

  dic = {"dados": lst}

  arqout = open("saida.json","wt")
  json.dump(dic,arqout)
  arqout.close()
# fim main

main()