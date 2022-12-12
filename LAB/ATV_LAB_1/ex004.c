#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    int result = 0;

    printf("Digite um número: ");
    scanf("%d", &n);

    for (int i = 2; i <= 7; i++) {
        if (n % i == 0) result += i;
    }

    printf("Soma dos divisores entre 2 e 7: %d\n", result);

    return 0;
}