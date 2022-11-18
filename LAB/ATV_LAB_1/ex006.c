#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, result;

    // 2 3 4 5 6 7
    printf("Digite um número: ");
    scanf("%d", &n);

    result = !(n % 2) * 2 + !(n % 3) * 3 + !(n % 4) * 4 + !(n % 5) * 5 + !(n % 6) * 6 + !(n % 7) * 7;

    printf("Soma dos divisores entre 2 e 7: %d\n", result);

    return 0;
}   