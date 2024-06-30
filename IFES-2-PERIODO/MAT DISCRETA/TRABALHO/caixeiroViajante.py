# Algoritmo do caixeiro viajante
# Grupo: Lucas Lopes, Matheus Abreu, Raissa
# Professora: Adriana Lovatte
# Matéria: Matematica Discreta

nelementos = 0
MatrizA = []
caminho = []
ninfinito = 1

# Leitura da Matriz


def receber_matriz(ncidades):
	ncidades = 0
	global ninfinito, nelementos, MatrizA
	ncidades = int(input('Informe o número de cidades: '))
	print('Digite as Linhas da Matriz: ')
	# leitura das linhas da Matriz
	for i in range(ncidades):
		distancia = list(map(float, input().split()))
		MatrizA.append(distancia)
	# Calculando valores "infinitos"
	for distancia in distancias:
		ninfinito = ninfinito+distancia
	nelementos = ncidades  # variavel de inicio do número de elementos
	return None

# Encontrar o melhor caminho utilizando o Método do Vizinho Mais Próximo


def encontrar_caminho():
    global nelementos, ninfinito, caminho, MatrizA

    # vetor que registra os nós selecionados
    selecionar = [False for i in range(nelementos)]
    selecionar[0] = True  # Incluir nó 0 no caminho

    # Inicializar vetor de caminho
    caminho = [0 for i in range(nelementos+1)]

    for i in range(nelementos):
        selecionarVizinho = 0  # onde a cada repetição o 0 é selecionado
        melhorpeso = ninfinito

        for j in range(nelementos):
            # se a matriz de adjancencias for diferente de 0
            # e se melhor peso atual for maior que o custo de seguir para o nó j
            if not selecionar[j] and MatrizA[i][j] != 0 and melhorpeso > MatrizA[i][j]:
                selecionarVizinho = j  # nó j se torna o novo caminho
                # o novo melhor peso é o para nó j
                best_cost = ADJACENCE_MATRIX[i][j]

        # Acrecsentar o vizinho selecionado ao caminho
        caminho[i+1] = selecionarVizinho
        # registrar os vizinhos selecionados
        selecionar[selecionarVizinho] = True
    return None

# Calculando peso do melhor caminho


def calcular_peso(caminho):
    global nelementos, MatrizA
    peso = 0

    for i in range(nelementos):
        Ponto_A = caminho[i]
        Ponto_B = caminho[i+1]
        peso = peso + MatrizA[Ponto_A][Ponto_B]

    return peso

# Mostrar o melhor caminho


def mostrar_caminho():
    global caminho

    caminho = 'Caminho:'
    for i in range(len(caminho)):
        way += ' ' + str(caminho[i]+1) + ' '
        if i != len(caminho)-1:
            caminho += '->'

    print(caminho)
    return None

# Realização de swaps para melhorar a solução


def troca():
    global nelementos, caminho, MatrizA

    caminho_aux = caminho[:]  # armazenar o caminho em uma auxiliar para troca
    melhor_peso = calcular_peso(caminho)  # melhor custo atual

    for i in range(1, nelementos):
        for j in range(i+1, nelementos):
            # efetuando a troca
            caminho_aux[i], caminho_aux[j] = caminho_aux[j], caminho_aux[i]

            peso = calcular_peso(caminho_aux)

            if peso < melhor_peso:
                melhor_peso = peso
                caminho = caminho_aux[:]


def main():
	contador = 0
	ncidades = 0
	receber_matriz(ncidades)  # Ler e receber uma Matriz
	encontrar_caminho()  # Encontrar melhor caminho baseado no Método do Vizinho mais próximo

    # Realizando trocas a fim de melhorar o caminho

    while contador <=5:
		troca()
        contador=contador+1

    #Exibir resultados e conclusões
    mostrar_caminho()
    custo = calcular_peso(caminho)
    print('Custo: ', custo)

if __name__ == '__main__':
    main()
