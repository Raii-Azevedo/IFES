def mergeSort(D):
    if len(D) <= 1:
        return D

    meio = len(D) // 2
    esq = D[:meio]
    dir = D[meio:]

    esq = mergeSort(esq)
    dir = mergeSort(dir)

    return merge(esq, dir)


def merge(esq, dir):
    merged = []
    i = j = 0

    while i < len(esq) and j < len(dir):
        if esq[i]["marca"] < dir[j]["marca"] or esq[i]["modelo"] < dir[j]["modelo"]:
            merged.append(esq[i])
            i += 1
        else:
            merged.append(dir[j])
            j += 1

    merged.extend(esq[i:])
    merged.extend(dir[j:])

    return merged


def lst_2_dict(lst):
    D = []
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
        print(i["marca"], i["modelo"], i["placa"], i["Km"])


def main():
    lst = txt_2_lst()

    D = lst_2_dict(lst)
 
    mergeS = mergeSort(D)
    print_lst(mergeS)


if __name__ == '__main__':
    main()
