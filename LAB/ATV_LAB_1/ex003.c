#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;

    printf("Digite um número: ");
    scanf("%d", &n);

    printf("Menor inteiro maior que %d: %d\n", n, n + 1);    

    return 0;
}