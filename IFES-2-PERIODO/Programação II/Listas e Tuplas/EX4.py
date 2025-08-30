print('4. Altere o programa anterior, intercalando 3 listas de 10 elementos cada.\n')

lst1 = []
lst2 = []
lst3 = []
lst4 = []

print('Digite os elementos da 1ª Lista:')
for i in range(10):
    num = int(input(f'Digite o {i+1}° N: '))
    lst1.append(num)

print('\nDigite os elementos da 2ª Lista:')
for i in range(10):
    num = int(input(f'Digite o {i+1}° N: '))
    lst2.append(num)

print('\nDigite os elementos da 3ª Lista:')
for i in range(10):
    num = int(input(f'Digite o {i+1}° N: '))
    lst3.append(num)

print(f'\nLista 1: {lst1}')
print(f'Lista 2: {lst2}')
print(f'Lista 3: {lst3}')

# Intercalando a lista 3

lst4 = lst1 + lst2 + lst3
lst4[::3] = lst1
lst4[1::3] = lst2
lst4[2::3] = lst3 
print (f'\nA lista intercalada 4 é {lst4}')