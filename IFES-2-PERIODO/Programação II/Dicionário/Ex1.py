def converte_2_txt(dic, n):

    if n in dic:
        return dic[n]

    else:
        aux = n
        n = abs(n) # Converte para absoluto para lidar com números negativos
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
                txtcentena = f'{dic[centena]} e '

        if dezena >= 2:
            txtdezena = dic[dezena * 10] 
            if unidade > 0:
                txtunidade = f'e {dic[unidade]}'
                
        elif dezena == 1:
            txtdezena = dic[10 + unidade]
        else:
            txtdezena = ''
            if unidade > 0:
                txtunidade = f'e {dic[unidade]}'
            else:
                txtunidade = 'zero'

        if aux < 0: # Números negativos
            txtnum = f'menos {txtcentena}{txtdezena} {txtunidade}'
        else:
            txtnum = f'{txtcentena}{txtdezena} {txtunidade}'

        return txtnum


def main():
    d = {0: 'zero', 1: 'um', 2: 'dois', 3: 'tres', 4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito',
         9: 'nove', 10: 'dez', 11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze', 16: 'dezesseis', 17: 'dezessete', 18: 'dezoito',
         19: 'dezenove', 20: 'vinte', 30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta', 70: 'setenta', 80: 'oitenta', 90: 'noventa',
         100: 'cento', 200: 'duzentos', 300: 'trezentos', 400: 'quatrocentos', 500: 'quinhentos', 600: 'seiscentos', 700:'setecentos',
         800:'oitocentos', 900:'novecentos'}
    
    num = int(input('Digite um número: '))
    print(converte_2_txt(d, num))


if __name__ == '__main__':
    main()
