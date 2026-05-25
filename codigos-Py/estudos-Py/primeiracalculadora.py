import math
import time

def adicao(a, b):
    a = float(a)
    b = float(b)
    return a+b

def subtracao(a, b):
    a = float(a)
    b = float(b)
    return a-b

def multiplicacao(a, b):
    a = float(a)
    b = float(b)
    return a*b

def divisao(a, b):
    a = float(a)
    b = float(b)
    return a/b

def raizquadrada(a):
    a = float(a)
    return math.sqrt(a)

numero1 = 0
numero2 = 0

while True:
    print("\nCalculadora\nDigite o primeiro número, depois a operação, e depois o segundo")
    numero1 = float(input("Digite o primeiro número: "))
    time.sleep(1)

    lista_operacoes = [1, 2, 3, 4, 5]

    operacaodig = int(input("Digite a operação que deseja realizar\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Raiz Quadrada\n"))
    while operacaodig in lista_operacoes:

        if operacaodig == 5:

            if numero1 >= 0:
                print(f"A raiz quadrada de {numero1} é: {raizquadrada(numero1)} ")
                time.sleep(2)
                break
            else:
                print("Raiz quadrada de números negativos não existem.")

        else:

            numero2 = float(input("Digite o segundo número: "))

            if operacaodig not in lista_operacoes:
                print("Digite um valor válido para usar a calculadora")
                break
            else:
                if operacaodig == 1:
                    print(f"A soma de {numero1} com o {numero2} é de: {adicao(numero1, numero2)}")
                    time.sleep(2)
                    break
                elif operacaodig == 2:
                    print(f"A subtração de {numero1} com o {numero2} é de {subtracao(numero1, numero2)}")
                    time.sleep(2)
                    break
                elif operacaodig == 3:
                    print(f"A múltiplicação de {numero1} com o {numero2} é de {multiplicacao(numero1, numero2)}")
                    time.sleep(2)
                    break
                elif operacaodig == 4:
                    print(f"A divisão de {numero1} com o {numero2} é de {divisao(numero1, numero2)}")
                    time.sleep(2)
                    break