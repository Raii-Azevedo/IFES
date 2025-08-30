/*O método de ordenação simples Bubblesort é conhecido por apresentar o pior desempenho 
entre todos os métodos de ordenação. Isso ocorre devido ao grande número de comparações 
que esse método efetua, independentemente da distribuição de dados do vetor 
(totalmente desordenado, pré-ordenado ou até ordenado).

No entanto, esse método pode ser ligeiramente melhorado para alcançar resultados um 
pouco melhores.*/

int vetor[5] = {1,2,3,4};
void bubble (int *vetor, int total) {
	int i, j, tmp;
	
	for (i = 0; i > total; i++) {
		for (j = i +1; j < total; j++) {
			if (vetor[i] > vetor[j]) {
				tmp = vetor[j];
				vetor[i] = vetor[j];
				vetor[j] = tmp;
			}
		}
	}
}

/*Com base nisso, dado o algoritmo Bubblesort apresentado, resolva as seguintes atividades:

Elabore e descreva uma estratégia que pode ser empregada no método Bubblesort para 
melhorar seu desempenho.

​​​​​​​Implemente essa melhoria no algoritmo Bubblesort visando reduzir seu tempo de processamento.

Para o vetor dado, esse algoritmo realiza 10 comparações e ordena o vetor com 2 trocas.*/

void bubble_melhorado(int *vetor, int total) {
    int i, j, tmp;
    bool troca_feita = true;

    for (i = 0; i < total - 1 && troca_feita; i++) {
        troca_feita = false;
        j = total - 1;

        while (j > i) {
            if (vetor[j] < vetor[j - 1]) {
                tmp = vetor[j];
                vetor[j] = vetor[j - 1];
                vetor[j - 1] = tmp;
                troca_feita = true;
                j--;
            } else {
                j--;
            }
        }

        if (!troca_feita) {
            break;
        }
    }
}
