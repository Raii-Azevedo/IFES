def main():

    print('''1) Ler 2 valores inteiros garantindo que o segundo valor lido será sempre maior 
    que o primeiro valor lido. Calcule e escreva a soma dos inteiros existentes entre 
    os 2 valores lidos (incluindo os valores lidos).''')
    
    v1 = int(input("Digite o 1º valor inteiro: "))
    v2 = int(input("Digite o 2º valor inteiro (maior que o primeiro): "))


    while v2 <= v1:
        print("O 2° valor deve ser maior que o 1º. Tente novamente.")
        v2 = int(input("Digite o segundo valor inteiro (maior que o primeiro): "))

    soma = 0
    for num in range(v1 + 1, v2):
        soma += num
        print(num)

    print(f"A soma dos inteiros entre {v1} e {v2} é: {soma}")


if __name__ == '__main__':
    main()