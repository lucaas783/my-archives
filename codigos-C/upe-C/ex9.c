#include <stdio.h>
#include <iso646.h>
#include <time.h>

int main (void)
{
    char nome[100];
    long idadeAtual;
    int idadeUser;
    int idadeUserSubtraida;
    long tempoAtual;
    
    tempoAtual = time(NULL);
    printf("%ld", tempoAtual);

    printf("\nDigite o seu nome: ");
    scanf("%s", &nome);
    printf("\nDigite o ano que você nasceu");
    scanf("%d", &idadeUser);

    idadeUserSubtraida = idadeUser - 1970;
    idadeUserSubtraida = idadeUserSubtraida * 365.25 * 24 * 3600;

    idadeAtual = tempoAtual - idadeUserSubtraida;

    printf("Olá %s, você tem %ld segundos de idade", nome, idadeAtual);

}