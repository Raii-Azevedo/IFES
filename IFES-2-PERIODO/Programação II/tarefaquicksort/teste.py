from modquicksort import quickr, quicknr

def carregabd(nomearq):
  arqin = open(nomearq, "rt")
  lst = []
  
  linha = arqin.readline().strip()

  while linha != "":
    dj = {}
    dj["placa"] = linha
    
    linha = arqin.readline().strip()
    dj["modelo"] = linha
    
    linha = arqin.readline().strip()
    dj["marca"] = linha
    
    linha = arqin.readline().strip()
    dj["km"] = linha
    
    linha = arqin.readline().strip()
    dj["cor"] = linha
    
    linha = arqin.readline().strip()
    dj["combustivel"] = linha

    lst.append(dj)

    linha = arqin.readline().strip()

  return lst
# fim carregabd


# fim arq_para_json

def salvaArq(arqnome,abrirbd):
  lerarq = open(arqnome,"wt")
  for info in abrirbd:
    linha = (f'{info["placa"]},{info["modelo"]},{info["marca"]},{info["km"]},{info["cor"]},{info["combustivel"]}\n')
    lerarq.write(linha)
	
  lerarq.close()
  #fechar arquivo

def main():
  nomearq = "bdveiculos2.txt"
  abrirbd = carregabd(nomearq)
  print(abrirbd)

  # Recursivo
  arqnome = "quickr-out.txt"
  quickRec = quickr(abrirbd)
  salvaArq(arqnome, quickRec)

  # Não Recursivo
  arqnome = "quicknr-out.txt"
  quickNRec = quicknr(abrirbd)
  salvaArq(arqnome, quickNRec)


# fim main

main()    