print('''7. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um 
crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no
crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada 
como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso 
contrário, ele será classificado como "Inocente".\n''')

print('RELATÓRIO DE UM CRIME\n')
menu = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?" ]
suspeito = 0
print('INTERROGATÓRIO')
for i in range(len(menu)):
    R = input(f'{menu[i]} [S/N]: ').upper().split()[0]
    if R == 'S':
        suspeito += 1

print('\nRELATÓRIO FINAL: ')
if suspeito == 0:
    print('INOCENTE')
elif suspeito == 1 or suspeito == 2:
    print('SUPEITO')
elif suspeito == 3 or suspeito == 4:
    print('CÚMPLICE')
else:
    print('ASSASSINO')
