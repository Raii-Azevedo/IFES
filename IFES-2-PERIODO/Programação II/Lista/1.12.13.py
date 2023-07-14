print('''1.12.13. Deseja-se fazer uma pesquisa a respeito do consumo mensal de energia elétrica em 
uma determinada cidade. Para isso, são fornecidos os seguintes dados:
- preço do kWh consumido;
- número do consumidor;
- quantidade de kWh consumidos durante o mês;
- código do tipo de consumidor (residencial, comercial, industrial).
O número do consumidor igual a zero deve ser usado como flag. Fazer um algoritmo que:
- leia os dados descritos acima:
- calcule:
a) para cada consumidor, o total a pagar;
b) o maior consumo verificado;
c) o menor consumo verificado;
d) o total do consumo para cada um dos três tipos de consumidores;
e) a média geral de consumo;
- escreva:
a) para cada consumidor, o seu número e o total a pagar;
b) o que foi calculado nos itens b, c, d, e acima especificados.\n''')

# CÓDIGO COMPLETAMENTE ERRADO

def main():
    print(f'- CONSUMO DE ENERGIA ELÉTRICA'
          'Preço: R$ 5.85\n')

    tot1 = tot2 = tot3 = count = 0

    N = int(input('N° consumidor: '))
    while N !=0:

        cod = int(input(f'\nCódigo consumidor\n'
              '[1] - Residencial\n'
              '[2] - Comercial\n'
              '[3] - Industrial\n'
              'Digite o Nº desejado: '))
        
        consumo = float(input(' Consumo wt mês: '))
        menor = maior = consumo
        
        if consumo < menor:
            menor = consumo
        if consumo > maior:
            maior = consumo

        if cod == 1:
            tot1 += consumo
            count += 1
        elif cod == 2:
            tot2 += consumo
            count += 1
        elif cod == 3:
            tot3 += consumo
            count += 1
        
        N = int(input('N° consumidor: '))

    if cod == 1:
        media = tot1/count
    if cod == 2:
        media = tot2/count
    if cod == 3:
        media = tot3/count

    print(f'\nTOTAL CONSUMO\nN° consumidor: {N}\nCódigo: {cod}\nValor a pagar: R${media}')

if __name__ == "__main__":
    main()