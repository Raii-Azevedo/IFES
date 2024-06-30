#include <stdio.h>
#include <stdbool.h> // Para usar o tipo de dado booleano

// Definindo estrutura para o livro
struct Livro {
    int codigo;
    char titulo[100];
};

// Declaração de funções
void inserirLivro();
void removerLivro();
void exibirLivros();

// Variáveis globais
struct Livro livro[30];
int tampilha = 0;

int main() {
    int opcao;
    do {
        printf("\nMenu:\n");
        printf("1. Inserir livro\n");
        printf("2. Remover livro\n");
        printf("3. Exibir livros\n");
        printf("4. Sair\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                inserirLivro();
                break;
            case 2:
                removerLivro();
                break;
            case 3:
                exibirLivros();
                break;
            case 4:
                printf("Saindo...\n");
                break;
            default:
                printf("Opção inválida!\n");
        }
    } while (opcao != 4);

    return 0;
}

// Função para inserir um livro na pilha
void inserirLivro() {
    if (tampilha < 30) {
        // Solicita os dados do livro ao usuário
        printf("\nColocar livro no topo da pilha\n");
        printf("Codigo do livro: ");
        scanf("%d", &livro[tampilha].codigo);
        printf("Titulo do Livro: ");
        fflush(stdin);
        gets(livro[tampilha].titulo);
        
        // Incrementa o topo da pilha
        tampilha++;

        printf("\nLivro inserido com sucesso!\n");
    } else {
        printf("\nPilha cheia, livro não foi inserido!\n");
    }
}

// Função para remover um livro da pilha com base no código
void removerLivro() {
    int codigo;
    bool encontrado = false;

    // Solicita o código do livro a ser removido
    printf("\nDigite o código do livro a ser removido: ");
    scanf("%d", &codigo);

    // Procura pelo livro com o código informado e o remove da pilha
    for (int i = tampilha - 1; i >= 0; i--) {
        if (livro[i].codigo == codigo) {
            encontrado = true;
            // Move todos os livros acima do livro removido uma posição para baixo
            for (int j = i; j < tampilha - 1; j++) {
                livro[j] = livro[j + 1];
            }
            tampilha--;
            printf("\nLivro removido com sucesso!\n");
            break;
        }
    }

    // Se o livro não for encontrado, exibe uma mensagem
    if (!encontrado) {
        printf("\nLivro não encontrado!\n");
    }
}

// Função para exibir todos os livros da pilha
void exibirLivros() {
    if (tampilha == 0) {
        printf("\nPilha vazia, nenhum livro para exibir!\n");
    } else {
        printf("\nLista de livros:\n");
        for (int i = 0; i < tampilha; i++) {
            printf("Código: %d, Título: %s\n", livro[i].codigo, livro[i].titulo);
        }
    }
}
