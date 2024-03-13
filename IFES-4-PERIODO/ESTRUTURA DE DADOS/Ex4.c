#include <stdio.h>
#include <stdlib.h>

// Definição da estrutura do nó da árvore
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// Função para criar um novo nó
struct Node* newNode(int data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

// Função para imprimir a ordem de nível transversal
void printLevelOrder(struct Node* root) {
    if (root == NULL)
        return;

    // Usamos uma fila (queue) para percorrer a árvore em ordem de nível
    struct Node* queue[1000];
    int front = 0, rear = 0;

    // Adicionamos a raiz à fila
    queue[rear++] = root;

    while (front < rear) {
        // Obtemos o nó atual da fila
        struct Node* current = queue[front++];
        // Imprimimos o valor do nó
        printf("%d ", current->data);

        // Adicionamos os filhos à fila, se existirem
        if (current->left != NULL)
            queue[rear++] = current->left;
        if (current->right != NULL)
            queue[rear++] = current->right;
    }
}

// Exemplo de uso
int main() {
    // Construção da árvore da empresa
    struct Node* root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    root->right->left = newNode(6);
    root->right->right = newNode(7);

    printf("Ordem de nível da matriz da empresa:\n");
    printLevelOrder(root);

    return 0;
}
