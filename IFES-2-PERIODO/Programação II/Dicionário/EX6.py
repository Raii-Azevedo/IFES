import json
print('''Construa uma programa Python que transforme a base de dados "bdcepruas.txt" em um arquivo JSON,
A estrutura do arquivo JSON de saída seque a ordem dos campos do artigo original. Nomeie o arquivo
de saída como "saidaexec.json" ''')


def linha_to_dic(linha_arq):
    lst = linha_arq.split(",")
    diccpruas = {
        "logradouro": lst[0],
        "numero": lst[1],
        "cep": lst[2],
        "bairro": lst[3],
        "municipio": lst[4],
        "uf": lst[5]
    }
    return diccpruas
# fim linha_to_dic


def main():
    arqcepsruas = open("bdcepsruas.txt", "rt")
    linha = arqcepsruas.readline().strip()

    lst = []

    while linha != "":
        dic = linha_to_dic(linha)
        lst.append(dic)
        linha = arqcepsruas.readline().strip()
    # while ..
    arqcepsruas.close()

    dic = {"dados": lst}

    arqout = open("saida.json", "wt")
    json.dump(dic, arqout)
    arqout.close()
# fim main

if __name__ == '__main__':
    main()
