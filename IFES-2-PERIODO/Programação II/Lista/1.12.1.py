print('''\033[1;33mFazer um algoritmo que:
- Leia um número indeterminado de linhas contendo cada uma a idade de um indivíduo. A 
última linha que não entrará nos cálculos, contém o valor da idade igual a zero. Calcule e 
escreva a idade média deste grupo de indivíduos.\033[0m\n''')
print('     MÉDIA IDADE ')

def main():
    count = 0
    idade = int(input("Digite a idade: "))
    while idade != 0:
        idade = int(input("Digite a idade: "))
        idade += idade
        count +=1 

    media = idade/count
    
    print(f'\nMédia de idade: {media}')
    


if __name__ == '__main__':
    main()
