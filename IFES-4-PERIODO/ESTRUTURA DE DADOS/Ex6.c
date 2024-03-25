#include <stdio.h>

int main() {
    float valores[4], aux;
    int i, j;

    // Leitura 
    for (i = 0; i < 4; i++) {
        printf("Digite o %do numero: ", i + 1);
        scanf("%f", &valores[i]);
    }

    // Ordenação "Bolha"
    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4; j++) {
            if (valores[i] > valores[j]) {
                aux = valores[j];
                valores[j] = valores[i];
                valores[i] = aux;
            }
        }
    }

    // Exibição
    printf("Valores ordenados:\n");
    for (i = 0; i < 4; i++) {
        printf("%.2f\n", valores[i]);
    }

    return 0;
}
