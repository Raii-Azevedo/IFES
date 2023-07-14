def main():
    F = open('primeiro.txt', 'rt')
    S = open('segundo.txt', 'rt')

    T = open('terceiro.txt', 'wt')

    linha1 = F.readline()

    while linha1 !='':
        T.write(linha1)
        linha1 = F.readline()
    T.write('\n\n')

    T.close()
    F.close()

    T = open('terceiro.txt', 'a')
    linha2 = S.readline()
    while linha2 !='':
        T.write(linha2)
        linha2 = S.readline()

    S.close()
    T.close()

    print('Tarefa Finalizada')

if __name__ == '__main__':
    main()