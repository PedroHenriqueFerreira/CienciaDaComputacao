#include <stdio.h>
#include <stdlib.h>

/* Considere que o codigo a seguir utilizado para gerenciar as notas finais da turma de ED 2022.2! Esta disciplina e composta de duas notas. Portanto, a nota final eh a media das duas notas: NF = (nota1+nota2)/2.*/


typedef struct no{
    char * nome_aluno;
    float nota1;
    float nota2;
    struct no *prox;
    struct no *ant;
}NO;

NO *inicio = NULL;
NO *fim = NULL;
int tam = 0;

void adicionar(char *nome_aluno, float nota1, float nota2, int pos){
    
        NO *novo = (NO*) malloc (sizeof (NO));
        novo->nome_aluno = nome_aluno;
        novo->nota1 = nota1;
        novo->nota2 = nota2;
        novo->prox = NULL;
        novo->ant = NULL;
    
        if(inicio == NULL){ //lista vazia :D
            inicio = novo;
            fim = novo;
        }else if(pos == 0){ //inicio - CONSTANTE <3
            novo->prox = inicio;
            inicio->ant = novo;
            inicio = novo;
        }else if(pos == tam){ //fim - CONSTANTE <3
            fim->prox = novo;
            novo->ant = fim;
            fim = novo;
        }else{ // "no meio" - busca :/ - LINEAR
            NO *aux = inicio;
            for(int i=0; i<pos; i++){
                aux = aux->prox;
            }
            novo->prox = aux;
            novo->ant = aux->ant;
            aux->ant = novo;
            novo->ant->prox = novo;
        }
        tam++;
}


void imprimir(){
    NO *aux = inicio;
    for(int i=0; i<tam; i++){
        printf("%s \n", aux->nome_aluno);
        aux = aux->prox;
    }
}

/* --------------- EXERCICIOS ----------*/

/*1 - crie uma função 100% recursiva para imprimir todos os alunos e sua media final*/
void imprimirRecursivo(NO *aux) {
    if (aux != NULL) {
        printf("ALUNO: %s | MÉDIA: %f\n", aux->nome_aluno, (aux->nota1 + aux->nota2) / 2);
        imprimirRecursivo(aux->prox);
    }
}

/*2 - crie uma função 100% recursiva que retorne a media final da turma*/
float mediaTurmaRecursiva(NO *aux) {
    if (aux == NULL) return 0;
    float media = (aux->nota1 + aux->nota2) / 2;

    if (aux == inicio) return (media + mediaTurmaRecursiva(aux->prox)) / tam;
    return media + mediaTurmaRecursiva(aux->prox);
}

/*3 - crie uma função 100% recursiva que imprima a situacao de cada aluno: aprovado, reprovado, final*/
void situacaoRecursiva(NO *aux) {
    if (aux != NULL) {
        float media = (aux->nota1 + aux->nota2) / 2;
        printf("NOME: %s | SITUAÇÃO: %s\n", aux->nome_aluno, media > 7 ? "APROVADO" : media > 4 ? "FINAL" : "REPROVADO");
        situacaoRecursiva(aux->prox);
    }
}


int main(){
    adicionar("Joao", 5.0, 3.0, 0);
    adicionar("Pedro", 4.0, 6.0, 1);
    adicionar("Laura", 7.5, 8.0, 1);
    adicionar("Marcos", 3.5, 5.0, 2);
    adicionar("Tatiane", 10.0, 10.0, 0);
    adicionar("Andre", 6.25, 8.0, 2);
    adicionar("Enzo", 8.75, 6.0, 2);
    adicionar("Luiza", 7.5, 4.0, 3);
    adicionar("Eduardo", 2.5, 3.0, 1);
    adicionar("Fernanda", 8.5, 4.0, 0);
    imprimir();
    /*Para testar suas funcoes faca suas chamadas aqui! :D
     Bons estudos!!! :D */

    printf("------------ Questão 1 ------------\n");
    imprimirRecursivo(inicio);
    printf("------------ Questão 2 ------------\n");
    printf("MEDIA DA TURMA: %f\n", mediaTurmaRecursiva(inicio));
    printf("------------ Questão 3 ------------\n");
    situacaoRecursiva(inicio);
    return 0;
}



