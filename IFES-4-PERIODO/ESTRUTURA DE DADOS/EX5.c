#include <stdio.h>
#include <stdlib.h>

// Estrutura de um nó da árvore AVL
struct Node {
    int data;
    int balance_factor; // Fator de balanceamento do nó
    struct Node *left;
    struct Node *right;
};

// Função para criar um novo nó
struct Node* newNode(int data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->balance_factor = 0; // Inicialmente, o fator de balanceamento é zero
    node->left = NULL;
    node->right = NULL;
    return node;
}

// Função para calcular a altura de uma árvore
int height(struct Node* node) {
    if (node == NULL)
        return 0;
    else {
        // Calcula a altura da subárvore esquerda e direita
        int left_height = height(node->left);
        int right_height = height(node->right);
        // Retorna a maior altura adicionada de 1 (para contar o próprio nó)
        return (left_height > right_height ? left_height : right_height) + 1;
    }
}

// Função para calcular o fator de balanceamento de um nó
int balanceFactor(struct Node* node) {
    if (node == NULL)
        return 0;
    // Calcula o fator de balanceamento como a diferença entre as alturas das subárvores
    return height(node->right) - height(node->left);
}

// Função de rotação para a esquerda
struct Node* rotateLeft(struct Node* node) {
    struct Node* new_root = node->right;
    node->right = new_root->left;
    new_root->left = node;
    // Recalcula o fator de balanceamento dos nós afetados
    node->balance_factor = balanceFactor(node);
    new_root->balance_factor = balanceFactor(new_root);
    return new_root;
}

// Função de rotação para a direita
struct Node* rotateRight(struct Node* node) {
    struct Node* new_root = node->left;
    node->left = new_root->right;
    new_root->right = node;
    // Recalcula o fator de balanceamento dos nós afetados
    node->balance_factor = balanceFactor(node);
    new_root->balance_factor = balanceFactor(new_root);
    return new_root;
}

// Função para inserir um novo nó na árvore AVL
struct Node* insert(struct Node* root, int data) {
    if (root == NULL)
        return newNode(data);

    // Inserção normal de um novo nó
    if (data < root->data)
        root->left = insert(root->left, data);
    else if (data > root->data)
        root->right = insert(root->right, data);
    else // Ignora valores duplicados
        return root;

    // Atualiza o fator de balanceamento do nó atual
    root->balance_factor = balanceFactor(root);

    // Verifica se é necessário realizar rotações para balancear a árvore
    if (root->balance_factor > 1) {
        if (data > root->right->data)
            root = rotateLeft(root);
        else {
            root->right = rotateRight(root->right);
            root = rotateLeft(root);
        }
    }
    else if (root->balance_factor < -1) {
        if (data < root->left->data)
            root = rotateRight(root);
        else {
            root->left = rotateLeft(root->left);
            root = rotateRight(root);
        }
    }
    return root;
}

// Função para percorrer a árvore em ordem
void inorderTraversal(struct Node* root) {
    if (root != NULL) {
        inorderTraversal(root->left);
        printf("%d (BF: %d)\n", root->data, root->balance_factor);
        inorderTraversal(root->right);
    }
}

// Função para liberar a memória alocada para a árvore
void freeTree(struct Node* root) {
    if (root != NULL) {
        freeTree(root->left);
        freeTree(root->right);
        free(root);
    }
}

// Função principal
int main() {
    // Construção da árvore desbalanceada
    struct Node* root = newNode(13);
    root->left = newNode(10);
    root->right = newNode(15);
    root->left->left = newNode(5);
    root->left->right = newNode(11);
    root->left->left->left = newNode(4);
    root->left->left->right = newNode(6);
    root->right->right = newNode(16);

    printf("Árvore original (antes do balanceamento):\n");
    inorderTraversal(root);

    // Inserção de índices de balanceamento e balanceamento da árvore
    root = insert(root, 20);
    root = insert(root, 17);
    root = insert(root, 14);

    printf("\nÁrvore balanceada:\n");
    inorderTraversal(root);

    // Libera a memória alocada para a árvore
    freeTree(root);

    return 0;
}
