import csv
import json

def json_to_json(nomearq): # DOCUMENTO JSON
    dict_2_json = {"dados": nomearq}
    with open('saida.json', 'w') as file:
        json.dump(dict_2_json, file, indent=4, sort_keys=True) # Indent 4 --> Formato JSON padrão
        file.close()


def json_to_dic_cpfs(nomearqjson):
    novo_dicionario = {}

    for dicionario in nomearqjson:
        cpf = dicionario.pop('cpf')  # Obtém o valor da chave 'placa'
        novo_dicionario[cpf] = dicionario  # Adiciona a placa como chave ao novo dicionário

    return novo_dicionario


def json_to_dic_placas(nomearqjson):
    novo_dicionario = {}

    for dicionario in nomearqjson:
        placa = dicionario.pop('placa')  # Obtém o valor da chave 'placa'
        novo_dicionario[placa] = dicionario  # Adiciona a placa como chave ao novo dicionário

    return novo_dicionario


def props_2_json(nomearq):
    json_data = []

    with open(nomearq, 'rt', encoding='utf-8') as file:  # UTF-8 Ler caracteres especiais
        reader = csv.reader(file)
        next(reader)  # Ignorar cabeçalho

        for linha in reader:
            linha_tratada = [item.strip().replace(";", ",") for item in linha]
            json_data.append(linha_tratada)

        json_tratado = []
        # Tratamento do Json_data, transformar em uma nova string a cada vírgula
        for linha in json_data:
            nova_linha = []
            for elemento in linha:
                elementos_separados = elemento.split(',')
                elementos_separados = [e.strip() for e in elementos_separados]
                nova_linha.extend(elementos_separados)
            json_tratado.append(nova_linha)

        json_final = []

        for linha in json_tratado:  # Dict com formato do JSON
            end = linha[2:7]  # Pega todos os elementos da lista de 2 a 7
            end_string = ', '.join(end) # Transforma numa longa string

            D = {
                "cpf": linha[0].strip(),
                "nome": linha[1].strip(),
                "end": end_string,
                "celular": linha[8].strip()
            }
            json_final.append(D)

        
            with open('bdproprietarios.json', 'w') as file:
                json.dump(json_final, file, indent=4, sort_keys=True)
                file.close()

    return json_final


def veiculos_2_json(nomearq):  # Função ler ARQ
    result = []

    with open(nomearq, 'rt') as file:
        reader = csv.reader(file)  # Lê o arq CSV
        next(reader)  # Ignora o cabeçalho

        for linha in reader:  # Dict com formato do JSON
            D = {
                "placa": linha[0].strip(),
                "modelo": linha[1].strip(),
                "marca": linha[2].strip(),
                "quilometragem": linha[3].strip()
            }
            result.append(D)

            with open('bdveiculos.json', 'w') as file:
                json.dump(result, file, indent=4, sort_keys=True)
                file.close()

    return result


def main():
    nomearq= 'bdveiculos.csv'
    D = veiculos_2_json(nomearq)

    nomearq = 'bdproprietarios.csv'

    J = props_2_json(nomearq)

    PLACA = json_to_dic_placas(D)
    CPF = json_to_dic_cpfs(J)

    nomearq = PLACA
    json_to_json(PLACA)

    print('-- PROCESSAMENTO FINALIZADO --')

if __name__ == '__main__':
    main()
