def matriz(soma): # Função que recebe matriz(lista) e escreve num arquivo
    saida = input('\nDigite o nome de arquivo de saída: ')
    with open(f'{saida}.txt', 'wt') as file:
        s = ""
        for i in range(len(soma)): # Laço que transforma a lista no formato de matriz
            for j in range(len(soma[0])):
                s = s + ("%5d" % soma[i][j])
            s = s + "\n"
        file.write(s)

    file.close()
    

def somaMat(ma,mb):
    linhas = len(ma)
    colunas = len(ma[0])  

    soma = [[0] * colunas for linha in range(linhas)] # Soma recebe [0] que multiplica o número de colunas para cada linha em len de linha

    for i in range(linhas):
        for j in range(colunas): # Laço para soma de duas listas em esquema de matriz
            soma[i][j] = ma[i][j] + mb[i][j]
    return soma


def loadmat(nomearq, arquivo):
    # Leitura do Arquivo
    ma = []
    mb = []

    arq = open(f'{nomearq}.txt', "rt")
    linha = arq.readline()

    while linha != '':
        valores = linha.strip().split()
        if nomearq == arquivo[0]:
            ma.append([int(valor) for valor in valores]) # Transformar em INT cada valor no laço for de valor em valores
            linha = arq.readline()
        else:
            mb.append([int(valor) for valor in valores])
            linha = arq.readline()

    arq.close()

    return ma, mb


def main():
    ma = []
    mb = []

    print('PROCESSAMENTO DE MATRIZ')
    arquivo = []
    quant = int(input('\nQuantas matrizes irá somar? '))

    # Loop para leitura de matrizes
    for i in range(quant):
        nomearq = input(f'\nDigite o nome do {i+1}º arquivo para leitura: ')
        arquivo.append(nomearq)
        ma_arq, mb_arq = loadmat(nomearq, arquivo)
        ma += ma_arq
        mb += mb_arq

    soma = somaMat(ma, mb)

    matriz(soma)

    print('\nPROCESSAMENTO CONCLUÍDO')

    

if __name__ == '__main__':
    main()
