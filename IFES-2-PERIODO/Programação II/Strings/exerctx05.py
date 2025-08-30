print('''5. Altere o programa exerctxt01.py para exibir (na mesma linha) somente nomes
compostos por 1 ou mais partes que possuam inicial maiúscula (nomes próprios de
pessoas, lugares, empresas, etc.). Exemplos: Caixa Econômica, Lojas Americanas,
Casas Bahia, Fernanda Montenegro, Tony Stark, Anita, etc.\n''')
def novoprint(text):
    novo = []
    for palavra in text:
        if palavra[0].isupper() and len(palavra) > 1:
            novo.append(palavra)
    return ' '.join(novo)


def main():
    with open('conteudotexto.txt', 'r') as file:
        text = file.read()

        text = text.split()

    #print(text)

    novo = novoprint(text)

    print(novo)

if __name__ == '__main__':
    main()

