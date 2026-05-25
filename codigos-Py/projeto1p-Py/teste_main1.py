from teste_modular1 import Carros

for marca, modelos in Carros.items():
    carroDigitado = str(input("Digite a marca do carro: "))
    if carroDigitado in Carros:
        # print(f"{marca}: {', '.join(modelos)}")
        print(f"O carro: {carroDigitado} é um carro válido e está na lista.")
        break
    else:
        print("Marca de carro não encontrada. Tente novamente.")

# explicação do codigo:
# 1. marca vai ser a variavel temporaria das MARCAS de carros do teste_modular1
# 2. modelos vai ser a variavel temporaria dos MODELOS de carros do teste_modular1
# 3. o '.items' vai dividir o dicionario em chave e valor, ou seja, marca e modelos
# 4. o 'join' vai juntar os modelos em uma string, separando por ', ''

# codigo exemplo abaixo:

# dicionario = {"maca": 5, "pera": 10}

# for fruta, numero in dicionario.items():
#     print(fruta, numero)