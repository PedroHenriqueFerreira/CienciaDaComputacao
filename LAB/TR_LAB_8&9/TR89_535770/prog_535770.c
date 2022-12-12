#include <stdlib.h>
#include <stdio.h>

#define TRUE 1
#define FALSE 0

int main (int argc, char** argv) {
    int friends, friendships, friend1, friend2;
    int i, line, item;

    FILE *readFile = fopen(argv[1], "r");
    FILE *writeFile = fopen(argv[2], "w");

    fscanf(readFile, "%d %*d %d", &friends, &friendships);

    friends++;

    char matriz[friends][friends];

    for (line = 0; line < friends; line++) {
        for (item = 0; item < friends; item++) {
            matriz[line][item] = line == item ? 1 : 0;
        }
    }

    for (i = 0; i < friendships; i++) {
        fscanf(readFile, "%d %d", &friend1, &friend2);
        matriz[friend1][friend2] = 1;
        matriz[friend2][friend1] = 1;
    }

    int sorted[friends];
    int sortedLength = 0;

    char click[friends];
    int clickLength = 0;

    for (i = 0; i < friends; i++) {
        sorted[i] = -1;
        click[i] = 0;
    }

    int savedLine, savedLineCount, count;
    char isClick, isOnClick;

    for (i = 0; i < friends; i++) {
        savedLineCount = 0;
        
        for (line = 0; line < friends; line++) {
            isOnClick = FALSE;
            count = 0;

            for (item = 0; item < friends; item++) {
                if (matriz[line][item]) count++;

                if (sorted[item] == line) {
                    isOnClick = TRUE;
                    break;
                }
            }
            
            if (count > savedLineCount && !isOnClick) {
                savedLineCount = count;
                savedLine = line;
            }
        }

        sorted[sortedLength] = savedLine;
        sortedLength++;
    }

    for (line = 0; line < friends; line++) {
        isClick = TRUE;

        for (i = 0; i < friends; i++) {
            if (click[i] == 1 && matriz[sorted[line]][i] == 0) {
                isClick = FALSE;
            }
        }

        if (isClick) {
            click[sorted[line]] = 1;
            clickLength++;
        }
    }

    fprintf(writeFile, "%d\n", clickLength);

    for (i = 0; i < friends; i++) {
        if (click[i] != 0) fprintf(writeFile, "%d\n", i);
    }

    fclose(readFile);
    fclose(writeFile);

    return 0;
}
