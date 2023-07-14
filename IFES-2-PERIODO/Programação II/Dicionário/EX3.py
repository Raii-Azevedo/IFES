def writefile(D):
    with open('dicsaida.txt', 'w') as file:
        for chave, valores in D.items():
            text = chave + ':'
            for valor in valores:
                text += valor[4:] + ',' # Remove o no. deixando somente o N° 
            text = text[:-1]  # Remove a última vírgula
            file.write(text + '\n')

def txt_2_dic(txt): 
    D = {}
    for lista in txt:
        chave = lista[2]
        valor = lista[1]
        if chave not in D:
            D[chave] = [valor]
        else:
            D[chave].append(valor)
    return D

def loadfile(txt):  
    with open('bdcepsruas.txt', 'rt') as file:
        linha = file.readline()
        while linha != '':
            txt.append(linha.strip().split(','))
            linha = file.readline()
    return txt

def main():
    txt = []
    
    loadfile(txt) # Função parar ler TXT e transformar em Lista(txt)
    
    D = txt_2_dic(txt)  # Função que lê o elemento[2] de cada lista e transforma em chave e o elemento[1] e transforma em valor

    writefile(D)

    print('PROCESSAMENTO FINALIZADO')

if __name__ == '__main__':
    main()
