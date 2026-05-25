# numeros = []

# for i in range(10):
#     numero = int(input("Digite um numero: "))
#     numeros.append(numero)
    
# numerosOrdenados = sorted(numeros, reverse=False)
# print("Numeros em ordem: ", numerosOrdenados)

# numero = 0
# while numero < 10:
#     numero += 1
#     print(numero)

# soma = 0

# while True:
#     numero = int(input("Digite o numero (Digite 0 para sair): "))
#     if numero < 0:
#         print("O numero é negativo, tente novamente.")
#     elif numero == 0:
#        break
#     else:
#         soma = numero + soma

# print(f"A soma é: {soma}")

# while True:
#     usuario = input("Digite seu nome de usuario: ")
#     senha = int(input("Digite sua senha: "))

#     if usuario == "admin" and senha == 1234:
#         print("Acesso concedido")
#         break
#     else:
#         print("Usuario ou senha incorretos, tente novamente.") 


# numero = 0

# while numero <= 100:
#     numero = numero + 1
#     if numero % 3 == 0:
#         print(numero)
#     else:
#         continue


valores=[5, 10, 15, 20]
resultado = 0

for v in valores:
    if v % 10 == 0:
        resultado += v
    else:
        resultado += 1

print(resultado)

# 0 + 5 = 5
# 5 + 1 = 6
# 6 + 15 = 21
# 21 + 11 = 32 
