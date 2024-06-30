def buscaBin(lst, alvo):
    
    # Busca Binária
    inicio = 0
    
    fim = len(lst) - 1
    
    achou = False
    
    while not achou and inicio <= fim: # O AND é importante para garantir que o inicio não assuma um N° maior que o fim da lista
        meio = inicio + (fim - inicio)//2
        print(inicio, meio, fim)

        if alvo == lst[meio]:
            achou = True
            
        else:
            if alvo > lst[meio]:
                inicio = meio + 1 # O novo inicio começa no MEIO + 1 posição
            else:
                fim = meio - 1 # Caso o elemento esteja na 1ª metade da lista somente o fim muda
        
    if achou:
        return meio
    else:
        return - 1


def main():
    lst = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alvo = input('Digite o nome para pesquisar na lista: ').capitalize()[0]

    indice = buscaBin(lst, alvo)

    if indice != -1:
        print(f'{alvo} encontrado na posição {indice}')
    else:
        print(f'{alvo} não encontrado na lista')
    
    
if __name__ == '__main__':
    main()