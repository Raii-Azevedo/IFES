Algoritmo "semnome"
//Sabendo que uma rede hoteleira deseja informatizar sua folha de pagamento,
//desenvolva em pseudoc�digo uma solu��o conforme regras apresentadas pela
//empresa, de acordo com as especifica��es abaixo:

//O funcion�rio possui os seguintes dados de entrada: c�digo, n�mero de horas
//trabalhadas no m�s, turno de trabalho (M � matutino, V � vespertino ou N �
//noturno), categoria (F � funcion�rio, G � gerente).

//Fa�a um algoritmo que:

//- Leia as informa��es dos funcion�rios: c�digo (inteiro), n�mero de horas
//trabalhadas (inteiro) no m�s, turno (caractere) e categoria (caractere).
//N�o leia somente o valor da hora trabalhada (real), pois ser� calculada.

//- Considere sempre a digita��o de uma �nica letra para representar o turno
//de trabalho e a categoria do funcion�rio, conforme as tabelas:


Var
 codigo, n_horas: inteiro
 turno, categoria: caractere
 valor: real

Inicio
Escreva("C�digo: ")
Leia(codigo)
Escreva("N� de Horas trabalhadas: ")
Leia(n_horas)
Escreva("Turno: ")
Leia(turno)
Escreva("Categoria: ")
Leia(categoria)
Escreva("Valor hora trabalhada R$: ")
Leia(valor)

Escreval("O funcion�rio c�digo:",codigo, " Categoria:",categoria, " do Turno", turno)
Escreval(" Trabalhou um total de ",n_horas," horas a um valor de R$ ",valor, "a hora ")
Escreval(" Totalizando R$ ", valor*n_horas)

Fimalgoritmo