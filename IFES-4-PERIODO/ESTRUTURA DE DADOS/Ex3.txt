#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Definição da estrutura do nó da árvore
typedef struct TreeNode {
    char isbn[14]; // ISBN (13 caracteres + '\0')
    char titulo[100]; // Título do livro
    float valor; // Valor
    char autor[50]; // Autor do livro
    char editora[50]; // Editora
    int ano_publicacao; // Ano de publicação
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

// Função para criar um novo nó da árvore
TreeNode* createNode(char isbn[], char titulo[], float valor, char autor[], char editora[], int ano_publicacao) {
    TreeNode *newNode = (TreeNode*)malloc(sizeof(TreeNode));
    if (newNode == NULL) {
        printf("Erro ao alocar memória para novo nó!\n");
        exit(1);
    }
    strcpy(newNode->isbn, isbn);
    strcpy(newNode->titulo, titulo);
    newNode->valor = valor;
    strcpy(newNode->autor, autor);
    strcpy(newNode->editora, editora);
    newNode->ano_publicacao = ano_publicacao;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Função para inserir um novo nó na árvore
TreeNode* insertNode(TreeNode *root, char isbn[], char titulo[], float valor, char autor[], char editora[], int ano_publicacao) {
    if (root == NULL) {
        return createNode(isbn, titulo, valor, autor, editora, ano_publicacao);
    }
    if (strcmp(isbn, root->isbn) < 0) {
        root->left = insertNode(root->left, isbn, titulo, valor, autor, editora, ano_publicacao);
    } else {
        root->right = insertNode(root->right, isbn, titulo, valor, autor, editora, ano_publicacao);
    }
    return root;
}

// Função para pesquisar um livro pelo ISBN na árvore
TreeNode* searchBook(TreeNode* root, char isbn[]) {
    if (root == NULL || strcmp(root->isbn, isbn) == 0) {
        return root;
    }
    if (strcmp(isbn, root->isbn) < 0) {
        return searchBook(root->left, isbn);
    } else {
        return searchBook(root->right, isbn);
    }
}

// Função para liberar a memória ocupada pela árvore
void freeTree(TreeNode* root) {
    if (root == NULL) {
        return;
    }
    freeTree(root->left);
    freeTree(root->right);
    free(root);
}

int main() {
    // Criando a árvore vazia
    TreeNode *root = NULL;
    
    // Inserindo alguns livros na árvore
    root = insertNode(root, "9783161484100", "Dom Casmurro", 25.90, "Machado de Assis", "Editora A", 1899);
    root = insertNode(root, "9788533301521", "O Príncipe", 20.50, "Nicolau Maquiavel", "Editora B", 1532);
    root = insertNode(root, "9788533624104", "1984", 30.00, "George Orwell", "Editora C", 1949);

    // Pesquisando um livro pelo ISBN
    char book_isbn[14];
    printf("Digite o ISBN do livro: ");
    scanf("%s", book_isbn);
    TreeNode *found_book = searchBook(root, book_isbn);
    
    if (found_book) {
        printf("Livro encontrado:\n");
        printf("ISBN: %s\n", found_book->isbn);
        printf("Título: %s\n", found_book->titulo);
        printf("Valor: %.2f\n", found_book->valor);
        printf("Autor: %s\n", found_book->autor);
        printf("Editora: %s\n", found_book->editora);
        printf("Ano de publicação: %d\n", found_book->ano_publicacao);
    } else {
        printf("Livro não encontrado.\n");
    }
    
    // Liberando a memória ocupada pela árvore
    freeTree(root);

    return 0;
}
