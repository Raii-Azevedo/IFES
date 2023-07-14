import tadcirculo as tc

def main():
  raiocirc = float(input("Entre com o raio: "))
  coordx = float(input("Entre com a coord x do centro: "))
  coordy = float(input("Entre com a coord y do centro: "))

  c = tc.criar(raiocirc,coordx,coordy)

  print("Raio:",tc.getraio(c))
  print("Coordenada x do centro:",tc.getx(c))
  print("Coordenada y do centro:",tc.gety(c))

  print("Area:",tc.getarea(c))
  print("Perimetro:",tc.getperimetro(c))

main()