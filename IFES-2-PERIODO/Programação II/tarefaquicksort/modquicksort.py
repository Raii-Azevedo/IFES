def quickr(arq):
    if len(arq) <= 1:
        return arq
    else:
        pivot = arq[0]
        menores = []
        iguais = []
        maiores = []

        for veiculo in arq:

            if menor(veiculo, pivot):
                menores.append(veiculo)
            elif veiculo == pivot:
                iguais.append(veiculo)
            else:
                maiores.append(veiculo)

        return quickr(menores) + iguais + quickr(maiores)


def quicknr(arq):
    if len(arq) <= 1:
        return arq
    else:
        pilha = [(0, len(arq) - 1)]
        while len(pilha) > 0: 
            baixo, alto = pilha[-1] 
            pilha = pilha[:-1] 

            if baixo < alto:
                pivot = particionar(arq, baixo, alto)
                pilha.append((baixo, pivot - 1)) 
                pilha.append((pivot + 1, alto)) 

        return arq


def particionar(arq, baixo, alto):
    pivot = arq[alto]
    i = baixo - 1
    for j in range(baixo, alto):
        if menor(arq[j], pivot):
            i += 1
            arq[i], arq[j] = arq[j], arq[i]
    arq[i + 1], arq[alto] = arq[alto], arq[i + 1]
    return i + 1


def menor(V1, V2):
    if V1['combustivel'] < V2['combustivel']:
        return True
    elif V1['combustivel'] == V2['combustivel'] and V1['cor'] < V2['cor']:
        return True
    elif V1['combustivel'] == V2['combustivel'] and V1['cor'] == V2['cor'] and V1['marca'] < V2['marca']:
        return True
    elif V1['combustivel'] == V2['combustivel'] and V1['cor'] == V2['cor'] and V1['marca'] == V2['marca'] and V1['modelo'] > V2['modelo']:
        return True
    elif V1['combustivel'] == V2['combustivel'] and V1['cor'] == V2['cor'] and V1['marca'] == V2['marca'] and V1['modelo'] == V2['modelo'] and V1['km'] < V2['km']:
        return True
    else:
        return False


def igual(V1, V2):
    return (
        V1['combustivel'] == V2['combustivel'] and
        V1['cor'] == V2['cor'] and
        V1['marca'] == V2['marca'] and
        V1['modelo'] == V2['modelo'] and
        V1['km'] == V2['km']
    )


def maior(V1, V2):
    if V1['combustivel'] > V2['combustivel']:
        return True
    elif V1['combustivel'] == V2['combustivel'] and V1['cor'] > V2['cor']:
        return True
    elif V1['combustivel'] == V2['combustivel'] and V1['cor'] == V2['cor'] and V1['marca'] > V2['marca']:
        return True
    elif V1['combustivel'] == V2['combustivel'] and V1['cor'] == V2['cor'] and V1['marca'] == V2['marca'] and V1['modelo'] < V2['modelo']:
        return True
    elif V1['combustivel'] == V2['combustivel'] and V1['cor'] == V2['cor'] and V1['marca'] == V2['marca'] and V1['modelo'] == V2['modelo'] and V1['km'] > V2['km']:
        return True
    else:
        return False