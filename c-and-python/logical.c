#include <stdio.h>
#include <cs50.h>

int main(void){
    char c = get_char();

    if(c == 'c' || c == 'C'){
        printf("yes\n");
    } else if (c == 'n' || c == 'N') {
        printf("no\n");
    } else {
        printf("error\n");
    }

    return 0;
}