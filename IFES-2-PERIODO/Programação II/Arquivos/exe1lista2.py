#
# Exercicio de aplicação: arquivos
# Exercicio 1, lista 2: remoção de acentos
#
# Data 06/04/2023
# Local: lab 205
# Autor: Ernani Ribeiro
#
def sem_acentos(tab,t):
  novo = ""
  for i in range(len(t)):
    # procurar a letra acentuada na tabela:
    j = 0
    while (j < len(tab)) and (t[i] != tab[j][0]):
        j = j + 1
    # fim while j
    
    # verdadeiro quando a letra txt[i] é um acentuado em tab_ac_nac[j][0].
    if j < len(tab):
      novo = novo + tab[j][1]
    else:
      novo = novo + t[i]
  # for i ..

  return novo
# fim sem_acentos

def main():
  tab_ac_nac = [['á','a'],['à','a'],['â','a'],['ã','a'],['é','e'],['ê','e'],['í','i'],['ó','o'],['ô','o'],['õ','o'],['ú','u'],['ü','u'],['ç','c']]

  txt = "g"
  novo = sem_acentos(tab_ac_nac,txt)
  
  print(txt)
  print(novo)
# fim main

main()