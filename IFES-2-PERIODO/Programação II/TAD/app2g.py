import tadequacao2g as teq2g

def main():
  print("ENTRE COM O VALOR DOS COEFICIENTES DA EQUAÇÃO 2o GRAU")
  a = float(input("Coeficiente a: "))
  b = float(input("Coeficiente b: "))
  c = float(input("Coeficiente c: "))

  eq = teq2g.criar(a,b,c) # O TYPE DE eq É tadequacao2g
  quant = teq2g.quant_raizes(eq)

  print("\nEquacao",teq2g.tostr(eq),"possui",quant,"raízes reais:")

  if quant == 1:
    print("Raiz:",teq2g.getraiz_1(eq))
  elif quant == 2:
    print("Raiz 1:",teq2g.getraiz_1(eq))
    print("Raiz 2:",teq2g.getraiz_2(eq))
  else:
    print("\nEquacao não possui raízes reais!!")

  print("\nVALOR DA EQUAÇÃO NO PONTO X")
  x = float(input("Entre com o valor de x: "))
  print("Valor da equação",teq2g.tostr(eq),"no ponto x =",x,"é y =",teq2g.gety(eq,x))
# fim main
