Algoritmo "semnome"
//Sabendo que uma rede hoteleira deseja informatizar sua folha de pagamento,
//desenvolva em pseudocódigo uma solução conforme regras apresentadas pela
//empresa, de acordo com as especificações abaixo:

//O funcionário possui os seguintes dados de entrada: código, número de horas
//trabalhadas no mês, turno de trabalho (M – matutino, V – vespertino ou N –
//noturno), categoria (F – funcionário, G – gerente).

//Faça um algoritmo que:

//- Leia as informações dos funcionários: código (inteiro), número de horas
//trabalhadas (inteiro) no mês, turno (caractere) e categoria (caractere).
//Não leia somente o valor da hora trabalhada (real), pois será calculada.

//- Considere sempre a digitação de uma única letra para representar o turno
//de trabalho e a categoria do funcionário, conforme as tabelas:


Var
 codigo, n_horas: inteiro
 turno, categoria: caractere
 valor: real

Inicio
Escreva("Código: ")
Leia(codigo)
Escreva("Nº de Horas trabalhadas: ")
Leia(n_horas)
Escreva("Turno: ")
Leia(turno)
Escreva("Categoria: ")
Leia(categoria)
Escreva("Valor hora trabalhada R$: ")
Leia(valor)

Escreval("O funcionário código:",codigo, " Categoria:",categoria, " do Turno", turno)
Escreval(" Trabalhou um total de ",n_horas," horas a um valor de R$ ",valor, "a hora ")
Escreval(" Totalizando R$ ", valor*n_horas)

Fimalgoritmo