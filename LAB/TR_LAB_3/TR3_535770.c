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

    for (y = 0; y <= 199; y++) {
        x[y] = 0;
    }    

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