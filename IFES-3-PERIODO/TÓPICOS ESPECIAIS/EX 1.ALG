Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 14/10/2023
Var
dia : inteiro
valor: real
teste : logico

Inicio
Escreva("Digite o dia da semana ( 1 at� 7): ")
Leia (dia)
teste <- falso
escolha(dia)
caso 1
valor<- 10.0
caso 2
valor<- 5.0
caso 3
valor<- 6.0
caso 4
valor<- 7.0
caso 5
valor<- 8.0
caso 6
valor<- 9.0
caso 7
valor<- 10.0
outrocaso
teste <- verdadeiro
fimescolha
se (teste = verdadeiro) entao
escreval(" Dia da semana inv�lido")
senao
Escreval(" Valor = ", valor)
fimse
FimAlgoritmo