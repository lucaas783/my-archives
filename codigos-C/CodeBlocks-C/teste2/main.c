#include <stdio.h>
#include <stdlib.h>
#include <iso646.h>

int main()
{
    int escolha;
    char F1 [] = "Carros, 2h03 min";
    char F2 [] = "Operação big hero";
    char F3 [] = "Divertida mente";

    /*while true do{


        if ( escolha == 1){
            print("o filme escolhido foi: %c", F1);
        }
    }*/

    printf("escolha o filme: ");
    scanf("%d", &escolha);

    switch (escolha){
    case 1:
        printf("o filme escolhido foi: %s", F1);
        break;
    case 2:
        printf("o filme escolhido foi: %s", F2);
        break;
    case 3:
        printf("o filme escolhido foi: %s", F3);
        break;
    default:
        printf("digite um valor válido");
}
return 0;
}
