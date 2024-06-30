def main():
    valid = []
    invalid = []
    aux = []
    inteiros = []
    with open('EndIP.txt', 'rt') as file:
        arq = file.readline()

        while arq != "":
            arqsem = arq.replace('.', ' ') # Retira o "." do arquivo
            aux.append(arqsem.strip()) # Elimina o \n da lista 
            arq = file.readline()
        file.close()

        for elemento in aux: # Quebrando cada elemento da lista em uma lista de strings
            valores_str = elemento.split() 
            valores_int = [int(valor) for valor in valores_str] # Convertendo cada valor em inteiro e adicionando à lista
            inteiros.append(valores_int)

        for lista in inteiros: # Verifica se algum valor da lista é maior que 255
            if any(valor > 255 for valor in lista):
                invalid.append(lista)
                for i in range(len(invalid)):
                    invalid[i] = str(invalid[i]).replace(',', '.')
            else:
                valid.append(lista)
                for i in range(len(valid)):
                    valid[i] = str(valid[i]).replace(',', '.')
        
        with open('Ips.txt', 'a') as final:
            final.write('IPS VALIDOS:\n')
            for ip in valid:
                final.write(ip + '\n')
                final.write('\n')
            final.write('IPS INVALIDOS:\n')
            
            for ip in invalid:
                final.write(ip + '\n')
                final.write('\n')

        final.close()

if __name__ == '__main__':
    main()