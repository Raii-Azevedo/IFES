def linha_maior_valor(tab):
    maiorvalor = -1
    posmaiorvalor = 0
    for i in range(len(tab)):
        if tab[i][1] > maiorvalor:
            maiorvalor = tab[i][1]
            posmaiorvalor = i

    return tab[posmaiorvalor]

def print_linha_tab(lst):
    print("%-9s%8d%4s%5d%18s%5d%5d" % (lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6]))

def main():
    tabela = [
        ["janeiro",56,"a",3,"Pronto",4,2],
        ["fevereiro",7,"f",4,"Pronto",5,5],
        ["Março",400,"g",2,"Em andamento",6,7],
        ["Abril",6,"p",3,"Pronto",8,3],
        ["Maio",23,"v",4,"Pronto",3,6],
        ["Junho",90,"p",4,"Concluído",3,0]
    ]

    linhavalormax = linha_maior_valor(tabela)
    print_linha_tab(linhavalormax)    
# fim main

main()