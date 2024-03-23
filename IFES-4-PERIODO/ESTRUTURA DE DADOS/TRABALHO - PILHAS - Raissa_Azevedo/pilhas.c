#include <stdio.h>
#include <stdlib.h>

#define TAMANHO_MAX 100

struct Pilha {
    int topo;
    int itens[TAMANHO_MAX];
};

void empilhar(struct Pilha *p, int valor) {
    if (p->topo < TAMANHO_MAX) {
        p->itens[p->topo] = valor;
        p->topo++;
    } else {
        printf("\nPILHA CHEIA!\n");
    }
}

int desempilhar(struct Pilha *p) {
    int valor = 0;
    if (p->topo > 0) {
        p->topo--;
        valor = p->itens[p->topo];
    } else {
        printf("\nPILHA VAZIA!\n");
    }
    return valor;
}

int retornatopo(struct Pilha *p) {
    int valor = 0;
    if (p->topo > 0) {
        valor = p->itens[p->topo - 1];
    } else {
        printf("\nPILHA VAZIA!\n");
    }
    return valor;
}

int main() {
    struct Pilha minhapilha;
    minhapilha.topo = 0;
    int op;
    int valor;

    while (1) {
        printf("\n1 - Empilhar(push)\n");
        printf("2 - Desempilhar(POP)\n");
        printf("3 - Mostrar o topo\n");
        printf("4 - Sair\n");
        printf("\nOpção? ");
        scanf("%d", &op);

        switch (op) {
            case 1: // push
                printf("\nDigite o valor a ser empilhado: ");
                scanf("%d", &valor);
                empilhar(&minhapilha, valor);
                break;

            case 2: // pop
                valor = desempilhar(&minhapilha);
                if (valor != 0) {
                    printf("\n%d DESEMPILHADO!\n", valor);
                }
                break;

            case 3: // mostrar topo
                valor = retornatopo(&minhapilha);
                if (valor != 0) {
                    printf("\nTOPO: %d\n", valor);
                }
                break;

            case 4:
                exit(0);

            default:
                printf("\nOPÇÃO INVÁLIDA\n");
        }
    }

    return 0;
}
