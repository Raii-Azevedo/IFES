def area(ces,cdi):
  base = cdi[0] - ces[0]
  altura = ces[1] - cdi[1]
  return base * altura

def perimetro(ces,cdi):
  base = cdi[0] - ces[0]
  altura = ces[1] - cdi[1]
  return 2*base + 2*altura

def main():
  ca = (10,30)
  cb = (50,10)

  print("Teste: Area e perimetro")
  print(area(ca,cb))
  print(perimetro(ca,cb))

  print("MODULO",__name__)

if __name__ == "__main__":
  main()