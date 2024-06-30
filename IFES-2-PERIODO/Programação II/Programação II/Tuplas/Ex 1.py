def funcao(M):
    n = len(M)
    for linha in M:
        if n != len(linha):
            return False
    return True