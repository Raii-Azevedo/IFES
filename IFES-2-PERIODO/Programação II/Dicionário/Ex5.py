def soma_lst(lista):
    soma = 0
    for i in lista:
        soma += i

    return soma

def int2romanos(dic, roman): # Função para localizar os algarismo Romanos => INT e guardar numa LST
    lst = []
    valint = 0
    subvalid = [4,9,40,90,400,900] # Valores de subtração válidos em Algarismos Romanos

    for valor in roman:
        if valor not in dic:
            return "Valor romano inválido"
        else:
            valint = dic[valor]
            if lst == []:
                lst.append(valint)
            else:
                if lst[-1] >= valint: # Verifica se o último número é maior ou igual ao valor informado
                    lst.append(valint)
                else:
                    sub = valint - lst[-1] 
                    if sub in subvalid: # Verifica se a subtração está dentro dos valores válidos de SUBVALID
                        lst[-1] = sub
                    else: # Gerou uma subtração Inválida
                        valint = -1
                        break

    return lst


def main():
    d = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    v = input('Digite um número em Algarismos Romanos para ver em Arábico: ').upper()
    
    lst = int2romanos(d, v)

    soma = soma_lst(lst)

    print(f'O algarismo romano: {v}, equivale ao número: {soma}')


if __name__ == '__main__':
    main()
