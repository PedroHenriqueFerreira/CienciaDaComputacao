#include <stdio.h>
#include <stdlib.h>

//MODELO DE EXEMPLO

int main(){
   
   	//Variáveis que podem ser usadas
   	int x;
   	int y;
   	int z;
   	int k;
   	int w;
   	int j;
   	int i;
   	
   	//#########################
   	
    y = 0;

    while (1) {
        printf("Digite um número: ");
        scanf("%d", &x);

        if (x == -1) break;
        if (x < 0 || x > 31) {
            printf("Número inválido!\n");
            continue;
        }

        y = y | (1 << x);
    }

    printf("Números digitados: ");

    for (z = 0; z <= 31; z++) {
        if (y & (1 << z)) {
            printf("%d ", z);
        }
    }

    printf("\n");

   	//#########################
   
	return 0;  
}