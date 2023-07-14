def entrada(file):
    with open(f'{entrada}.txt', 'w') as file:
        file = input('Digite o texto dentrada do arquivo: ')

    return file

def main():
    origem = input('Digite o nome de arquivo de entrada: ')
    saida = input('Digite o nome do arquivo de saída: ')

    print(f'O arquivo de entrada é: {entrada(origem)}')
    
if __name__ == '__main__':
    main()