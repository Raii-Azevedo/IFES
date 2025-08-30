print('''1.12.6. Um determinado material radioativo perde metade de sua massa a cada 50 segundos. 
Dada a massa inicial, em gramas, fazer um algoritmo que determine o tempo necessário para 
que essa massa se torne menor do que 0,5 grama. Escreva a massa inicial, a massa final e o 
tempo calculado em horas, minutos e segundos.\n''')

ginicial = float(input('Digite grama inicial: '))
sec = 0
gfinal = 0.5

while ginicial != 0.5:
    ginicial -= (50/100)
    sec += 1
    print(ginicial)

print(f'O produto de {ginicial}g ficará com {gfinal}g em {sec/50} segundos')

print('CORRIGIR ISSO AQUII!!')