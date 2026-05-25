#include <stdio.h>
#include <string.h>

int main()
{
    char nome[50];

    printf("Digite o seu nome: ");
    fgets(nome, 50,stdin);

    printf("Nome digitado: %s", nome);
    return 0;

}
