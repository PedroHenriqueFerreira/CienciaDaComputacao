#include <stdio.h>
#include <stdlib.h>

typedef struct no{
    int valor;
    struct no *prox;
}NO;

NO *inicio = NULL;
int tam = 0;

void adicionar(int valor){
    
        NO *novo = (NO*) malloc (sizeof (NO));
        novo->valor = valor;
        novo->prox = NULL;
    
        if(inicio == NULL){ //pilha vazia :D
            inicio = novo;
        }else { //inicio - CONSTANTE <3
            novo->prox = inicio;
            inicio = novo;
        }
        tam++;
    
}



int remover(){
    
    int valor_removido = -1;
    if(inicio != NULL){//pilha não está vazia! :D
        NO* lixo = inicio;
        if(tam == 1){//1 elemento - CONSTANTE
            inicio = NULL;
        }else{ //inicio - CONSTANTE
            inicio = inicio->prox;
        }
        valor_removido = lixo->valor;
        free(lixo);
        tam--;
    }
    return valor_removido;
}


int main(){
    adicionar(817236);
    adicionar(172833);
    adicionar(192743);
    adicionar(934832);
    adicionar(918374);
    int cod_produto_removido = remover();
    
    if(cod_produto_removido == -1){
        printf("Fila de estoque vazia!\n");
    }else{
        printf("Código do produto removido: %d\n", cod_produto_removido);
    }
    return 0;
}


