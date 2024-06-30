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

def main(args):
    ca,cb,cc,cd,ce,cf,cg,ch,ci = 0,0,0,0,0,0,0,0,0

    # Supor que a empresa possui 10 funcionários.
    for i in range(10):
        totalvendas = float(input("Entre com o total de vendas do funcionário %d: " % (i+1)))
        salario = 200 + totalvendas * 0.09
        if salario >= 200 and salario <= 299:
            ca = ca + 1
        elif salario >= 300 and salario <= 399:
            cb = cb + 1
        elif salario >= 400 and salario <= 499:
            cc = cc + 1
        elif salario >= 500 and salario <= 599:
            cd = cd + 1
        elif salario >= 600 and salario <= 699:
            ce = ce + 1
        elif salario >= 700 and salario <= 799:
            cf = cf + 1
        elif salario >= 800 and salario <= 899:
            cg = cg + 1
        elif salario >= 900 and salario <= 999:
            ch = ch + 1
        elif salario >= 1000:
            ci = ci + 1
    # for i ..

    print("Quantidade de salários dentro das faixas:")
    print("Faixa A) ",ca)
    print("Faixa B) ",cb)
    print("Faixa C) ",cc)
    print("Faixa D) ",cd)
    print("Faixa E) ",ce)
    print("Faixa F) ",cf)
    print("Faixa G) ",cg)
    print("Faixa H) ",ch)
    print("Faixa I) ",ci)

    return 0
# fim main

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
