#include <stdio.h>
#include <stdlib.h>

int main() {
    int num;
    int binNum[5];

    printf("Digite um valor decimal: ");
    scanf("%d", &num);

    if (num < 0 || num > 31) {
        printf("Valor inválido!\n");
    } else {
        for (int i = 4; i >= 0; i--) {
            binNum[i] = num % 2;
            num /= 2;
        }

        printf("Este valor em binário é: ");

        for (int i = 0; i <= 4; i++) {
            printf("%d", binNum[i]);
        }

        printf("\n");
    }

    return 0;
}