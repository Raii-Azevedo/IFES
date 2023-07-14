def converte_num_txt(dic, n):
     if n in dic:
        return dic[n]

     else:
        aux = n
        n = abs(n)  # Converte para absoluto para lidar com números negativos
        dezena = (n // 10) % 10
        unidade = (n % 10)
        centena = (n // 100) * 100

        txtcentena = ''
        txtdezena = ''
        txtunidade = ''

        if centena > 0:
            if centena == 100 and dezena == 0 and unidade == 0:
                txtcentena = dic[centena]
            else:
                txtcentena = f'{dic[centena]}'

        if dezena >= 2:
            txtdezena = dic[dezena * 10]
            if unidade > 0:
                txtunidade = f'{dic[unidade]}'

        elif dezena == 1:
            txtdezena = dic[10 + unidade]
        else:
            if unidade > 0:
                txtunidade = f'{dic[unidade]}'
            else:
                txtunidade = 'zero'

        if aux < 0:  # Números negativos
            txtnum = f'- {txtcentena}{txtdezena} {txtunidade}'
        else:
            txtnum = f'{txtcentena}{txtdezena} {txtunidade}'

        return txtnum



def main():
    d = { 0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 
         11: 'XI', 12: 'XII', 13: 'XIII', 14:'XIV', 15: 'XV', 16:'XVI', 17:'XVII', 18:'XVIII', 19:'XIX', 20: 'XX', 30: 'XXX',
         40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 
         700: 'DCC', 800: 'DCCC', 900: 'CM' }

    
    num = int(input('Digite um número para ver em Algarismos Romanos: '))
    print(converte_num_txt(d, num))

if __name__ == '__main__':
    main()