# Num Copa do Mundo, determine o número de empates.
def SomaPontos(classificacao):
    soma = 0
    for _, pontos in classificacao:
        soma += pontos

    return soma

def Copa (N,classificacao):
    return 3* N - SomaPontos (classificacao)

    