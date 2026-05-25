# cadastro
import time

while True:
    try:
        nome = input("Digite seu nome: ")
        if not nome.replace(" ", "").isalpha():
            raise ValueError("Digite apenas letras")
        senha = int(input("Digite sua senha: "))
        break
    except ValueError:
        print("Tente novamente. \nVocê será encaminhado para a página inicial")
        print("="*30)
        time.sleep(1)

if nome and senha:
    print("Bem vindo, ", nome)
