#include "ordvetor.h"

int comparar(void* x, void* y) {
	int xx = *((int*) x);
	int yy = *((int*) y);

	return xx < yy ? 1 : xx == yy ? 0 : -1;
}

int main() {
	const int VETOR_SIZE = 10;
	const int VETOR_REMOVE = 2;

	VETORORD* vetor = VETORD_create(VETOR_SIZE, comparar);

	int meuVetor[VETOR_SIZE];

	printf("VETOR INICIALIZADO: ");
	for (int i = 0; i < VETOR_SIZE; i++) {
		meuVetor[i] = rand() % VETOR_SIZE;
		printf("%d - ", meuVetor[i]);
	}
	printf("FIM\n\n");

	for (int i = 0; i < VETOR_SIZE; i++) {
		VETORD_add(vetor, &meuVetor[i]);
	}

	printf("ITENS REMOVIDOS: ");
	for (int i = 0; i < VETOR_REMOVE; i++) {
		printf("%d - ", *((int*) VETORD_remove(vetor)));
	}
	printf("FIM\n\n");

	printf("VETOR FINAL: ");
	for (int i = 0; i < vetor->P; i++) {
		printf("%d - ", *((int*) vetor->elems[i]));
	}
	printf("FIM\n");

	return 0;
}
