#include <stdio.h>

int main() {
    // Definição dos preços normais e com desconto para cada material
    float precos[3][2] = {
        {15.00, 12.50},
        {13.00, 7.50},
        {100.00, 97.00}
    };

    // Vetor para armazenar a média de preços por produto
    float media_precos[3] = {0}; // Inicializado com 0

    // Cálculo da média de preços por produto
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 2; j++) {
            media_precos[i] += precos[i][j]; // Soma dos preços normais e com desconto
        }
        media_precos[i] /= 2; // Divide a soma pelo número de preços (2)
    }

    // Apresentação dos resultados
    printf("Média de preços por produto:\n");
    for (int i = 0; i < 3; i++) {
        printf("%.2f\t", media_precos[i]);
    }
    printf("\n");

    return 0;
}
