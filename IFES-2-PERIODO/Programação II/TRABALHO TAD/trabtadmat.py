from tadmatriz import carregamat, somaMat, subMat, multi, negativa, salvamat, transposta

def main():
    arq = open("matops.txt", "rt")

    linha = arq.readline().strip()

    calculo = ""

    lst = ["-", "T"]

    while (linha != ""):
        calculo = linha.split(" ")
        matA = ""

        matB = ""
        for x in calculo[0]:
            if x not in lst:
                matA += x

        for x in calculo[2]:
            if x not in lst:
                matB += x

        matA = carregamat(f"{matA}")

        matB = carregamat(f"{matB}")

        if ("T" in calculo[0]):
            matA = transposta(matA)

        if ("T" in calculo[2]):
            matB = transposta(matB)

        if ("-" in calculo[0]):
            matA = negativa(matA)
        if ("-" in calculo[2]):
            matB = negativa(matB)

        if (calculo[1] == "+"):
            resultado = somaMat(matA, matB)
            salvamat(f"{calculo[0]}mais{calculo[2]}", resultado)

        elif (calculo[1] == "x"):
            resultado = multi(matA, matB)
            if resultado is not None:
                salvamat(f"{calculo[0]}vezes{calculo[2]}", resultado)

        elif (calculo[1] == "-"):
            matBnegado = negativa(matB)
            resultado = somaMat(matA, matBnegado)
            if resultado is not None:
                salvamat(f"{calculo[0]}menos{calculo[2]}", resultado)

        linha = arq.readline().strip()

    arq.close()

    print('OPERAÇÃO COM MATRIZES FINALIZADA')

if __name__ == '__main__':
    main()