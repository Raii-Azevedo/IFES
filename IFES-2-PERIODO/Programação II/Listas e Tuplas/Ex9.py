print('''9. Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus 
vendedores com base em comissões. O vendedor recebe R$200 por semana mais 9 
por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que 
teve vendas brutas de R$3000 em uma semana recebe R$200 mais 9 por cento de 
$3000, ou seja, um total de $470. Escreva um programa (usando uma lista de 
contadores) que determine quantos vendedores receberam salários nos seguintes 
intervalos de valores:
a) R$200 - R$299
b) R$300 - R$399
c) R$400 - R$499
d) R$500 - R$599
e) R$600 - R$699
f) R$700 - R$799
g) R$800 - R$899
h) R$900 - R$999
i) R$1000 em diante
Desafio: Crie uma função para chegar na posição da lista a partir do salário, sem 
fazer vários ifs aninhados.\n''')

salarios = []

for i in range (10):
    valor = int(input('Valor da venda: '))

    salarios.append(valor)


contadores = [0] * 9

for salario in salarios:
    comissao = salario * 0.09
    salario_total = salario + 200 + comissao
    indice = max(0, min(int((salario_total - 200) / 100), 8))
    contadores[indice] += 1

for i, contador in enumerate(contadores):
    if i == 8:
        print(f"R$1000 em diante: {contador}")
    else:
        print(f"R${200+(i*100)}-R${299+(i*100)}: {contador}")



