import sqlite3
import os
import math
import hashlib

# Banco de dados
caminho_banco = "usuarios.db"

def criar_banco():
    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT NULL
    )
    """)
    conexao.commit()
    conexao.close()

# ========================
# CADASTRO
# ========================
def cadastrar_usuario():
    print("\n=== CADASTRO ===")
    
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()
    
    if not nome or not email or not senha:
        print("❌ Preencha todos os campos!")
        return
    
    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.cursor()
    
    cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
    if cursor.fetchone():
        print("❌ Email já cadastrado!")
        conexao.close()
        return
    
    cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                   (nome, email, senha))
    conexao.commit()
    conexao.close()
    
    print(f"✅ Cadastro realizado! Bem-vindo, {nome}!")
    simulador(nome)

# ========================
# LOGIN
# ========================
def login_usuario():
    print("\n=== LOGIN ===")
    
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()
    
    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.cursor()
    
    cursor.execute("SELECT nome FROM usuarios WHERE email = ? AND senha = ?",
                   (email, senha))
    usuario = cursor.fetchone()
    conexao.close()
    
    if usuario:
        print(f"✅ Bem-vindo, {usuario[0]}!")
        simulador(usuario[0])
    else:
        print("❌ Email ou senha incorretos!")

# ========================
# SIMULADOR SOH
# ========================
def simulador(nome_usuario):
    print(f"\n=== SIMULADOR SOH ===")
    print(f"Olá, {nome_usuario}!\n")
    
    try:
        modelo = input("Modelo do carro: ")
        ciclos = float(input("Ciclos de carga: "))
        anos = float(input("Idade (anos): "))
        temperatura = float(input("Temperatura média (°C): "))
        c_rate = float(input("Taxa de carga (C-Rate): "))
        
        # Constantes
        k1, alpha = 0.02, 0.7
        k2, beta = 1.5, 1
        k3, Ea = 5000, 50000
        k4, gamma = 2, 1.3
        R = 8.314
        
        T = temperatura + 273.15
        
        D_ciclos = k1 * (ciclos ** alpha)
        D_tempo = k2 * (anos ** beta)
        D_temp = k3 * math.exp(-Ea / (R * T)) * anos
        D_operacao = k4 * (c_rate ** gamma)
        
        SOH = 100 - (D_ciclos + D_tempo + D_temp + D_operacao)
        SOH = max(0, min(100, SOH))
        
        # Status
        if SOH > 90:
            status = "Excelente 🟢"
        elif SOH > 80:
            status = "Bom 🟡"
        elif SOH > 60:
            status = "Desgastada 🔴"
        else:
            status = "Fim de Vida ⚫"
        
        print("\n=== RESULTADO ===")
        print(f"Modelo: {modelo}")
        print(f"SOH: {SOH:.2f}%")
        print(f"Status: {status}")
        
    except ValueError:
        print("❌ Erro: digite apenas números válidos!")

# ========================
# MENU
# ========================
def menu():
    while True:
        print("\n===== MENU =====")
        print("(1) Login")
        print("(2) Cadastro")
        print("(3) Sair")
        
        escolha = input("Escolha: ")
        
        if escolha == "1":
            login_usuario()
        elif escolha == "2":
            cadastrar_usuario()
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("❌ Opção inválida!")

# ========================
# MAIN
# ========================
def main():
    criar_banco()
    menu()

if __name__ == "__main__":
    main()