from random import randint

def geraMat(quant_linhas, quant_colunas): # Gerar uma matriz com randint
    mat = []
    for i in range(quant_linhas):
        linha_mat = []
        for j in range(quant_colunas):
            linha_mat.append(randint(1, 99))
        mat.append(linha_mat)
    return mat

def printMat(mat):
    linhas = len(mat)
    colunas = len(mat[0])

    for i in range(linhas):
        for j in range(colunas):
            print('%4d' % mat[i][j], end='') 
        print()

    return mat

def salvaMat(nomearq, m):
    linhas = len(m)
    colunas = len(m[0])

    with open(f'{nomearq}.txt', 'wt') as file:
        for i in range(linhas):
            for j in range(colunas):
                file.write('%4d' % m[i][j])
            file.write('\n')
        
    file.close()

def main():
    nomearq = input('Digite o nome do arquivo: ')
    matriz = geraMat(5, 10)
    salvaMat(nomearq, matriz)

if __name__ == '__main__':
    main()
