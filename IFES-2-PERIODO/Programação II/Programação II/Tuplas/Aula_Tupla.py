# Método 1 #
m = []
for i in range (5):
    linha = []
    for j in range (7):
        linha.append(0)
    m.append(linha)
#print(m)
# ESSES DOIS MÉTODOS SÃO EQUIVALENTES -> IRÃO GERAR O MESMO RESULTADO
# Método 2 #
m1 = []
for i in range (5):
    m1.append (7*[0])
#print (m1)

# CRIANDO FUNÇÃO
def soma_matriz(A,B):
    nLinhas = len(A)
    nColunas = len (A[0])
    C = cria_matriz(nLinhas,nColunas)

    for i in range (nLinhas):
        for j in range (nColunas):
            C[i][j] = A[i][j] + B [i][j]
    
    return (C)