def relatorioDomains(nomearq, lst):
    arq = open(nomearq, "wt")
    lst_count = []
    position = 0
    for UF in lst:
        lst_count.append((UF[0], []))
        for site in UF[1]:
            dom = site.split(".")
            lst_count[position][1].append(dom[len(dom) - 2])

        position += 1

    lstContados = []
    contador = 0
    for dominio in lst_count:
        arq.write(dominio[0] + ":")
        arq.write("\n")
        lstContados = []
        for penultimo in dominio[1]:
            contador = 0
            if penultimo not in lstContados:
                lstContados.append(penultimo)
                for cod in dominio[1]:
                    if cod == penultimo:
                        contador += 1
                arq.write("{}:{}\n".format(penultimo, contador))

        arq.write("\n")

    arq.close()
    return lst


def processa(nomearq):
    aux = []
    # LISTA AUXILIAR SOMENTE COM OS DOMÍNIOS
    with open('webdomains.txt', 'rt') as arq:
        linha = arq.readline().strip()
        while linha != '':
            aux.append(linha)
            linha = arq.readline().strip()

    arq.close()

    # LISTA INDEX COM UFS
    index = []
    for uf in aux:
        indicador = uf[-2:]
        if indicador not in index:
            index.append(indicador)

    # LISTA D (TUPLAS)
    D = []
    for uf in index:
        dominios_uf = []
        for dominio in aux:
            if dominio[-2:] == uf:
                dominios_uf.append(dominio)
        D.append((uf, dominios_uf))

    return D

def main():
    print('PROCESSAMENTO DE ARQUIVO')
    
    D = processa("webdomains.txt")
    
    relatorioDomains("saidaprova1.txt", D)


if __name__ == '__main__':
    main()
