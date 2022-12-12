#include <stdio.h>
#include <stdlib.h>

typedef struct List {
    int value;
    struct List *prev, *next;
} List;

int length = 0;
List *first = NULL;
List *last = NULL;

void addItem(int value, int pos) {
    if (pos >= 0 && pos <= length) {
        List *new = malloc(sizeof(List));
        new->value = value;
        new->prev = NULL;
        new->next = NULL;

        if (first == NULL) {
            first = new;
            last = new;
        } else if (pos == 0) {
            new->next = first;
            first->prev = new;
            first = new;
        } else if (pos == length) {
            last->next = new;
            new->prev = last;
            last = new;
        } else {
            List *hook = first;
            for (int i = 0; i < pos - 1; i++) {
                hook = hook->next;
            }

            new->next = hook->next;
            hook->next = new;
            new->prev = hook;
            new->next->prev = new;
        }
        
        length++;
    }
}

int removeItem(int pos) {
    if (pos >= 0 && pos < length) {
        List *trash;

        if (length == 1) {
            trash = first; 
            first = NULL;
            last = NULL;
        } else if (pos == 0) {
            trash = first;
            first = first->next;
        } else if (pos == length - 1) {
            trash = last;
            last->prev->next = NULL;
            last = last->prev;
        } else {
            List *hook = first;

            for (int i = 0; i < pos - 1; i++) {
                hook = hook->next;
            }   

            trash = hook->next;
            hook->next = trash->next;
            trash->next->prev = hook;
        }

        length--;

        int value = trash->value;
        free(trash);   

        return value;
    }
}

void print() {
    List *hook = first;

    printf("---LISTA----\n");

    for (int i = 0; i < length; i++) {
        printf("VALOR: %d\n", hook->value);
        hook = hook->next;
    }
}

int main() {
    addItem(5, 0);
    addItem(10, 1);
    addItem(20, 2);
    addItem(25, 3);
    addItem(15, 2);
    print();
    removeItem(2);
    print();
    
    return 0;
}