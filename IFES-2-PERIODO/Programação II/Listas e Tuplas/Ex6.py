print('''6. Faça um programa que receba a temperatura média de cada mês do ano e 
armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e 
mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram 
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).\n''')

lst = []
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']

for i in range(len(mes)):
    temp = float(input(f'Digite a temperatura de {mes[i]}: '))
    lst.append(temp)

print(lst)

#Calculo Média Anual
soma = 0
for i in range(len(lst)):
    soma = soma + (lst[i])
media = soma/6

print(f'\nMédia de Temperatura: {media:.2f}°C\n')

# Índice de temperatura ACIMA da média

