print('''17. Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e 
armazene os resultados em uma lista . Depois, mostre quantas vezes cada valor foi 
conseguido. Dica: use uma lista de contadores(1-6) e uma função para gerar numeros
aleatórios, simulando os lançamentos dos dados\n''')

from random import randint

lst = []
# Números aleatórios da DADO
for i in range(100):
    dado = randint(1, 6)
    lst.append(dado)

print(f'Lista: {lst}\n')

# Contagem de números
for i in range (1, 7):
    print(f'O n° {i} saiu {lst.count(i)} vezes')


