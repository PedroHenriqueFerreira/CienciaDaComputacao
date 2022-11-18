#include <stdio.h>
#include <stdlib.h>
#include "heap.h"

HEAP* HEAP_create(int n, COMP* compara) {
	HEAP* heap = malloc(sizeof(HEAP));
	heap->elems = malloc(n * sizeof(void*));
	heap->N = n;
	heap->P = 0;
	heap->comparador = compara;

	return heap;
}

void HEAP_add(HEAP* heap, void* newelem) {
  if (heap->P < heap->N) {
    heap->elems[heap->P] = newelem;
	int pos = heap->P;

	while (heap->comparador(heap->elems[pos], heap->elems[(pos - 1) / 2]) > 0) {
		void* aux = heap->elems[pos];
		heap->elems[pos] = heap->elems[(pos - 1) / 2];
		heap->elems[(pos - 1) / 2] = aux;	
		pos = (pos - 1) / 2;
	}	

	heap->P++;
  }
}

void* HEAP_remove(HEAP* heap) {
	void* min = heap->elems[0];

	heap->elems[0] = heap->elems[heap->P - 1];
	heap->elems[heap->P - 1] = min;
	
	heap->P--;

	int pai = 0;
	int filho = pai * 2 + 1;
	
	while (filho < heap->P) {
		if (filho + 1 < heap->P) {
			if (heap->comparador(heap->elems[filho], heap->elems[filho + 1]) < 0) {
				filho += 1;
			}
		}

		if (heap->comparador(heap->elems[pai], heap->elems[filho]) < 0) {
			void* aux = heap->elems[pai];
			heap->elems[pai] = heap->elems[filho];
			heap->elems[filho] = aux;

			pai = filho;
			filho = pai * 2 + 1;
		} else {
			filho = heap->P + 1;
		}
	}

	return min;
}

//Função de comparação
int myCOMP(void* x, void* y){
	int ptx = *((int*)x);
	int pty = *((int*)y);
	if(ptx < pty){
		return -1;
	}else{
		if(ptx > pty) return 1;
		else return 0;
	}
}

//Print para a estrutura
void print(void** vet, int P){
	int i;
	printf("VETOR DE %d TAMANHO:\n", P);
	for(i = 0; i < 10; i++){
		printf(" %d ", *((int*)vet[i]));
	}
	printf("\n");
}

int main(){
   	HEAP* vet = HEAP_create(10, myCOMP);
   	
   	int* x;
   	int i;
   	
   	printf("INCLUINDO... \n");
	for(i = 0; i < 10; i++){
		x = malloc(sizeof(int));
		*x = i*10;
		HEAP_add(vet, x);
	}
	
	print(vet->elems, vet->P);
  
  	printf("REMOVENDO!");
  	HEAP_remove(vet);	
	HEAP_remove(vet);	
	HEAP_remove(vet);	
	HEAP_remove(vet);	
	HEAP_remove(vet);	
	HEAP_remove(vet);	
	HEAP_remove(vet);	
	HEAP_remove(vet);	
	HEAP_remove(vet);	
	HEAP_remove(vet);	
  	
	print(vet->elems, vet->P);
   
	return 0;  
}
