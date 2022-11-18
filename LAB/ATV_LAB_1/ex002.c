#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    float total = 0;

    printf("Digite um número: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        total += 1.0 / i;
    }
    printf("%f\n", total);
    return 0;
}