#include <stdio.h>
#include <stdlib.h>

int main() {
    float x, y;

    printf("Digite um número: ");
    scanf("%f", &x);

    printf("Digite outro número: ");
    scanf("%f", &y);

    if (y == 0) {
        printf("Divisão por zero inválida\n");
    } else {
        printf("%.2f / %.2f = %.2f\n", x, y, x / y);
    }

    return 0;
}