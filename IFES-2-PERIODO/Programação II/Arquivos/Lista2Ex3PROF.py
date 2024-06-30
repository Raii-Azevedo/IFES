def valida_ip(str_ip):
    lst = str_ip.split(".")
    if len(lst) != 4:
        return False

    for octeto in lst:
        if octeto not in range(256):
            return False
    # for
    return True
# fim valida_ip


def main():
    lista_ips = []

    # Leitura dos ips
    arq = open("bdips.txt", "rt")
    linha = arq.readline()
    while linha != "":
        lista_ips.append(linha.strip())
        linha = arq.readline()
    # while
    arq.close()

    lista_val = []
    lista_inv = []

    for ip in lista_ips:
        if valida_ip(ip):
            lista_val.append(ip)
        else:
            lista_inv.append(ip)
    # for ip

    # Processando o arquivo de saída.
    arq = open("saidabdips.txt", "wt")
    arq.write('[Endereços Válidos:]\n')


arq = open("saidabdips.txt", "wt")
arq.write('[Endereços Válidos:]\n')

   for ip in lista_val:
        arq.write(ip + '\n')
        arq.write('\n')


    arq.close()
# fim main

if __name__ == '__main__':
 main()
