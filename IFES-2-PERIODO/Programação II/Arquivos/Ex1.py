def main():
    origem = input('Digite o nome de arquivo de entrada: ')

    file = open(f'{origem}.txt', 'wt')
    
    texto = str(input('Digite o texto dentrada do arquivo: '))

    file.write(texto)

    file.close()

    saida = input('Digite o nome do arquivo de saída: ')

    doc = open(f'{origem}.txt', 'rt')

    linha = doc.readline()

    while linha != '':
        txt = open(f'{saida}.txt', 'wt')
        txt.write(linha)

    txt.close()

    print(f'O arquivo de entrada é: {origem}')

    print(f'O arquivo de saída é: {saida}')
    
if __name__ == '__main__':
    main()