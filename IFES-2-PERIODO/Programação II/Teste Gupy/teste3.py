from random import randint

def main():
    print('''3) Faça um algoritmo para ler 50 números e armazenar em uma lista,
    verificar e escrever se existem números repetidos na lista e em que posições se encontram.''')


    lst = []
    repetido = []

    # N° aleatórios na lista
    i = 0
    while i != 50:
        N = randint(0, 99)
        lst.append(N)
        i += 1

    # Verificando repetidos
    print(lst)
    for num in lst:
        if lst.count(num) > 1 and num not in repetido:
            repetido.append(num)
            pos = []
            for i in range(len(lst)):
                if lst[i] == num:
                    pos.append(i)
            print(f"O número {num} se repete nas posições: {pos}")


if __name__ == '__main__':
    main()
