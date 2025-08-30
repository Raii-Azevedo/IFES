print('''1. Faça um Programa que leia 20 números inteiros e armazene-os em uma lista. Após a
leitura, percorra a lista original e a Armazene os números PARES em uma segunda 
lista e os números IMPARES em uma terceira lista. Ao final imprima as três listas.\n''')

lst = []
for i in range(1, 21):
    num = int(input(f' Digite o {i}° inteiro: '))

    lst.append(num)

lstPar = []
lstImpar = []

for i in range (len(lst)):
    if lst[i]%2 == 0:
        lstPar.append(lst[i])
    else:
        lstImpar.append(lst[i])

print(f'Lista completa: {lst}')
print(f'Lista Par: {lstPar}')
print(f'Listar Ímpar: {lstImpar}')

