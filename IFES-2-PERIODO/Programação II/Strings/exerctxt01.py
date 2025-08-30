print('''\033[1;32m Construir um programa python (CUPP) que processe uma string chamado texto.
O programa deve se chamar exerctxt01.py. O conteúdo de texto pode ser acessado
por meio da importação do arquivo conteudotexto.py. O conteúdo deste arquivo
pode ser alterado por você. A teoria por trás de módulos e imports será vista em
breve. Por hora basta reproduzir o código, modificar e acessar o texto na aplicação
exerctxt01.py.\033[1;31m''')

print()

with open('conteudotexto.txt', 'r') as file:
    count = 0
    text = file.read()

    text = text.split()

    for i in text:
        count += 1

print(text)
print (f'\n\033[1;35mTotal de palavras {count}\033[0m')
