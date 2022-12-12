#include <stdio.h>
#include <stdlib.h>

#ifndef TR67_535770_H
#define TR67_535770_H

typedef struct set {
	int size, max;
	float density;
	int* elems;
} Set;

int bit1Count(unsigned int n);
int highestBit(unsigned int n);

Set* emptySet();
Set* readSet(FILE *file);

void unionSet(Set *C, Set *A, Set *B);
void intersecSet(Set *C, Set *A, Set *B);

void writeSet(FILE *file, Set *A);

void printSet(Set *A);

#endif