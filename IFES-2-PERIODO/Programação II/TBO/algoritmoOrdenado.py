def selection(D):
    for i in range(len(D)-1):
        indice_menor_de_todos = i

        for j in range(i+1, len(D)):
            if D[j]['marca'] < D[indice_menor_de_todos]['marca'] or D[j]['marca'] ==  D[indice_menor_de_todos]['marca'] and D[j]['modelo'] < D[indice_menor_de_todos]['modelo']:
                indice_menor_de_todos = j

        aux = D[i]
        D[i] = D[indice_menor_de_todos]
        D[indice_menor_de_todos] = aux

    return D


def insertion(D):

    for i in range(1, len(D)):
        chave = D[i]
        j = i - 1
        while j >= 0 and D[j]['marca'] > chave['marca'] or D[j]['marca'] == D[j]['marca'] and D[j]['modelo'] < D[j]['modelo']:
            D[j + 1] = D[j]
            j -= 1
        D[j + 1] = chave

    return D


def lst_2_dict(lst):
    D = []
    # Range de 0 ao Tamanha da lista de 4 em 4 items.
    for i in range(0, len(lst), 4):
        item = lst[i:i+4]

        V = {
            "placa": item[0].strip(),
            "modelo": item[1].strip(),
            "marca": item[2].strip(),
            "Km": item[3].strip(),
        }

        D.append(V)

    return D


def txt_2_lst():
    lst = []
    with open('bdveiculos.txt', 'rt') as file:
        linha = file.readline().strip()

        while linha != '':
            lst.append(linha)
            linha = file.readline().strip()

    return lst


def print_lst(D):
    for i in D:
        print(i["marca"], i["modelo"], i["placa"], i["Km"],)


def main():
    lst = txt_2_lst()

    D = lst_2_dict(lst)
    print_lst(D)

    insertion(D)
    print('\nINSERTION')
    print_lst(D)

    selection(D)
    print('\nSELECTION')
    print_lst(D)


if __name__ == '__main__':
    main()
