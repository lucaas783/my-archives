# exercicio 1:

#try:
#    numero = int(input("digite o seu numero: "))
#except ValueError:
#    print("entrada invalida, apenas diigte numeros inteiros")
#else:
#    print("numero valido")

# exercicio 2:

#def divisao(a, b):
#    a = int(a)
#    b = int(b)
#    return a/b

#try:
#    numero1 = int(input("digite um numero: "))
#    numero2 = int(input("digite o divisor do numero: "))
#    resultado = divisao(numero1, numero2)
#except ValueError:
#    print("apenas digite numeros")
#except ZeroDivisionError:
#    print("nao pode divisao por zero")
#else:
#    print(resultado)

# exercicio 3:

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

while True:
    try:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        if operacao == "+":
            resultado = adicao(numero1, numero2)
        elif operacao == "-":
            resultado = subtracao(numero1, numero2)
        elif operacao == "*":
            resultado = multiplicacao(numero1, numero2)
        elif operacao == "/":
            resultado = divisao(numero1, numero2)
        print(f"O resultado é: {resultado}")
    except ValueError:
        print("Digite apenas números inteiros.")
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")