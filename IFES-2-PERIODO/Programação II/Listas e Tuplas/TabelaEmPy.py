# COMO TRANSFORMAR UM TABELA EM PYTHON
def maior_valor(tabela):
     # Função que recebe a tabela como parâmetro e indique o maior valor
    maior = 0
    posicao = 0
    
    for linha in tabela:
        if linha[1] > maior:
            maior = linha[1]
            posicao = [linha]

    print(posicao)

    

def main():
    tabela = [
        ['Janeiro', 56, 'a', 3, 'Pronto', 4, 2],
        ['Fevereiro', 7, 'f', 4, 'Pronto', 5, 5],
        ['Março', 400, 'g', 2, 'em andamento', 6, 7],
        ['Abril', 6, 'p', 3, 'Pronto', 8, 3],
        ['maio',23,'v',4,'pronto',3,6],
        ['junho',90,'p',4,'concluido']
    ]

    #for linha in tabela:
        #print("%-9s%8d%4s%5d%18s%5d%5d" % (linha[0], linha[1], linha[2], linha[4], linha[5], linha[6]))

    maior_valor(tabela)


if __name__ == '__main__':
    main()
