#include <stdio.h>
#include <stdlib.h>

typedef struct no{
    int valor;
    struct no *prox;
}NO;

NO *inicio = NULL;
NO *fim = NULL;
int tam = 0;

void adicionar(int valor){
    
        NO *novo = (NO*) malloc (sizeof (NO));
        novo->valor = valor;
        novo->prox = NULL;
    
        if(inicio == NULL){ //fila vazia :D
            inicio = novo;
            fim = novo;
        }else{ //fim - CONSTANTE <3
            fim->prox = novo;
            fim = novo;
        }
        tam++;
    
}

int remover(){
    
    int valor_removido = -1;
    if(inicio != NULL){//fila tem elementos! :D
    
        NO* lixo = inicio;
        if(tam == 1){// fila com unico elemento - inicio e fim = NULL
            inicio = NULL;
            fim= NULL;
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


