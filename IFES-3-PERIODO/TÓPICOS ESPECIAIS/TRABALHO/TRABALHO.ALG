Algoritmo "NOTA ALUNO"
// Disciplina   : [Topicos Especiais]
// Autor(a)    : Raissa Azevedo
// Data atual  : 23/10/2023
Var
   nome: Caractere
   nota1, nota2, nota3, soma: Real

Inicio
   Escreva("Digite o nome do aluno: ")
   Leia(nome)

   // Nota 1
   Repita
      Escreva("Digite a nota 1 (0 a 10): ")
      Leia(nota1)
   Ate (nota1 >= 0) E (nota1 <= 10)

   // Nota 2
   Repita
      Escreva("Digite a nota 2 (0 a 10): ")
      Leia(nota2)
   Ate (nota2 >= 0) E (nota2 <= 10)

   // Nota 3
   Repita
      Escreva("Digite a nota 3 (0 a 10): ")
      Leia(nota3)
   Ate (nota3 >= 0) E (nota3 <= 10)

   // Soma
   soma <- nota1 + nota2 + nota3

   // Verifica��o
   Se soma >= 18 Entao
      Escreva("O(a) aluno(a) ", nome, " foi APROVADO com nota igual a ", soma)
   Senao
      Escreva("O(a) aluno(a) ", nome, " foi REPROVADO com nota igual a ", soma)
   FimSe

FimAlgoritmo