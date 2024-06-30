print('''1.12.3. A conversão de graus Farenheit para centígrados é obtida por
C = 5 x (F - 32)
 9
Fazer um algoritmo que calcule e escreva uma tabela de centígrados em função de graus 
Farenheit, que variam de 50 a 150 de 1 em 1.\n''')
F = 50
print(f'°F to °C')
while F !=150+1:
    C = (F - 32) * 5/9
    print(f'{F:.2f}°F - {C:.2f}°C')
    F += 1

C = 50
print(f'\n°C to °F')
while C !=150+1:
    F = (C * 9/5) + 32
    print(f'{C:.2f}°C - {F:.2f}°F')
    C += 1
