#include <stdio.h>
#include <stdlib.h>

#define TAMANHO_MAX 100

struct Pilha {
    int topo;
    float itens[TAMANHO_MAX];
};

void empilhar(struct Pilha *p, float valor) {
    if (p->topo < TAMANHO_MAX) {
        p->itens[p->topo] = valor;
        p->topo++;
    } else {
        printf("\nPILHA CHEIA!\n");
    }
}

float desempilhar(struct Pilha *p) {
    float valor = 0.0;
    if (p->topo > 0) {
        p->topo--;
        valor = p->itens[p->topo];
    } else {
        printf("\nPILHA VAZIA!\n");
    }
    return valor;
}

float retornatopo(struct Pilha *p) {
    float valor = 0.0;
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
    float valor;

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
                scanf("%f", &valor);
                empilhar(&minhapilha, valor);
                break;

            case 2: // pop
                valor = desempilhar(&minhapilha);
                if (valor != 0.0) {
                    printf("\n%1f DESEMPILHADO!\n", valor);
                }
                break;

            case 3: // mostrar topo
                valor = retornatopo(&minhapilha);
                if (valor != 0.0) {
                    printf("\nTOPO: %1f\n", valor);
                }
                break;

            case 4: // sair
                exit(0);

            default:
                printf("\nOPÇÃO INVÁLIDA\n");
        }
    }

    return 0;
}
