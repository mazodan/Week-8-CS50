#include <stdio.h>
#include <cs50.h>

int main(void){
    printf("x is ");
    int x = get_int();

    printf("y is ");
    int y = get_int();

    // Perform some calculations
    printf("%i plus %i is %i\n", x, y, x + y);
    printf("%i minus %i is %i\n", x, y, x - y);
    printf("%i times %i is %i\n", x, y, x * y);
    printf("%i divided by %i is %i\n", x, y, x / y);
    printf("remainder of %i divided by %i is %i\n", x, y, x % y);

    return 0;
}