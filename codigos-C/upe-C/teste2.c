#include <stdio.h>
#include <iso646.h>
#include <stdbool.h>

int main(void)
{
    int idade;
    char nome[100];

    printf("Digite a sua idade: ");
    scanf("%d", &idade);
    printf("\nVocê tem %d anos", idade);
    printf("\n==============================");
    printf("\nDigite o seu nome: ");
    scanf("%s", &nome);
    printf("\nSeu nome é: %s", nome);

    if (idade <= 100 and idade == 18 and nome != " ")
    {
        printf("\nVocê é maior de idade, %s\n", nome);
    }
    else if (idade < 18 and nome != " ")
    {
        printf("\nVocê é menor de idade, %s\n", nome);
    }
    else
    {
        printf("\nAlgo está errado\n");
    }
    
    return 0;
}