# Fundamentos de Programação
# Criação e manipulação de listas

# Lista é uma estrutura de dados que permite
# armazenar múltiplos valores, como numeros, textos e outros tipos.

# as listas são: ordenadas e mutáveis.

# pode criar uma lista usando: list()
# exemplo: list((1, 2, 3))
# resultado: [1, 2, 3]

# acessar elemento de uma lista:
# exemplo: nomes: ["Ana", "Carlos", "Bruno"]
# print(nomes[0]) = Ana
# print(nomes[2]) = Bruno

# Nota: o índice começa em 0.
# Nota 2: Pode usar indices negativos para achar elementos na lista.
# exemplo: print(nomes[-1]) = Bruno

# algumas funções para manipular listas:
# .append() inserir algo no final da lista
# .insert() inserir algo na lista, mas pode escolher o que e a posição.
# .pop() deletar o ultimo item da lista
# .pop(x) x sendo um número (índice), vai deletar o item na posição digitada.
# .sort() vai ordenar em ordem crescente.
# .sort(reverse=True) vai ordenar em ordem decrescente.
# len() vai ler os itens na lista em ordem crescente.

# EXERCICIO 1

nomes = ["Ana", "Bruno", "Carlos", "Daniel"]

print(f"{nomes[0]} e {nomes[2]}\n")
print("======= EXERCICIO 1 =======")

# EXERCICIO 2 (USANDO A LISTA DO EX. 1)

print(f"\n{nomes[-1]} e {nomes[-2]}")

# EXERCICIO 3

nomes = ["Ana", "Bruno", "Carlos"]

nomes[1] = "Beatriz"

print(f"{", ".join(nomes)}")


# EXERCICIO 4
numeros = [10, 20, 30, 40, 50]

for v in numeros:
    if v == 30:
        print(f"{numeros[0]}, {numeros[-1]}, {v}")

# EXERCICIO 5

valores = [5, 10, 15, 20]

soma = valores[0] + valores[-1]

print(f"a soma é {soma}")

# EXERCICIO 6

# numeros = []

for i in range(5):
    numero = str(input("digite um numero: "))
    numeros.append(numero)

print(f"{", ".join(numeros)}\nPrimeiro Numero: {numeros[0]}\nÚltimo Numero: {numeros[-1]}")

# EXERCICIO 7

numeros = []
maiorNumero = None
menorNumero = None
soma = 0
contador = 0

for i in range(5):
    contador += 1
    numero = int(input("Digite um numero: "))
    soma += numero
    numeros.append(numero)
    maiorNumero = max(numeros)
    menorNumero = min(numeros)

media = soma/contador

print(f"\n{numeros}\n{maiorNumero}\n{menorNumero}\n{media}")