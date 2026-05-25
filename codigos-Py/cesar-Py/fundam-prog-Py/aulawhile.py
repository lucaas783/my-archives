import time as tempo
soma = 0
totalNumeros = 0
while True:
    print(f"{"="*30}\n Este programa irá solicitar para você digitar números. \n Digite 0 para sair do programa. \n {"="*30}")
    tempo.sleep(1)
    numero = int(input("Digite um número: "))
    if numero == 0:
        print("Saindo do programa...")
        tempo.sleep(1)
        break
    else:
        soma += numero
    totalNumeros += 1

print(f"O somatório é:, {soma}\n O total de números digitados é: {totalNumeros}")

# ---------------------------------------------------------------

senha = "1234"

while senha:
    senhaTentada = input("Digite sua senha: ")
    if not senhaTentada == senha:
        print("Acesso negado")
    else:
        print("Acesso concedido")
        break

while True:
    Usuario = str(input("Digite seu nome de usuario: "))
    Senha = input("Digite sua senha: ")

    if not Usuario == "admin" or not Senha == "1234":
        print("O usuario ou a senha estão incorretos \n Tente novamente.")
    else:
        print("Acesso concedido")
        break

# ---------------------------------------------------------------

soma = 0
contador = 0
while True:
    numero = int(input(f"{"="*30}\n Digite um número: "))
    contador += 1
    soma += numero
    confirmacao = input("Deseja continuar? \n Digite S para continuar \n Digite N para sair. \n")
    if confirmacao.upper() == "N":
        print("Saindo do sistema")
        break
    
    # Eu movi o "contador += 1" e o "soma += numero" para ficar abaixo do contador

media = soma / contador
print(f"{"="*30}\n A média é: {media}\n {"="*30}")

# ---------------------------------------------------------------

soma = 0
contador = 0
par = []
impar = []
NumeroMaior = None

conjuntoDeNumeros = []

for i in range(10):
    contador +=1
    numero = int(input("Digite um numero: "))
    soma += numero
    conjuntoDeNumeros.append(numero)
    NumeroMaior = max(conjuntoDeNumeros)
    if numero % 2 == 1:
        par.append(numero)
    else:
        impar.append(numero)

print(f"{par}\n {impar}\n {NumeroMaior}\n {conjuntoDeNumeros}")

print(f"Soma: {soma}\n Média: {soma/contador} \n Números pares: {par} \n Números Ímpares: {impar}\n Maior Número: {NumeroMaior}")

