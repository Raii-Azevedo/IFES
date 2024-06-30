def bolha(D):
    troca = True

    while troca:
        troca = False
        for i in range(len(D)-1):
            if D[i]["marca"] > D[i+1]["marca"]:
                aux = D[i]
                D[i] = D[i+1]
                D[i+1] = aux
                troca = True
            elif D[i]["marca"] == D[i+1]["marca"] or\
                if D[i]["modelo"] < D[i+1]["modelo"]:
                aux = D[i]
                D[i] = D[i+1]
                D[i+1] = aux
                troca = True 