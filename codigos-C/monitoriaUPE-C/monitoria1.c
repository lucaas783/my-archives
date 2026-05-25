#include <stdio.h>
#include <iso646.h>

float calculadora(float x, float y, int z)
{
    if (z == 1) return x+y;
    else if (z == 2) return x-y;
    else if (z == 3) return x*y;
    else if (z == 4) if (z == 0) return 0; else return x/y;

}
int main (void)
{
    float a, b, c;

    printf("\nWelcome to the best calculator in the world\n");
}