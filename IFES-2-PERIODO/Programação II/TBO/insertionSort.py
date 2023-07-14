def insertion_sort(lista):
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
