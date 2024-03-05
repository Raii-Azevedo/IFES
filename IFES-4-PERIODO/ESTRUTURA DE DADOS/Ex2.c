#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ALUNOS 30

struct Aluno {
    int matricula;
    char nome[100];
    int polo;
};

struct Aluno fila[MAX_ALUNOS];
int tamfila = 0;

void inserir() {
    int continuar;
    do {
        printf("\nChegada de novo aluno na fila\n");
        printf("\nNumero da Matricula: ");
        scanf("%d", &fila[tamfila].matricula);
        printf("\nNome: ");
        scanf(" %[^\n]s", fila[tamfila].nome);
        printf("\nPolo do Aluno(1- Batalha, 2-Valenca): ");
        scanf("%d", &fila[tamfila].polo);

        if (tamfila < MAX_ALUNOS) {
            tamfila++;
            printf("\n\nAluno Inserido com Sucesso!!!!\n\n");
        } else {
            printf("\n\nFila cheia, Aluno nao inserido!!!!\n\n");
        }

        printf("Continuar inserindo (1-sim/2-nao)? ");
        scanf("%d", &continuar);
    } while (continuar == 1);
}

void consultar_primeiro() {
    if (tamfila > 0) {
        printf("O nome do primeiro aluno na fila é: %s\n", fila[0].nome);
    } else {
        printf("A fila está vazia.\n");
    }
}

int main() {
    inserir();

    // Supondo que a inserção de alunos na fila já tenha sido feita

    consultar_primeiro();

    return 0;
}
