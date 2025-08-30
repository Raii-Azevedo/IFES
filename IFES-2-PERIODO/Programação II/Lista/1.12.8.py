print('''1.12.8. Uma certa firma fez uma pesquisa de mercado para saber se as pessoas gostaram ou 
não de um novo produto lançado no mercado. Para isso, forneceu o sexo do entrevistado e sua 
resposta (sim ou não). Sabendo-se que foram entrevistadas 2.000 pessoas, fazer um algoritmo 
que calcule e escreva:
- o número de pessoas que responderam sim;
- o número de pessoas que responderam não;
- a porcentagem de pessoas do sexo feminino que responderam sim;
- a porcentagem de pessoas do sexo masculino que responderam não;\n''')
F = M = S = N = 0

for c in range(10):
    sexo = input('Gênero [M|F]: ').upper()[0]
    aprovacao = input('Aprova o produto? [S|N]: ').upper()[0]

    if sexo == 'F':
        F += 1
    if sexo == 'M':
        M += 1
    if aprovacao == 'S':
        S += 1
    else:
        N += 1

mS = (S*100)/c
mN = (N*100)/c

print(f'\nDADOS COLETADOS\n Nº de mulheres: {F}\n Nº de homens {M}')
print(f'Aprovação:\n{S} pessoas responderam Sim = {mS:.2f}%\n{N} pessoas responderam Não = {mN:.2f}%\n')

print('CORRIGIR PORCENTAGEM!')