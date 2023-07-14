print('''1.12.18. A comissão organizadora de um rallye automobilístico decidiu apurar os resultados 
da competição através de um processamento eletrônico. Um dos algoritmos necessários para a
classificação das equipes concorrentes é o que emite uma listagem geral do desempenho das 
equipes, atribuindo pontos segundo determinadas normas:
O algoritmo deverá:
a) Ler:
a.1) uma linha contendo os tempos-padrão (em minutos decimais) para as três fases de 
competição;
a.2) um conjunto de linhas contendo cada uma o número de inscrição da equipe e os tempos 
(em minutos decimais) que as mesmas despenderam ao cumprir as três diferentes etapas. A 
última linha (flag), que não entrará nos cálculos, contém o número 9999 como número de 
inscrição.
b) Calcular:
b.1) os pontos de cada equipe em cada uma das etapas, seguindo o seguinte critério:
4 de 12
Seja D o valor absoluto da diferença entre o tempo-padrão (lido na primeira linha) e o tempo 
despendido pela equipe numa etapa:
D < 3 minutos – atribuir 100 pontos à etapa
3 <= D <= 5 minutos – atribuir 80 pontos à etapa
D > 5 minutos – atribuir 80 – (D - 5)/5 pontos à etapa
b.2) o total de pontos de cada equipe nas três etapas;
b.3) a equipe vencedora.
c) Escrever:
c.1) para cada equipe, o número de inscrição, os pontos obtidos em cada etapa e o total de 
pontos obtidos.\n''')

def pontos1etapa(tp, te):
    D = abs(tp - te)
    pontuacao = 0

    if D < 3:
        pontuacao = 100
    elif D >=3 and D <= 5:
        pontuacao = 80
    else:
        pontuacao = 80 - (D-5)/5

    return pontuacao


def main():
    print('O PROBLEMA DE RALLY\n')

    tp1 = float(input('Entre com o tempo padrão 1: '))
    tp2 = float(input('Entre com o tempo padrão 2: '))
    tp3 = float(input('Entre com o tempo padrão 3: '))
   
    inscwinner = 0
    pontoswinner = 0

    inscricao = input('Nº de inscrição da equipe: ')

    while inscricao != '9999':
        te1 = float(input(' Entre com o tempo 1 da equipe: '))
        te2 = float(input(' Entre com o tempo 2 da equipe: '))
        te3 = float(input(' Entre com o tempo 3 da equipe: '))

        pe1 = pontos1etapa(tp1, te1)
        pe2 = pontos1etapa(tp2, te2)
        pe3 = pontos1etapa(tp3, te3)
        totalpts = pe1 + pe2 + pe3

        print ("%s %10d %10d %10d %10d" % (inscricao, pe1, pe2, pe3, totalpts))

        if totalpts > pontoswinner:
            pontoswinner = totalpts
            inscwinner = inscricao
        
        inscricao = input('Nº de inscrição da equipe: ')


    print('EQUIPE VENCEDORA')
    print(f'Inscrição: {inscwinner}\n Pontos: {totalpts}')


if __name__ == '__main__':
    main()