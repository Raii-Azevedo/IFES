def main():
    ca,cb,cc,cd,ce,cf,cg,ch,ci = 0,0,0,0,0,0,0,0,0

    # SUPOR QUE EMPRESA POSSUI 10 FUNCIONÁRIOS
    for i in range(10):
        totalvendas = float(input(f'Entre com o total de vendas do {i+1} funcionário: '))
        salario = 200 + totalvendas * 0.09
        if salario >= 200 and salario <= 299:
            ca += 1
        elif salario >= 300 and salario <= 399:
            cb += 1
        elif salario >= 400 and salario <= 499:
            cc += 1
        elif salario >= 500 and salario <= 599:
            cd += 1
        elif salario >= 600 and salario <= 699:
            ce += 1
        elif salario >= 700 and salario <= 799:
            cf += 1
        elif salario >= 800 and salario <= 899:
            cb += 1
        elif salario >= 900 and salario <= 999:
            ch += 1
        else:
            ci += 1
    
    print(' Quantidade de salários dentro das faixas: ')
    print(f'Faixa A: {ca}')
    print(f'Faixa B: {cb}')
    print(f'Faixa C: {cc}')
    print(f'Faixa D: {cd}')
    print(f'Faixa E: {ce}')
    print(f'Faixa F: {cf}')
    print(f'Faixa G: {cg}')
    print(f'Faixa H: {ch}')
    print(f'Faixa I: {ci}')



if __name__ == '__main__':
    main()