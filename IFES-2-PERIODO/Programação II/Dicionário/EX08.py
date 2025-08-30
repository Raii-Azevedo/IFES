import json
print('''Dado o arquivo BDVEICULOS>TXT ma sua forma original (1 veículo a cada 4 linhas), construa um
programa pythn que transforme este arquivo em um arquivo JSON.
O ID dos campos e placa, modelo, marca e Km''')


def lst_2_Dic(lst):
    result = []
    for item in lst:
        D = {
            "placa": item[0].strip(),
            "modelo": item[1].strip(),
            "marca": item[2].strip(),
            "quilometragem": item[3].strip()
        }
        result.append(D)

    print(result)
    return result


def txt_2_json():
    lst = []
    with open('bdveiculos.txt', 'rt') as file:
        linha = file.readline().strip() 

        while linha != '':
            for i in range(4):
                lst.append(linha)
                linha = file.readline().strip() 

    return lst

def main():
    lst = txt_2_json()

    print(lst)

    D = lst_2_Dic(lst)

    print('Processamento Concluído')


if __name__ == '__main__':
    main()
