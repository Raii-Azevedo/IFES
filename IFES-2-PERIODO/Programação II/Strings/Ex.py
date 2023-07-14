# Construa uma função que recebe uma string contendo um texto qualquer e retorne uma lista das palavras encontradas no texto.
# Limpar a sujeira no meio da palavra
# Remover palavras repetidas - Contar essas palavras e indicar!
# Retirar os vazios (limpeza nos erro gramaticais)

def faxina(palavra): # Menos eficiente
    if palavra.isalnum():
        return palavra
    else: # Utilizar fatiamento para eliminar o caractere que está no final
        return palavra[:-1]
    
def faxina2(palavra): # Mais eficiente
    while not palavra[-1].isalnum():  # Utilizar fatiamento para eliminar o caractere que está no final. O palavra[-1] indica que quero eliminar só a sujeira do final da palavra, não no meio
        palavra = palavra[:-1]
    while palavra != '' and not palavra[0].isalnum():
        palavra = palavra[1:]

    return palavra.lower()
    
def print_palavras(lista):
    for palavra in lista:
        print(palavra)

def separa(txt):
    lst = txt.split() # Assume que o separador é o espaço, 1 caractere espaço.

    for i in range(len(lst)):
        lst[i] = faxina2(lst[i])
    return lst


def print_contagem(lst_pl, lst_cont):
    for i in range(len(lst_pl)):
        print("%50s%8d" % (lst_pl[i], lst_cont[i]))


def repetidas(lst):
    lst_palavras = []
    lista_contadores = []

    for palavra in lst:
        if palavra in lst_palavras:
            pos = lst_palavras.index(palavra)
            lista_contadores[pos] += 1
        else:
            lst_palavras.append(palavra)
            lista_contadores.append(1)

    return lst_palavras, lista_contadores

def main():
    s = open('conteudotexto.txt', 'rt').read()

    lst_palavras = separa(s)

    print_palavras(lst_palavras)

    print(f'Foram encontradas {len(lst_palavras)} palavras na lista')

    lst_palavras, lista_contadores = repetidas(lst_palavras)
    
    print_contagem(lst_palavras, lista_contadores)

if __name__ == "__main__":
    main()
    
# PARA CRIAR UM ARQUIVO TXT DIRETO DO TERMINAL
# Ex.py" > contagem.txt
