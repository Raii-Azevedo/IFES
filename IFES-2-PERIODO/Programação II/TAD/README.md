MÓDULOS

Arquivo .py que possui o main.py(sistema) e módulos (preenchidos com bibliotecas ou API) ou TAD (Tipo Abstrato de Dados).

- INSERTION SORT -
  
7 8 5 2 4 6 3

"9" > "100" -> A string 9 é maior que 100, porque o caractere 9 é maior....
Assim como:
"C" > "abacate" porque C é maior que A.

O Insertion Sort é um algoritmo de classificação simples que percorre uma lista de elementos e os insere em sua posição correta. Ele começa com o segundo elemento da lista e compara com os elementos anteriores, movendo-os para a direita até encontrar a posição correta.

Aqui está um resumo do algoritmo de Insertion Sort em Python:

Comece percorrendo a lista a partir do segundo elemento (índice 1) até o último elemento (índice n-1), onde n é o tamanho da lista.

Para cada elemento, armazene seu valor em uma variável temporária.

Compare o elemento atual com os elementos anteriores (começando pelo índice atual - 1) até encontrar a posição correta para inserir o elemento.

Enquanto o valor do elemento anterior for maior que o valor temporário e o índice atual for maior ou igual a 0, mova o elemento anterior para a direita.

Quando encontrar a posição correta, insira o valor temporário no índice atual.

Repita os passos 2 a 5 para todos os elementos da lista.

Após percorrer todos os elementos, a lista estará ordenada.

Aqui está um exemplo de implementação do Insertion Sort em Python:

#### def insertion_sort(lista):
    for i in range(1, len(lista)):
        valor_temporario = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > valor_temporario:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor_temporario

# Exemplo de uso
lista = [5, 2, 8, 12, 1]
insertion_sort(lista)
print(lista)  # Saída: [1, 2, 5, 8, 12]

- Nesse exemplo, a função insertion_sort recebe uma lista como entrada e a ordena utilizando o algoritmo de Insertion Sort. Ao final, a lista é impressa para verificar a ordenação correta.
