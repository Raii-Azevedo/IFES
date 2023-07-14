#
# Exercicio de aplicação: arquivos
# Exercicio 4, lista 2: processamento bdveiculos.txt
#
# Data 31/03/2023
# Local: lab 205
# Autor: Ernani Ribeiro
#
def loadtab(nomearq):
  arq = open(nomearq, "rt")
  tabela = []

  placa = arq.readline()
  while placa != "":
    modelo = arq.readline()
    marca = arq.readline()
    km = arq.readline()
    lstveiculo = [placa.strip(), modelo.strip(), marca.strip(), km.strip()]
    tabela.append(lstveiculo)
    placa = arq.readline()
  # while

  arq.close()
  return tabela
# fim de loadtab

def filtro(tb, strmarca):
  nomearq = strmarca + ".txt"
  arq = open(nomearq, "wt")

  for veiculo in tb:
    if veiculo[2] == strmarca:
      linha = veiculo[0] + ", " + veiculo[1] + ", " + veiculo[2] + ", " + veiculo[3] + "\n"
      arq.write(linha)

  arq.close()

# fim filtro

def printtabela(tab):
  for veiculo in tab:
    print("%10s%20s%20s%10s" %
          (veiculo[0], veiculo[1], veiculo[2], veiculo[3]))
# fim printtabela

def main():
  tab = loadtab("bdveiculos.txt")

  filtro(tab, "FORD")
  filtro(tab, "TOYOTA")
  filtro(tab, "FIAT")

  print("Processamento concluído!!")

# fim main

main()