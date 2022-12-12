#include <stdio.h>
#include <stdlib.h>

//MODELO DE EXEMPLO

int main(){
   
   	//Variáveis que podem ser usadas
   	unsigned int x[200];
   	int y;
   	int z;
   	int k;
   	int w;
   	int j;
   	int i;
   	
   	//#########################

    // Zerando os valores do vetor
    for (y = 0; y <= 199; y++) {
        x[y] = 0;
    }    

    // Lendo os números e marcando no vetor bit a bit
    while (1) {
        printf("Digite um número: ");
        scanf("%d", &z);

        if (z == -1) break;
        if (z < 0 || z > 5000) {
            printf("Número inválido!\n");
            continue;
        }

        x[z / 32] |= (1 << (z % 32));
    }

    // Mostrando os números marcados bit a bit no vetor
    printf("Números digitados: ");

    for (k = 0; k <= 5000; k++) {
        if (x[k / 32] & (1 << (k % 32))) {
            printf("%d ", k);
        }
    }

    printf("\n");
   	
   	//#########################
   
	return 0;  
}