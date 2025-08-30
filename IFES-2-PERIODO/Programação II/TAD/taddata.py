def criadata(intdia, intmes, intano):
  return [intdia, intmes, intano]

def criadata_str(str_ddmmaaaa):
  lst = str_ddmmaaaa.split("/")
  for i in range(len(lst)):
    lst[i] = int(lst[i])
  #  return criadata(lst[0],lst[1],lst[2])
  #  ou
  return lst

def getdia(vartaddata):
  return vartaddata[0]

def getmes(vartaddata):
  return vartaddata[1]

def getano(vartaddata):
  return vartaddata[2]

def cmpdata(dataA,dataB):
  numA = dataA[2] * 10000 + dataA[1] * 100 + dataA[0]
  numB = dataB[2] * 10000 + dataB[1] * 100 + dataB[0]

  if numA == numB:
    return 0
  elif numA > numB:
    return 1
  else:
    return -1
# fim cmpdata  

def parastr(vartaddata):
  s = "%02d/%02d/%d" % (vartaddata[0],vartaddata[1],vartaddata[2])
  return s

def diff(dataA,dataB):
  diasA = dataA[0] + dataA[1] * 30 + dataA[2] * 365
  diasB = dataB[0] + dataB[1] * 30 + dataB[2] * 365

  return abs(diasA - diasB)
# fim diff

def futuro(data,dias):
  qtdanos = dias//365
  restodias = dias % 365
  qtdmeses = restodias//30
  sobradias = restodias % 30

  data[2] = data[2] + qtdanos
  data[1] = data[1] + qtdmeses
  data[0] = data[0] + sobradias

  if data[0] > 30:
    data[0] = data[0] - 30
    data[1] = data[1] + 1

    if data[1] > 12:
      data[2] = data[2] + 1
      data[1] = 1

  return data
# fim futuro

def passado(data,dias):
  return None
# fim passado

def main():
  da = criadata_str("25/5/2023")
  novadata = futuro(da,29)
  print(parastr(novadata))
# fim main

if __name__ == "__main__":
  main()