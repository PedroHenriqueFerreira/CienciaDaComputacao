#include "TR67_535770.h"

int bit1Count(unsigned int n)
{
	unsigned int count;
	count = n - ((n >> 1) & 033333333333) - ((n >> 2) & 011111111111);
	return ((count + (count >> 3)) & 030707070707) % 63;
}

int highestBit(unsigned int n) {
	unsigned int count = 0;
	while(n >> 1) {
		n = n >> 1;
		count++;
	}	

	return count;
}

Set* emptySet() {
	Set* new = malloc(sizeof(Set));
	new->size = 0;
	new->max = 0;
	new->density = 0.0;
	new->elems = NULL;

	return new;
}

Set* readSet(FILE* file) {
	Set* new = emptySet();
	
	if (file == NULL) return new;

	int i, size, max, elem;
	float density;

	fscanf(file, "%d %d %f", &size, &max, &density);

	new->size = size;
	new->max = max;
	new->density = density;

	new->elems = calloc(((max >> 5) + 1), sizeof(int));

	for (i = 0; i <= size; i++) {
		fscanf(file, "%d", &elem);
		new->elems[elem >> 5] |= (1 << (elem & 31));
	}	

	return new;
}

void unionSet(Set *C, Set *A, Set *B) {
	Set* larger = A->max > B->max ? A : B;
	Set* smaller = A->max > B->max ? B : A;

	C->max = larger->max;
	C->elems = calloc((C->max >> 5) + 1, sizeof(int));
	
	for (int i = 0; i <= (larger->max >> 5); i++) {
		C->elems[i] = larger->elems[i];
		if (i <= (smaller->max >> 5)) {
			C->elems[i] |= smaller->elems[i];
		}

		C->size += bit1Count(C->elems[i]);
	}	
	
	if (C->max) C->density = (float) C->size / C->max;
}

void intersecSet(Set *D,Set *A, Set *B) {
	Set* larger = A->max > B->max ? A : B;
	Set* smaller = A->max > B->max ? B : A;

	D->elems = calloc((smaller->max >> 5) + 1, sizeof(int));

	for (int i = (smaller->max >> 5); i >= 0; i--) {
		D->elems[i] = smaller->elems[i] & larger->elems[i];
		D->size += bit1Count(D->elems[i]);

		if (D->max == 0 && D->elems[i] != 0) {
		 	D->max = (i << 5) + highestBit(D->elems[i]);
		}
	}	

	if (D->max) D->density = (float) D->size / D->max;
}

void writeSet(FILE* file, Set* A) {
	fprintf(file, "%d\n%d\n%f\n", A->size, A->max, A->density);
	
	for(int i = 0; i <= A->max; i++) {
		if (A->elems[i >> 5] & (1 << (i & 31))) {
			fprintf(file, "%d\n", i);
		}
	}
}

void printSet(Set *A) {
	printf("TOTAL DE ELEMENTOS: %d\n", A->size);
	printf("MAIOR ELEMENTO: %d\n", A->max);
	printf("DENSIDADE: %f\n", A->density);

	printf("ELEMENTOS: ");
	for (int i = 0; i <= A->max; i++) {
		if(A->elems[i >> 5] & (1 << (i & 31))) {
			printf("%d ", i);
		}
	}

	printf("\n");
}