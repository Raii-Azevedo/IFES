def main():
    print('''4) Escreva uma função que recebe por parâmetro a seguinte lista denotas escolares 
    [73, 67,38 ,33]. A função deve percorrer a lista de notas,aplicando as seguintes regras e 
    retornar as notas finais.
    
    Regras:
    ● Se a diferença entre uma nota e o próximo número múltiplo de 5 for menor que 3, 
    arredonde a nota para o próximo múltiplo de 5
    
    ● Se a nota for menor que 38 nada acontece com a nota.
    
    Exemplos: Se uma nota for igual a 84, seu próximo múltiplo de 5 é 85, logo a nota será 
    arredondada para para 85, pois a diferença (85-84) é menor que 3.''')

    N = [73, 67, 38, 33]
    NF = []
    for nota in N:
        if nota < 38:
            NF.append(nota)
        else:
            multiplo_5 = (nota // 5 + 1) * 5
            dif = multiplo_5 - nota
            if dif < 3:
                NF.append(multiplo_5)
            else:
                NF.append(nota)
    print(N)
    print(NF)

if __name__ == '__main__':
    main()
