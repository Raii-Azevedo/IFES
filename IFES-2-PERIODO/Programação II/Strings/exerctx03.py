from unicodedata import normalize

text = ''

def semAcento(text):
    with open('conteudotexto.txt', 'r') as file:
        text = file.read()
    print('\033[1;33mTexto original:\033[0m')
    print(text)

    # ERRO AQUI
    out = normalize('NFKD', text.decode(codif)).encode('ASCII','ignore')
    print('\033[1;33mTexto modificado:\033[0m')
    print(out)


def main():
    semAcento(text)


if __name__ == '__main__':
    main()