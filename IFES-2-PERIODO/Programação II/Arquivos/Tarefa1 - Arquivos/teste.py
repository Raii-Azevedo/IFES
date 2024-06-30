def somaMat(ma,mb):
    linhas = len(ma)
    colunas = len(ma[0])  

    soma = [[0] * colunas for _ in range(linhas)]

    for i in range(linhas):
        for j in range(colunas):
            soma[i][j] = ma[i][j] + mb[i][j]

    return soma



def loadmat(nomearq):
    with open(f'{nomearq}.txt', "r") as arq:
        matrix = []
        for linha in arq:
            matrix.append([int(valor) for valor in linha.strip().split()])
        return matrix

def main():
    print('PROCESSAMENTO DE MATRIZ')
    quant = int(input('\nQuantas matrizes irá somar? '))

    # Loop para leitura de matrizes
    ma = []
    mb = []
    for i in range(quant):
        nomearq = input('\nDigite o nome do arquivo para leitura: ')
        ma_arq = loadmat(nomearq)
        mb_arq = loadmat(nomearq)
        ma += ma_arq
        mb += mb_arq

    soma = somaMat(ma, mb)

    print(soma)
    
if __name__ == '__main__':
    main()
