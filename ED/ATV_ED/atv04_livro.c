#include <stdio.h>
#include <stdlib.h>

void troca(int *n1, int *n2) {
    int temp = *n1;
    *n1 = *n2;
    *n2 = temp;
}

int main() {
    int n1 = 4;
    int n2 = 5;

    troca(&n1, &n2);

    printf("N1: %d\nN2: %d\n", n1, n2);

    return 0;
}