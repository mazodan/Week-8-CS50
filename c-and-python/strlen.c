#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void){
    string s = get_string();
    int n = 0;
    while(s[n] != '\0'){
        n++;
    }
    printf("%i\n", n);

    // Higher level implementation
    printf("%i\n", strlen(s));

    return 0;


}