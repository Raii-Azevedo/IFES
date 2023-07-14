import json
print(f'''Construa um programa pyhton que receba como entrada o arquivo JSON "saidaExec.json" e gere como saída
o arquvo "exec7.json". O arquivo deve seguir a seguinte estrutura para cada dado:
''')

def jsonEstruturado(dicJSON):
    lst = dicJSON['dados']

    D = {}
    
    for dicrua in lst:
        CEP = dicrua['cep']
        
        if CEP in D:
            D[CEP].append(dicrua['numero'])
        else:
            D[CEP] = [dicrua['numero']]



def txt_2_json():
    fileJSON = open("saidaexec.json", "rt")

    dicJSON = json.load(fileJSON)

    fileJSON.close()

    return dicJSON


def main():
    dicJSON = txt_2_json()

    print('Processamento concluído')

    jsonEstruturado(dicJSON)


if __name__ == '__main__':
    main()
