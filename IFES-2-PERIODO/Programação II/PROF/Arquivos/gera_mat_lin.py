import random


def main():
  arq = open("dadosmat.txt", "wt")

  for i in range(49):
    num = random.randint(1, 99)
    arq.write(str(num) + "\n")
  # for i..

  num = random.randint(1, 99)
  arq.write(str(num))

  arq.close()

  print("Matriz gerada com sucesso!!")


# fim main

main()
