def main():

    final = []
    atleta = ()

    nome = input('Nome do Atleta: ')
    while nome != '':
        atleta = (nome,)
        for i in range(3):
            salto = float(input(f'Entre com o valor do {i+1}º salto m²: '))
            atleta += (salto,)
        nome = input('Nome do Atleta: ')
        
        final.append(atleta)
    

    print(f'Lista de atletas: {final}')
    
        
if __name__ == '__main__':
    main()
