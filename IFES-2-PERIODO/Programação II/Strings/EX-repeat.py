def repetidas(lst):
    lst_palavra = []
    lista_contadores = [0] * len(lst)

    for palavra in lst:
        if palavra not in lst_palavra:
            lst_palavra.append(palavra)
            lista_contadores.append(1)
        else:
            pos = lst_palavra.index(palavra)
            lista_contadores += 1

        return lst_palavra
    
    for i in range(len(lst_palavra)):
        print(f"A palavra '{lst_palavra[i]}' apareceu {lista_contadores[i]} vezes na lista.")
    
repetidas(lst)
