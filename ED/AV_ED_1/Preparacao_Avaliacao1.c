#include "No.h"

NO *inicio;
int tam = 0;

void add (int id, int sexo, int num_filhotes){
    NO *novo = malloc (sizeof(NO));
    novo->id = id;
    novo->sexo = sexo;
    novo->num_filhotes = num_filhotes;
    if(tam == 0){
        novo->prox = novo;
        novo->ant = novo;
        inicio = novo;
    }else{
        novo->prox = inicio;
        novo->ant = inicio->ant;
        inicio->ant->prox = novo;
        inicio->ant = novo;
    }
    tam++;
}


void remover(int id){
    NO *aux = inicio;
    for(int i=0; i<tam; i++){
        if(aux->id == id){
            break;
        }else{
            aux = aux->prox;
        }
    }
    if(aux->id == id){
        aux->ant->prox = aux->prox;
        aux->prox->ant = aux->ant;
        if(aux == inicio){
            inicio = aux->prox;
        }
        free(aux);
        tam--;
    }else{
        printf("Canguru não encontrado! \n");
    }
}

int soma (NO *aux){
    if (tam == 0 || aux->prox == inicio) return 0;

    return aux->num_filhotes + soma(aux->prox);
}

void imprimir(){
    NO *aux = inicio;
    for(int i=0; i<tam; i++){
        printf("Caguru: %d \n", aux->id);
        aux = aux->prox;
    }
}

int main(){
    add(1,1,2);
    add(2,1,1);
    add(3,0,0);
    add(4,1,2);
    add(5,0,0);
    imprimir();
    printf("Filhotes gerados: %d\n", soma(inicio));
    return 0;
}
