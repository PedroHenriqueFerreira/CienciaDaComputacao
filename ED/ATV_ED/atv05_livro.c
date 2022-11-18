#include <stdio.h>
#include <stdlib.h>

typedef struct ImoveisDaRua {
    int numero;
    char *complemento;
    char imovelComercial;
    struct ImoveisDaRua *prox;
} IDR;

int main() {
    IDR *casa342 = malloc(sizeof(IDR));
    IDR *apartamento17 = malloc(sizeof(IDR));
    IDR *mercantil1 = malloc(sizeof(IDR));

    casa342->numero = 342;
    casa342->complemento = "Casa, 284 m²";
    casa342->imovelComercial = 'N';

    apartamento17->numero = 17;
    apartamento17->complemento = "Predio, 4 andares, 182 m²";
    apartamento17->imovelComercial = 'N';

    mercantil1->numero = 1;
    mercantil1->complemento = "Casa Comercial, 521 m²";
    mercantil1->imovelComercial = 'S';

    casa342->prox = apartamento17;
    apartamento17->prox = mercantil1;
    mercantil1->prox = NULL;

    IDR *gancho = casa342;

    while (gancho != NULL) {
        printf("Número: %d\nComplemento: %s\nImovel Comercial: %c\n\n", gancho->numero, gancho->complemento, gancho->imovelComercial);

        gancho = gancho->prox;
    }

    return 0;
}