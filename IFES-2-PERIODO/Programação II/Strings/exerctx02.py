text = ''

def normalizaSPC(text):

    with open('conteudotexto.txt', 'r') as file:
        text = file.read()

    print('\033[1;33mTexto original:\033[0m')
    print(text)

    text = text.strip()
    print('\033[1;33mTexto modificado: \033[0m')
    print(text)

           
def main():
    normalizaSPC(text)


if __name__ == '__main__':
    main()
