import json

def main():
  arqIN = open("bdveiculos.txt","rt")
  arqOUT = open("saidaEXE8.json","wt")

  # Gerando o objeto JSON ..
  linha = arqIN.readline().strip()
  lst_veics = []

  while linha != "":
    dic_veic = {}
    dic_veic["placa"] = linha
    linha = arqIN.readline().strip()
    dic_veic["modelo"] = linha
    linha = arqIN.readline().strip()
    dic_veic["marca"] = linha
    linha = arqIN.readline().strip()
    dic_veic["km"] = linha

    lst_veics.append(dic_veic)

    linha = arqIN.readline().strip()
  # fim while

  # GERANDO O ARQUIVO JSON
  d = {"dados": lst_veics}

  json.dump(d,arqOUT,indent=4,sort_keys=True)
  arqOUT.close()

  print("Processamento concluído!!!")  
# fim main

main()    