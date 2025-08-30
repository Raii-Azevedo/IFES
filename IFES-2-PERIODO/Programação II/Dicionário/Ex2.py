def faxina(palavra):
    # Faxina no final da palavra
    while (palavra != "") and (not palavra[-1].isalnum()):
        palavra = palavra[:-1]

    # Faxina no inicio da palavra
    if len(palavra) > 0:
        while not palavra[0].isalnum():
            palavra = palavra[1:]

    return palavra


def loadfile():
    D = {}

    proibidos = ['a','à','o','e','na','no','se','seu','seus','teu','tua','então','uma','um','de','que','os',
                 'dos','para','do','as','com','em','da','é','ao','por','mas','pois','te','me']

    with open('biblia.txt', 'rt', encoding='utf-8') as arquivo:

        for word in arquivo:
            palavras = word.lower().split()

            for palavra in palavras:
                palavra = faxina(palavra)

                if palavra != "" and palavra not in proibidos:
                    if palavra in D:
                        D[palavra] += 1
                    else:
                        D[palavra] = 1
        arquivo.close()

    return D


def writefile(D):

    total = f'Total de palavras: {sum(D.values())}\n' + '\n'
    diferent = f'Total de palavras diferentes: {len(D)}\n' + '\n'

    mais_frequentes = sorted(
        D.items(), key=get_freq, reverse=True)[:20] # SORTED (Ordena por frquencia) 
    

    with open('BibliaData.txt', 'wt', encoding='utf-8') as file:
        file.write('- BASE DE DADOS BÍBLIA -\n\n')
        file.write(total)
        file.write(diferent)

        file.write('As 20 palavras mais frequentes:\n')
        cont = 0
        for palavra, frequencia in mais_frequentes:
            cont += 1
            frequency = f'{cont}° - "{palavra}": {frequencia} \n'
            file.write(frequency)

        file.close()
    
def get_freq(item): # A função get_freq recebe um item do dicionário (que é uma tupla contendo uma palavra e sua frequência) e retorna o valor da segunda posição (frequência).
    return item[1]

def main():
    print('CONTAGEM DE PALAVRAS NA BÍBLIA -> DICIONÁRIO')

    D = loadfile()

    writefile(D)

    print('- TAREFA FINALIZADA -')


if __name__ == '__main__':
    main()
