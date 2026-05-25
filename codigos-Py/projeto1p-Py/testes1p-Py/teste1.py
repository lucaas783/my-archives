def contaVogal(palavra):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador +=1
    return contador

while True:

    palavra = input("Digite uma palavra:")
    print(contaVogal(palavra))
    resposta = input("Deseja continuar? (s/n)")
    if resposta.lower() != "s":
        break

