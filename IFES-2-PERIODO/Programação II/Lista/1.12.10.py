print('''1.12.10. Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma certa 
cidade, num determinado dia. Para cada casa visitada, é fornecido o número do canal 
(4,5,7,12) e o número de pessoas que o estavam assistindo naquela casa. Se a televisão 
estivesse desligada, nada era anotado, ou seja, esta casa não entrava na pesquisa. Fazer um 
algoritmo que:
- leia um número indeterminado de dados, sendo que o “FLAG” corresponde ao número do 
canal igual a zero;
- calcule a porcentagem de audiência para cada emissora;
- escreva o número do canal e a sua respectiva porcentagem.\n''')



def main():
    canal = int(input('Digite o canal de preferência [4|5|7|12]: '))
    count = sete = quatro = doze = cinco =  0

    while canal != 0:
        if canal == 4:
            quatro += 1
        if canal == 5:
            cinco += 1
        if canal == 7:
            sete += 1
        if canal == 12:
            doze += 1
        count += 1
        canal = int(input('Digite o canal de preferência [4|5|7|12]: '))
    

    print(f'\nCanal 4: {quatro} telespectadores = {(quatro*100)/count:.2f}%')
    print(f'\nCanal 5: {cinco} telespectadores = {(cinco*100)/count:.2f}%')
    print(f'\nCanal 7: {sete} telespectadores = {(sete*100)/count:.2f}%')
    print(f'\nCanal 12: {doze} telespectadores = {(doze*100)/count:.2f}%')

    
if __name__ == "__main__":
    main()
