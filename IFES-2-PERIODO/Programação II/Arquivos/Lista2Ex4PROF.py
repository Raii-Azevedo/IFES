def filtro(tb, strmarca):
    nomearq = strmarca + '.txt'

    arq = open (nomearq, 'wt')

    for veiculo in tb:
        if veiculo[2] == strmarca:
            linha = veiculo[0] + ',' + veiculo[1] + ',' + veiculo[2] + ',' + veiculo[3] + '\n'
            arq.write(linha)

    arq.close()

def loadtab(nomearq):
    arq = open('bdveiculos.txt', 'rt')
    tabela = []

    placa = arq.readline()

    while placa != '':
        modelo = arq.readline()
        marca = arq.readline()
        km = arq.readline()

        lstveiculo = [placa.strip(), modelo.strip(), marca.strip(), km.strip()] 

        tabela.append(lstveiculo) # Adicionar a lista de dados do veículo na lista TABELA       

        placa = arq.readline()

    arq.close()

    return tabela

def main():
    tab = loadtab("bdveiculos.txt")
    filtro(tab,"FORD")
    filtro(tab,"TOYOTA")
    filtro(tab,"FIAT")
    
    print("Processamento concluído!!")


if __name__ == '__main__':
    main()