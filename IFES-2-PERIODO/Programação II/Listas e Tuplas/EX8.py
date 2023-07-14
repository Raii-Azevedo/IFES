print('''8. Faça um programa que leia um número indeterminado de valores, correspondentes a
notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que
não deve ser armazenado). Após esta entrada de dados, faça:
a) Mostre a quantidade de valores que foram lidos;
b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c) Exiba todos os valores na ordem inversa à que foram informados, um ao lado do 
outro;
d) Calcule e mostre a soma dos valores;
e) Calcule e mostre a média dos valores;
f) Calcule e mostre a quantidade de valores acima da média calculada;
g) Calcule e mostre a quantidade de valores abaixo de sete;
h) Encerre o programa com uma mensagem.\n''')

def main():
    lst = []

    valor = cont = contb = soma = 0

    while valor != -1:
        valor = float(input(' Digite um valor: '))
        lst.append(valor)
    
    for i in range(len(lst)):
        soma = soma + (lst[i])
    media = soma/(len(lst))

    
    

    print(lst)
    print(f'Média dos valores: {media:.2f}')
    print(f'Valores acima da média: {cont}')
    print(f'Valores abaixo de 7 {contb}\n')

    print('PROGRAMA ENCERRADO')
    



if __name__== '__main__':
    main()