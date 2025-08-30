# É chamado String qualquer coleção de caracteres entre aspas duplas ou simples. è possível criar um variável, concatenar, percorrer e fatiar uma string.

s = "Ifes Campus Serra"
print(s[3:8])
sa = "Ifes"
sa += ' ' + "Serra"
print(sa)
a = "João da Silva, 25 anos, Goiabeiras, A+"

# O método SPLIT vai usar um separador, no caso a vírgula e colocar em cada posição da lista.
lst = a.split(",")
print(lst)

# O método STRIP vai eliminar os espaços desnecessários 
b= "    \n\n\n Goiaba   \n\n\n"
b.strip()
print(b)

#Para modificar a string, com um caracterer específico, é preciso uma função Auxiliar
s = "João da Silva Medeiros"
aux = s[0:8] + "s" + s[9:]
print(aux)


# COMANDOS PARA TRATAR PALAVRAS
s = "Ifes campus serra!!"
s1 = "yfdskfdhfo"
print(s1.isalpha()) # Indica se todos os caracteres são Letras

s2 = "565"
print(s2.isdigit()) # Indica se todos os caracteres são números

s3 = "ifes@campus123"
print(s3.isalnum()) # Vai indicar falso devido o @

