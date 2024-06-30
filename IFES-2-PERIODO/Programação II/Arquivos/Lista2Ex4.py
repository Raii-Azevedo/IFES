def filtro(lst, marca): # Percorrer a lista e gravar no arquivo separando por marca
    



def main():
    aux = []
    veiculos = []
    with open ('bdveiculos.txt', 'rt') as file:
        arq = file.readline()

        while arq != "":
            aux.append(arq.strip())
            arq = file.readline()
        file.close()

        for i in range(0, len(aux), 4):
            carros = aux[i:i+4]
            veiculos.append(carros)

        print(veiculos)

        # CATALOGANDO OS CARROS

        filtro(veiculos)

if __name__ == '__main__':
    main()