import tadretangulo as tret

def tadRet(lst):
    with open ('boisxy.txt', 'rt') as arq:
        linha.

        

def ler_txt(nomearq):

    lst = []
    
    with open (nomearq, 'rt') as file:
        linha = file.readline().strip()

        while linha != '':
            tratado = linha.strip().split(',')
            lote = tret.cria(float(lst[1]), float(lst[2]), float(lst[3]), float(lst[4]))

            D = {"dono": lst[0], "lote": lote, "cont": 0}

            lst.append(D)
            
        file.close()


    return lst



def main():
    
    nomearq = 'lotes.txt'
    lst = ler_txt(nomearq)

    TAD = tadRet(lst)
  

if __name__ == '__main__':
    main()