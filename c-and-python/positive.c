#include <stdio.h>
#include <cs50.h>

int get_positive_int(void);

int main(void){
    int i = get_positive_int();
    printf("%i is a positive integer\n", i);
    return 0;
}

int get_positive_int(void){
    int n;
    do {
        printf("n is ");
        n = get_int();
    } while (n < 1);
    return n;
}