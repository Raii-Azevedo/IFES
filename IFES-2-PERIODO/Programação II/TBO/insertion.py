"""O loop for percorre a lista a partir do segundo elemento (índice 1) até o último elemento. 
A cada iteração, o elemento atual é armazenado na variável k e o índice anterior é armazenado na variável 
j.
O loop while é executado enquanto j é maior ou igual a zero e o elemento na posição j é maior que 
o valor temporário k. Dentro desse loop, o elemento atual (lst[j]) é movido para a direita (lst[j+1]) 
para abrir espaço para o valor temporário ser inserido na posição correta.

Depois de sair do loop while, o valor temporário k é inserido na posição correta, que é lst[j+1]."""

def main():
    lst = [7, 8, 5, 2, 4, 6, 3]

    print(lst)

    for i in range(1, len(lst)):
        k = lst[i]
        j = i - 1

        while j >= 0 and lst[j] > k : # Para indicar o J parar a ordenação da lista ao encontrar um elemento menor que ele
            lst[j+1] = lst[j] # Deslocamento do elemento +1 para o J.
            j -= 1

            lst [j+1] = k # Salva temporariamento o elemento que perde a posição
    
    print(lst)


if __name__ == '__main__':
    main()