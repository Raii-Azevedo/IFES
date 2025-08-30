def carregatxt(texto):
    with open ('Entrada.txt', 'rt') as file:
        linha = file.readline()

        while linha != '':
            texto.append(linha)
            linha = file.readline()

def main():
    texto = []

    print(texto)

if __name__ == '__main__':
    main()