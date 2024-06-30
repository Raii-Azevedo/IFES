def main():
    lst = ['mateus', 'gislany', 'paulo', 'marcos', 'maria']
    alvo = input('Digite o nome para pesquisar na lista: ').capitalize()

    achou = False

    i = 0
    
    while i < len(lst) and not achou:
        if alvo == lst[i]:
            achou = True
        i += 1

    if achou:
        print(f'{alvo} está na posição {i-1}')
    else:
        print(f'{alvo} não está na lista')

if __name__ == '__main__':
    main()