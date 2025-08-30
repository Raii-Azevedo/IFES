def main():
    nome = input('Digite o nome do aluno(a): ')
    notas = []

    for n in range(3):
        nota = float(input(f'Digite a {n+1}ª nota: '))
        while nota < 0 or nota > 10:
            print("Nota inválida. A nota deve estar entre 0 e 10.\n")
            nota = float(input(f'Digite a {n+1}ª nota: '))
        notas.append(nota)

    print("Notas digitadas:", notas)
    final = sum(notas)

    # BLOCO DD BOLETIM FINAL
    if final >= 18:
        print(f'O aluno {nome} está APROVADO com nota: {final}')
    elif final < 15:
        print(f'O aluno {nome} está REPROVADO com nota: {final}')
    else:
        print(f'O aluno {nome} está RECUPERAÇÃO com nota: {final}')


if __name__ == '__main__':
    main()

