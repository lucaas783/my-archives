#include <stdio.h>
#include <string.h>
#include <iso646.h>

int main(void)
{

    char senha_correta[] = "lucas10"; // senha fixa; Nota: o [] vazio significa que pode-se ter um número indefinido de caracteres
    char nome_correto[] = "lucas";
    char tentativa_senha[50];
    char tentativa_nome[50];
    int contador = 0;

    while (contador < 4)
        {

            printf("Digite a senha: ");
            fgets(tentativa_senha, 50, stdin); // ler tentativa do usuário

            tentativa_senha[strcspn(tentativa_senha, "\n")] = '\0';

            printf("Digite o nome: ");
            fgets(tentativa_nome, 50, stdin);

            tentativa_nome[strcspn(tentativa_nome, "\n")] = '\0';

            if (strcmp(tentativa_senha, senha_correta) == 0 and strcmp(tentativa_nome, nome_correto) == 0)
            {
                printf("\nAcesso concedido!\n");
                break;
            }
            else
            {
                printf("\nSenha Incorreta! \n");
                contador++;
            }
            //return 0;

        }
}

