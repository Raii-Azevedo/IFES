#
# Exercicio 9 Lista PythonBr
#
# Data 02/03/2023
# Local: lab 205
# Autor: Ernani Ribeiro
#
# Utilize uma lista para resolver o problema a 
# seguir. 
# Uma empresa paga seus # vendedores com base em 
# comissões. 
# O vendedor recebe R$200 por semana mais 9 # por 
# cento de suas # vendas brutas daquela semana. 
# Por exemplo, um vendedor que teve vendas brutas 
# de R$3000 em uma semana recebe R$200 mais 9 por 
# cento de $3000, ou seja, um total de $470. 
# Escreva um programa (usando uma lista de
# contadores) que determine quantos vendedores 
# receberam salários nos seguintes intervalos de 
# valores:
#
# a) R$200 - R$299
# b) R$300 - R$399
# c) R$400 - R$499
# d) R$500 - R$599
# e) R$600 - R$699
# f) R$700 - R$799
# g) R$800 - R$899
# h) R$900 - R$999
# i) R$1000 em diante
#
# Desafio: Crie uma função para chegar na posição 
# da lista a partir do salário, sem fazer vários 
# ifs aninhados.
#
def achacontador(lstf,totalv):
    salario = 200 + totalv * 0.09
    lstf[len(lstf)-1][1] = totalv

    for i in range(len(lstf)):
        t = lstf[i]
        if (salario >= t[0]) and (salario <= t[1]):
            return i
# fim achacontador 

def main(args):
    lstfaixas = [[(200,299),0],(300,399),(1000,9999)]
    lstcont = [0,0,0,0,0,0,0,0,0]

    # Supor que a empresa possui 10 funcionários.
    for i in range(10):
        totalvendas = float(input("Entre com o total de vendas do funcionário %d: " % (i+1)))
        posicao = achacontador(lstfaixas,totalvendas)
        lstcont[posicao] = lstcont[posicao] + 1
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
