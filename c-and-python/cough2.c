#include <stdio.h>

void cough(void);

int main(void){
    for(int i = 0; i < 3; i++){
        cough();
    }

    return 0;
}

void cough(void){
    printf("cough\n");
}