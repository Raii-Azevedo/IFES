#
# Exercicio de aplicação: arquivos
# Exercicio 1, lista 2: remoção de acentos
#
# Data 06/04/2023
# Local: lab 205
# Autor: Ernani Ribeiro
#
def sem_acentos(lac,lnac,t):
  novo = ""
  for i in range(len(t)):
    if t[i] in lac:
      pos = lac.index(t[i])
      novo = novo + lnac[pos]
    else:
      novo = novo + t[i]
  # for i ..
  return novo
# fim sem_acentos

def main():
  lst_ac =  ['á','à','â','ã','é','ê','í','ó','ô','õ','ú','ü','ç']
  lst_nac = ['a','a','a','a','e','e','i','o','o','o','u','u','c']

  d = {'cvrd':'companhia ','bb':'banco do brasil'}

  txt = "abóbora paçoca amor mãe páscoa você."
  novo = sem_acentos(lst_ac,lst_nac,txt)
  
  print(txt)
  print(novo)
# fim main

main()