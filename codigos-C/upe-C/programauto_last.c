#include <stdio.h>
#include <stdlib.h>

int main(void){
    int numero = 10;

    printf("Valor de numero: %d\n", numero);

    // %p exibe o endereço em hexadecimal
    printf("Endereço de número (&numero): %p\n", (void*)&numero); // Ex:  0x7ffd123

    printf("O valor guardado na memória é:");


}
