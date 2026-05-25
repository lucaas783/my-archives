# revisao av1 primeiro periodo

contador = 0
soma = 0
maior_numero = None
todos_numeros = []
par = []
impar = []

for i in range(10):
    contador += 1
    numero = int(input("digite um numero: "))
    todos_numeros.append(numero)
    maior_numero = max(todos_numeros)
    soma += numero
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

media = soma / contador

# saida de dados
print(f"A soma dos números é: {soma};\nA média dos números é: {media};\nOs números pares são: {par};\nOs números ímpares são: {impar};\nO maior número é: {maior_numero}.")