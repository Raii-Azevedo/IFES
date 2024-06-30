import json

def main():
  # RECUPERAÇÃO DOS DADOS JSON
  arqjsonIN = open("saida.json", "rt")
  dicjsonIN = json.load(arqjsonIN)
  arqjsonIN.close()

  # PROCESSAMENTO DOS DADOS
  lst = dicjsonIN["dados"] # {"74647536": ["num12", "num 34", ....]}

  d = {}

  for dicrua in lst:
    c_e_p = dicrua["cep"] 
    if c_e_p in d:
      d[c_e_p].append(dicrua["numero"])
    else:
      d[c_e_p] = [dicrua["numero"]]
  # for dicrua

  # CRIANDO ARQ JSON COM RESULTADO DO PROCESSAMENTO.
  arqjsonOUT = open("saidaEXE7.json", "wt")
  json.dump(d,arqjsonOUT,indent=4, sort_keys=True)
  arqjsonOUT.close()

  print("Processamento concluído!!!")
# fim main

main()
