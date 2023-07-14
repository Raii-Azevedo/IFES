def det(M):
    diag1 = M [0][0] * M[1][1] * M[2][2]
    diag2 = M [0][1] * M [1][2] * M [2][0]
    diag3 = M [0][2] * M [1][0] * M [2][1]

    soma1 = diag1 + diag2 + diag3

    diag4 = M [0][2] * M [1][1] * M [2][0]
    diag5 = M [0][0] * M [1][2] * M [2][1]
    diag6 = M [0][1] * M [1][0] * M [2][2]

    soma2 = diag4 + diag5 + diag6

    return soma1 - soma2


def alinhados (p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    M = [[x1, y1, 1],[x2,y2,1], [x3,y3,1]]
    return det(M) == 0

# SE O RESULTADO DA FUNÇÃO FOR TRUE, ESTÃO ALINHADOS.

 
