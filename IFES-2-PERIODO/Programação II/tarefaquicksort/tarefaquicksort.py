from modquicksort import quickr, quicknr

def salvafile(file, arq):
    with open(file, "w") as file:
        for veiculo in arq:
            linha = (f"{veiculo['placa']}, {veiculo['modelo']}, {veiculo['marca']}, {veiculo['km']}, {veiculo['cor']}, {veiculo['combustivel']}\n")
            file.write(linha)
    file.close()


def carregabd(file):
    veiculos = []
    with open(file, 'rt') as input_file:
        linha = input_file.readline()
        while linha != '':
            dados = linha.strip().split(', ')
            if len(dados) == 6:
                veiculo = {
                    'placa': dados[0],
                    'modelo': dados[1],
                    'marca': dados[2],
                    'km': dados[3], 
                    'cor': dados[4],
                    'combustivel': dados[5]
                }
                veiculos.append(veiculo)
            else:
                pass
            linha = input_file.readline()

    return veiculos


def main():
    file = 'bdveiculos2.txt'
    arq = carregabd(file)
    print("JSON executado")

    # QUICKSORT RECURSIVO
    file_quickr = 'quickr-out.txt'
    salvafile(file_quickr, quickr(arq))
    print("Quicksort recursivo concluído")

    # QUICKSORT NÃO RECURSIVO
    file_quicknr = 'quicknr-out.txt'
    salvafile(file_quicknr, quicknr(arq))
    print("Quicksort não recursivo concluído")

if __name__ == '__main__':
    main()
