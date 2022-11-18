#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    char *heroi;
    int num_filmes, dias_descanso;
    struct No *prox;
} NO;

int tam = 0;
NO *inicio = NULL, *fim = NULL;

void adicionar(char *heroi, int num_filmes) {
    NO *novo = malloc(sizeof(NO));
    novo->heroi = heroi;
    novo->num_filmes = num_filmes;
    novo->dias_descanso = 5 * num_filmes;
    novo->prox = NULL;

    if (inicio == NULL) {
        inicio = novo;
        fim = novo;
    } else if (inicio->num_filmes < num_filmes) {
        novo->prox = inicio;
        inicio = novo;
    } else {
        if (fim->num_filmes > num_filmes) {
            fim->prox = novo;
            fim = novo;
        } else {
            NO *auxiliar = inicio;

            while(auxiliar->prox != NULL && num_filmes < auxiliar->prox->num_filmes) {
                auxiliar = auxiliar->prox;
            }

            novo->prox = auxiliar->prox;
            auxiliar->prox = novo;
        }
    }

    tam++;
}

char* remover() {
    if (tam == 0) return NULL;

    char *heroi_removido;

    NO *lixo = inicio;

    heroi_removido = inicio->heroi;
    inicio = inicio->prox;

    free(lixo);

    return heroi_removido;
}

void imprimir() {
    NO *auxiliar = inicio;

    while (auxiliar != NULL) {
        printf("Heroi: %s - Dias: %d\n", auxiliar->heroi, auxiliar->dias_descanso);

        auxiliar = auxiliar->prox;
    }

    printf("FIM!\n");
}

int main() {
    adicionar("Doutor Estranho", 6);
    adicionar("Homem Formiga", 4);
    adicionar("Wanda", 5);
    adicionar("Homem Aranha", 11);
    imprimir();
    printf("Primeiro herói a tirar férias: %s\n", remover());

    imprimir();

    return 0;
}