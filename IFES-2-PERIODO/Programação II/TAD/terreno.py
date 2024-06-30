import tadretangulo as tret

def cria_lst_lotes(lt, ct, divl, divc, lr):
  # CALCULANDO LARG E COMP DE CADA LOTE
  larg_l = (lt - (divl + 1) * lr)/divl
  comp_l = (ct - (divc + 1) * lr)/divc

  # TODAS AS COORDENADAS DE ORIGEM DE LOTE FORAM TOMADAS
  # EM RELAÇÃO A COORDENADA DE ORIGEM DO TERRENO (0,0.)
  lst_lotes =[]
  
  for i in range(1,divc+1):
    for j in range(1,divl+1):
      lote = tret.cria_lh(j * lr + (j-1) * larg_l, i * lr + (i-1) * ct,larg_l,comp_l)
      lst_lotes.append(lote)

  return lst_lotes
# fim cria_lst_lotes  

def print_lista_lotes(lstlts):
  print("\n%s%7s%10s%12s%10s%9s%11s" % ("COD","X","Y","LARG.","COMP.","AREA","PERIM"))
  cont = 1
  for lote in lstlts:
    xy = tret.getES(lote)
    l = tret.getL(lote)
    c = tret.getA(lote)
    a = tret.area(lote)
    p = tret.perimetro(lote)
    print("%2d%10.2f%10.2f%10.2f%10.2f%10.2f%10.2f" % (cont,xy[0],xy[1],l,c,a,p))
    cont = cont + 1
  # for ..
# fim print_lista_lotes

def salva_lista_lotes(lst_lots,nomearq):
  arqout = open(nomearq,"wt")
  
  for i in range(len(lst_lots)-1):
    lote = lst_lots[i]
    es = tret.getES(lote)
    di = tret.getDI(lote)
    s = str(es[0]) +", " + str(es[1]) + ", " + str(di[0]) + ", " + str(di[1]) + "\n"
    arqout.write(s)
  # for ..

  lote = lst_lots[-1]
  es = tret.getES(lote)
  di = tret.getDI(lote)
  s = str(es[0]) +", " + str(es[1]) + ", " + str(di[0]) + ", " + str(di[1])
  arqout.write(s)
  
  arqout.close()
# fim salva_lista_lotes

def main():
  divs_l = 3
  divs_c = 4
  larg_rua = 2
  
  print("EXERCÍCIO TERRENOS E LOTES V. 1.0")
  print("=================================\n")
  larg_t = float(input("Entre com a largura do terreno: "))
  comp_t = float(input("Entre com o comprimento do terreno do terreno: "))

  lista_lotes = cria_lst_lotes(larg_t,comp_t,divs_l,divs_c,larg_rua)

  print_lista_lotes(lista_lotes)

  # GERANDO O ARQUIVO lotes.txt
  salva_lista_lotes(lista_lotes,"lotes.txt")

  print("Processamento concluido!!!")
# fim main

if __name__ == '__main__':
  main()