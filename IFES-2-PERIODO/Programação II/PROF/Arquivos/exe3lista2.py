#
# Exercicio de aplicação: arquivos
# Exercicio 3, lista 2: ips válidos/inválidos
#
# Data 30/03/2023
# Local: lab 205
# Autor: Ernani Ribeiro
#
def valida_ip(str_ip):
  lst = str_ip.split(".")
  if len(lst) != 4:
    return False

  for octeto in lst:
    if int(octeto) not in range(256):
      return False
  # for
  return True
# fim valida_ip

def main():
  lista_ips = []

  # Leitura dos ips
  arq = open("bdips.txt","rt")
  linha = arq.readline()
  while linha != "":
    lista_ips.append(linha.strip())
    linha = arq.readline()
  # while
  arq.close()

  # Separa ips válidos e inválidos.
  lista_val = []
  lista_inv = []

  for ip in lista_ips:
    if valida_ip(ip):
      lista_val.append(ip)
    else:
      lista_inv.append(ip)
  # for ip

  # Processando o arquivo de saída.
  arq = open("saidabdips.txt","wt")
  
  arq.write("[Endereços válidos:]\n")
  for ip in lista_val:
    arq.write(ip + "\n")

  arq.write("\n")

  arq.write("[Endereços inválidos:]\n")
  for ip in lista_inv:
    arq.write(ip + "\n")
  arq.close()
# fim main

main()