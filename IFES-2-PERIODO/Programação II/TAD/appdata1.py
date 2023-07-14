import taddata as td

def main():
  arqin = open("dadosboleto.txt","rt")
  linha = arqin.readline().strip()

  print("COD. VALOR DT VENC. DT PGTO. ATRASO JUROS VALOR FINAL")

  while(linha != ""):
    lst = linha.split(",")
    dtavenc = td.criadata_str(lst[2])
    dtapgto = td.criadata_str(lst[3])
    qtddias = td.diff(dtapgto,dtavenc)
    valor_boleto = float(lst[1])
    juro_diario = float(lst[4])
    msg = ""

    if (td.cmpdata(dtavenc,dtapgto) == 1) or (td.cmpdata(dtavenc,dtapgto) == 0):
      val_final_bol = valor_boleto
      msg = "Sem atraso!"
    else:
      val_final_bol = valor_boleto + ((qtddias * juro_diario/100) * valor_boleto)
      msg = str(qtddias) + " dias de atraso!"

    strsaida = "%s%10.2f%15s%15s%25s%10.1f%15.2f" %\
               (lst[0],valor_boleto,td.parastr(dtavenc),\
               td.parastr(dtapgto),msg,juro_diario,val_final_bol)
    print(strsaida)
    linha = arqin.readline().strip()
  # fim while

  arqin.close()
# fim main

main()