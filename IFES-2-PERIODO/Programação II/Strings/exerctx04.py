print('''4. Aprimore o programa do exercício 1 para incluir palavras compostas separadas 
por hífen: saci-pererê, micro-organismo, contra-ataque, etc''')
with open('conteudotexto.txt', 'r') as file:
    count = 0
    text = file.read()

    text = text.split()

    for i in text:
        count += 1

print(text)
print (f'\n\033[1;35mTotal de palavras {count}\033[0m')