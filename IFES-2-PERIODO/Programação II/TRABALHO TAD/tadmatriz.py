def transposta(matT):
    matTrans = []
    for i in range(len(matT[0])):
        matTrans.append(len(matT) * [0])

    for i in range(len(matT)):
        for j in range(len(matT[0])):
            matTrans[j][i] = matT[i][j]
    return matTrans

def carregamat(arquivo):
    with open(f'{arquivo}.txt', 'r') as arq:
        mat = []
        linhas = arq.readline()
        while linhas != '':
            linha = linhas.split()
            for i in range(len(linha)):
                linha[i] = int(linha[i])
            mat.append(linha)
            linhas = arq.readline()
    return mat

def salvamat(file, arquivo):
    if arquivo is None:
        with open(f'{file}.txt', 'w', encoding='utf-8') as arq:
            arq.write('Operação impossível de realizar')
        return None

    with open(f'{file}.txt', 'w', encoding='utf-8') as arq:
        for i in range(len(arquivo)):
            for j in range(len(arquivo[0])):
                num = arquivo[i][j]
                num = str(num) + " "
                arq.write(num)
            arq.write('\n')
    return arquivo

def somaMat(matA, matB):
    if len(matA) == len(matB) and len(matA[0]) == len(matB[0]):
        soma = []
        for i in range(len(matA)):
            linha = []
            for j in range(len(matA[0])):
                linha.append(matA[i][j] + matB[i][j])
            soma.append(linha)
        return soma
    else:
        return None


def multi(matA, matB):
    if len(matA[0]) != len(matB):
        return None
    else:
        multiplicacao = []
        for i in range(len(matA)):
            linha = []
            for j in range(len(matB[0])):
                soma = 0
                for k in range(len(matA[0])):
                    soma += matA[i][k] * matB[k][j]
                linha.append(soma)
            multiplicacao.append(linha)
        return multiplicacao


def negativa(matN):
    for i in range(len(matN)):
        for j in range(len(matN[i])):
            matN[i][j] = -matN[i][j]
    return matN

def subMat(matA, matB):
    if len(matA) == len(matB) and len(matA[0]) == len(matB[0]):
        subtracao = []
        for i in range(len(matA)):
            linha = []
            for j in range(len(matA[0])):
                linha.append(matA[i][j] - matB[i][j])
            subtracao.append(linha)
        return subtracao
    else:
        return None


