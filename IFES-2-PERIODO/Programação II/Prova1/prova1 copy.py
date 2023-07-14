def relatorioDomains(nomearq, lst):
    with open(nomearq, "w") as arq:
        for uf, sites in lst:
            arq.write(f"{uf}:\n")
            dominios = [site.split(".")[-2] for site in sites]
            dominios_contados = set(dominios)
            for dominio in dominios_contados:
                count = dominios.count(dominio)
                arq.write(f"{dominio}:{count}\n")
            arq.write("\n")
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
