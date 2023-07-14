print('''1.12.2. Tem-se um conjunto de dados contendo a altura e o sexo (masculino, feminino) de 50 
pessoas. Fazer um algoritmo que calcule e escreva:
- a maior e a menor altura do grupo;
- a média de altura das mulheres;
- o número de homens\n''')
F = H = mediaF = 0
menor = 1.99

for c in range(6):
    sexo = input('Gênero [F|M]: ').upper()[0]
    altura = float(input('Altura: '))
    if altura < menor:
        menor = altura
    if sexo == 'M':
        H += 1
    if sexo == 'F':
        F += 1
        mediaF += altura

media = mediaF/F

print(f'DADOS COLETADOS\nMenor altura: {menor}')
print(f'Nº de homens: {H}')
print(f'Média altura feminina: {media:.2f}')
