# data: 14/05/2026

import teste4module as t4m
import time

while True:
    try:
        time.sleep(2)
        print("\nBem vindo ao EcoVolt! \nPor favor, faça o seu cadastro agora.")
        time.sleep(1)
        nome = input("Digite seu nome: ")
        for letra in nome:
            if letra.isdigit():
                raise ValueError("O nome não pode conter números.")
            
        time.sleep(1)    
        idade = int(input("Digite sua idade: "))

        time.sleep(1)
        carro = str(input("Digite o modelo do seu carro: "))
        
        time.sleep(1)
        if carro not in t4m.lista(carros={}):
            raise ValueError("Carro não encontrado em nossa lista de carros elétricos.")
    except ValueError:
        print("Erro: Dados inválidos. Por favor, tente novamente.")
    else:
        print(f"Cadastro realizado com sucesso! Bem-vindo, {nome}!")
        break
    # vou continuar depois
    # o que falta:
    # apuração do modelo do carro
    # cadastro do carro
    # cadastro do usuario e conexao ao db
    # calculo de soh da bateria
    # -- 14/05/26