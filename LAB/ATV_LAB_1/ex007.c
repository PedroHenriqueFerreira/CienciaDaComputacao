#include <stdio.h>
#include <stdlib.h>

int isPrimo(int n) {
    for (int i = 2; n > i; i++) {
        if (!(n % i) && i != n) {
            return 0;
        }
    }

    return 1;
}

int main() {
    int n, p1 = 0, p2 = 0;

    printf("Digite um número: ");
    scanf("%d", &n);

    while (1) {
        n++;
        
        

        if (isPrimo(n)) {
            if (!p1) p1 = n;
            else if (!p2 && n - p1 == 2) {
                p2 = n;
                break;
            } else {
                p1 = 0;
                p2 = 0;
            }
        }
    }

    printf("p1: %d\n", p1);
    printf("p2: %d\n", p2);

    return 0;
}   