#include <stdio.h>

int main(void)
{
    char nome[50];
    int idade;
    
    printf("Digite o seu nome: ");
    scanf("%s", &nome);

    printf("Digite a sua idade: ");
    scanf("%i", &idade);

    if (nome && idade)
    {
        printf("O seu nome é: %s e a sua idade é: %i", nome, idade);
    }
    else
    {
        return 0;
    }

}