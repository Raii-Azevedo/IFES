print(''''1.12.5. Supondo que a população de um país A seja da ordem de 90.000.000 de habitantes 
com uma taxa anual de crescimento de 3% e que a população de um país B seja, 
aproximadamente, de 20.000.000 de habitantes com uma taxa anual de crescimento de 1,5%, 
fazer um algoritmo que calcule e escreva o número de anos necessários para que a população 
do país A ultrapasse ou iguale a população do país B, mantidas essas taxas de crescimento.\n''')

popA = 90000000
popB = 20000000

cresA = (3/100)
cresB = (15/100)

count = 0

while popB != popA:
    popA = popA * cresA
    popB = popB * cresB

    print(f'{count} => A = {popA} - B = {popB}')

    count += 1

print(f'A população B {popB} se igualará a A {popA} em {count} anos')
