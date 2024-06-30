#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Definição da estrutura para os elementos da lista
typedef struct Elemento {
    char nome[50];
    int idade;
    char endereco[100];
    struct Elemento *prox; // Ponteiro para o próximo elemento da lista
} Elemento;

// Definição da estrutura para a lista dinâmica
typedef struct {
    Elemento *inicio; // Ponteiro para o primeiro elemento da lista
    Elemento *fim;    // Ponteiro para o último elemento da lista
} ListaDinamica;

// Função para inicializar a lista
void inicializarLista(ListaDinamica *lista) {
    lista->inicio = NULL;
    lista->fim = NULL;
}

// Função para inserir elemento no início da lista
void inserirInicio(ListaDinamica *lista, const char *nome, int idade, const char *endereco) {
    Elemento *novoElemento = (Elemento *)malloc(sizeof(Elemento));
    if (novoElemento == NULL) {
        printf("Erro ao alocar memoria para novo elemento.\n");
        return;
    }
    strcpy(novoElemento->nome, nome);
    novoElemento->idade = idade;
    strcpy(novoElemento->endereco, endereco);
    novoElemento->prox = lista->inicio;
    lista->inicio = novoElemento;
    if (lista->fim == NULL) { // Lista vazia
        lista->fim = novoElemento;
    }
}

// Função para inserir elemento no final da lista
void inserirFinal(ListaDinamica *lista, const char *nome, int idade, const char *endereco) {
    Elemento *novoElemento = (Elemento *)malloc(sizeof(Elemento));
    if (novoElemento == NULL) {
        printf("Erro ao alocar memoria para novo elemento.\n");
        return;
    }
    strcpy(novoElemento->nome, nome);
    novoElemento->idade = idade;
    strcpy(novoElemento->endereco, endereco);
    novoElemento->prox = NULL;
    if (lista->fim != NULL) { // Lista não está vazia
        lista->fim->prox = novoElemento;
    }
    lista->fim = novoElemento;
    if (lista->inicio == NULL) { // Lista vazia
        lista->inicio = novoElemento;
    }
}

// Função para excluir elemento do início da lista
void excluirInicio(ListaDinamica *lista) {
    if (lista->inicio == NULL) { // Lista vazia
        printf("Lista vazia. Nao ha elementos para excluir.\n");
        return;
    }
    Elemento *elementoRemovido = lista->inicio;
    lista->inicio = lista->inicio->prox;
    free(elementoRemovido);
    if (lista->inicio == NULL) { // Lista ficou vazia
        lista->fim = NULL;
    }
}

// Função para excluir elemento do final da lista
void excluirFinal(ListaDinamica *lista) {
    if (lista->inicio == NULL) { // Lista vazia
        printf("Lista vazia. Nao ha elementos para excluir.\n");
        return;
    }
    if (lista->inicio->prox == NULL) { // Lista com apenas um elemento
        free(lista->inicio);
        lista->inicio = NULL;
        lista->fim = NULL;
        return;
    }
    Elemento *elementoAnterior = NULL;
    Elemento *elementoAtual = lista->inicio;
    while (elementoAtual->prox != NULL) {
        elementoAnterior = elementoAtual;
        elementoAtual = elementoAtual->prox;
    }
    elementoAnterior->prox = NULL;
    lista->fim = elementoAnterior;
    free(elementoAtual);
}

// Função para imprimir a lista
void imprimirLista(ListaDinamica *lista) {
    Elemento *elementoAtual = lista->inicio;
    printf("Lista:\n");
    while (elementoAtual != NULL) {
        printf("Nome: %s\tIdade: %d\tEndereco: %s\n", elementoAtual->nome, elementoAtual->idade, elementoAtual->endereco);
        elementoAtual = elementoAtual->prox;
    }
}

// Função para excluir toda a lista
void excluirLista(ListaDinamica *lista) {
    Elemento *elementoAtual = lista->inicio;
    while (elementoAtual != NULL) {
        Elemento *elementoRemovido = elementoAtual;
        elementoAtual = elementoAtual->prox;
        free(elementoRemovido);
    }
    lista->inicio = NULL;
    lista->fim = NULL;
}

int main() {
    ListaDinamica lista;
    inicializarLista(&lista);

    inserirInicio(&lista, "Alice", 25, "Rua A");
    inserirInicio(&lista, "Bob", 30, "Rua B");
    inserirFinal(&lista, "Carol", 28, "Rua C");
    inserirFinal(&lista, "João", 23, "Rua C");

    printf("Lista inicial:\n");
    imprimirLista(&lista);

    excluirInicio(&lista);
    excluirFinal(&lista);

    printf("\nLista apos excluir inicio e final:\n");
    imprimirLista(&lista);

    excluirLista(&lista);

    printf("\nLista apos excluir tudo:\n");
    imprimirLista(&lista);

    return 0;
}
