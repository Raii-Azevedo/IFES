print('''3. Faça um Programa que leia duas listas com 10 elementos cada. Gere uma terceira 
lista de 20 elementos, cujos valores deverão ser compostos pelos elementos 
intercalados das duas outras listas.\n''')

lst1 = []
lst2 = []
lst3 = []

print('Digite os elementos da 1ª Lista:')
for i in range(10):
    num = int(input(f'Digite o {i+1}° N: '))
    lst1.append(num)

print('\nDigite os elementos da 2ª Lista:')
for i in range(10):
    num = int(input(f'Digite o {i+1}° N: '))
    lst2.append(num)

print(f'\nLista 1: {lst1}')
print(f'Lista 2: {lst2}')

# Intercalando a lista 3

lst3 = lst1 + lst2
lst3[::2] = lst1
lst3[1::2] = lst2 
print (f'\nA lista intercalada 3 é {lst3}')
