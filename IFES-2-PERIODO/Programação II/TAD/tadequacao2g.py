# CONSTRUA UM TAD PARA REPRESENTAR UM TIPO DE DADO CHAMADO EQUACAO DO SEGUNDO GRAU. O # TAD DEVERÁ POSSUI A SEGUINTE INTERFACE (CONJUNTO DE FUNCOES):

# criar(a,b,c) // deve retornar uma estrutura de dados com a , b e c
# quantraizes(<variavel tad eq 2o grau>): int quantas raizes possui a equacao.
# getraiz1(<variavel tad eq 2o grau>): retorna o valor da raiz 1.
# getraiz2(<variavel tad eq 2o grau>): retorna o valor da raiz 2.
# geta(<variavel tad eq 2o grau>): retorna o coeficiente a.
# getb(<variavel tad eq 2o grau>): retorna o coeficiente b.
# getc(<variavel tad eq 2o grau>): retorna o coeficiente c.
# gety(<variavel tad eq 2o grau>,val x): retorna o valor da equacao.
def criar(ca,cb,cc):
  lst = [ca,cb,cc]
  delta = lst[1]**2 - 4 * lst[0] * lst[2]
  lst.append(delta)
  return lst

def geta(eq2g):
  return eq2g[0]
  
def getb(eq2g):
  return eq2g[1]
  
def getc(eq2g):
  return eq2g[2]

def gety(eq2g,valor_x):
  return eq2g[0] * valor_x**2 + eq2g[1] * valor_x + eq2g[2]

def getdelta(eq2g):
  return eq2g[3]

def quant_raizes(eq2g):
  delta = eq2g[-1] #eq2g[1]**2 - 4 * eq2g[0] * eq2g[2]
  if delta > 0:
    return 2
  elif delta == 0:
    return 1
  else:
    return 0
    
def getraiz_1(eq2g):
  delta = eq2g[-1] #eq2g[1]**2 - 4 * eq2g[0] * eq2g[2]
  raiz = (-eq2g[1] + delta**0.5)/(2 * eq2g[0])
  return raiz

def getraiz_2(eq2g):
  delta = eq2g[-1] #eq2g[1]**2 - 4 * eq2g[0] * eq2g[2]
  raiz = (-eq2g[1] - delta**0.5)/(2 * eq2g[0])
  return raiz

def tostr(eq2g):
  s = str(eq2g[0]) + "X2"
  if eq2g[1] > 0:
    s = s + " + " + str(eq2g[1]) + "X"
  elif eq2g[1] < 0:
    s = s + " - " + str(abs(eq2g[1])) + "X"

  if eq2g[2] != 0:
    if eq2g[2] > 0:
      s = s + " + " + str(eq2g[2])
    else:
      s = s + " - " + str(abs(eq2g[2]))

  return s