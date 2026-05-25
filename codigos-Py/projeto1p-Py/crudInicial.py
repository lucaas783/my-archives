import sqlite3
import math
import hashlib
import re
from colorama import Fore
from os import system

# ==============================================================
# ALTERAÇÃO 1: Remoção do import "os" (não estava sendo usado)
# e adição do "re" para validação de e-mail via expressão regular.
# ==============================================================

CAMINHO_BANCO = "usuarios.db"

# ==============================================================
# ALTERAÇÃO 2: Constante no lugar de variável global.
# "caminho_banco" virou "CAMINHO_BANCO" (letras maiúsculas).
# Em Python, o padrão de nomenclatura para constantes é SNAKE_CASE
# em maiúsculas. Isso deixa claro para qualquer dev que esse valor
# não deve ser alterado durante a execução.
# ==============================================================


# ========================
# CONEXÃO CENTRALIZADA
# ========================

def get_conexao():
    """Retorna uma conexão com o banco de dados."""
    return sqlite3.connect(CAMINHO_BANCO)

# ==============================================================
# ALTERAÇÃO 3: Função get_conexao() centralizada.
# Antes, cada função repetia sqlite3.connect(caminho_banco).
# Agora existe um único ponto de controle para a conexão.
# Se o caminho mudar ou precisarmos adicionar configurações
# (ex: timeout, detect_types), basta alterar aqui.
# ==============================================================


# ========================
# BANCO DE DADOS
# ========================

def criar_banco():
    """Cria a tabela de usuários se ainda não existir."""
    with get_conexao() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                nome  TEXT    NOT NULL,
                email TEXT    NOT NULL UNIQUE,
                senha TEXT    NOT NULL
            )
        """)

# ==============================================================
# ALTERAÇÃO 4: Uso do gerenciador de contexto "with".
# Antes: conexao = sqlite3.connect(...) / conexao.commit() /
#        conexao.close() — repetido em toda função.
# Agora: "with get_conexao() as conexao" faz commit automático
# em caso de sucesso e rollback em caso de exceção, além de
# fechar a conexão corretamente ao sair do bloco.
# ==============================================================

# ==============================================================
# ALTERAÇÃO 5: UNIQUE na coluna e-mail no schema.
# Antes, a unicidade era verificada manualmente com um SELECT
# antes de todo INSERT. Agora o próprio banco garante isso, o que
# é mais seguro e evita condições de corrida (race conditions).
# ==============================================================


# ========================
# SEGURANÇA
# ========================

def hash_senha(senha: str) -> str:
    """Retorna o hash SHA-256 da senha."""
    return hashlib.sha256(senha.encode()).hexdigest()

def validar_email(email: str) -> bool:
    """Valida o formato básico de um e-mail."""
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return re.match(padrao, email) is not None

# ==============================================================
# ALTERAÇÃO 6: Hash de senha com SHA-256.
# Antes, a senha era salva em texto puro no banco — qualquer
# pessoa com acesso ao arquivo .db conseguia ler todas as senhas.
# Agora ela é convertida em hash antes de salvar ou comparar.
# SHA-256 é uma função unidirecional: não é possível recuperar
# a senha original a partir do hash.
#
# ALTERAÇÃO 7: Validação de e-mail com expressão regular.
# Antes, qualquer string era aceita como e-mail.
# A regex verifica o formato básico: algo@algo.extensao
# evitando cadastros com dados claramente inválidos.
# ==============================================================


# ========================
# CREATE — Cadastro
# ========================

def cadastrar_usuario():
    system("cls")
    print(Fore.GREEN + "\n==========================\n  🍃 EcoVolt Analytics\n==========================")
    print(Fore.YELLOW + "\n=== CADASTRO ===")

    nome  = input("Nome: ").strip()
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()

    if not nome or not email or not senha:
        print("❌ Preencha todos os campos!")
        return

    if not validar_email(email):
        print("❌ Formato de e-mail inválido!")
        return

    try:
        with get_conexao() as conexao:
            conexao.execute(
                "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                (nome, email, hash_senha(senha))
            )
        print(f"✅ Cadastro realizado! Bem-vindo, {nome}!")
        menu_logado(nome, _buscar_id_por_email(email))

    except sqlite3.IntegrityError:
        print("❌ E-mail já cadastrado!")

# ==============================================================
# ALTERAÇÃO 8: Tratamento de IntegrityError no lugar de SELECT
# preventivo. Como o campo email agora tem UNIQUE no banco,
# tentar inserir um e-mail duplicado lança sqlite3.IntegrityError.
# Capturamos essa exceção diretamente — mais simples e seguro.
#
# ALTERAÇÃO 9: Após o cadastro, chamamos menu_logado() passando
# nome e id do usuário, em vez de ir direto ao simulador.
# Isso permite que o usuário acesse edição, exclusão etc.
# ==============================================================


# ========================
# READ — Login e Busca
# ========================

def login_usuario():
    system("cls")
    print(Fore.GREEN + "\n==========================\n  🍃 EcoVolt Analytics\n==========================")
    print(Fore.YELLOW + "\n=== LOGIN ===")

    email = input("Email: ").strip()
    senha = input("Senha: ").strip()

    with get_conexao() as conexao:
        cursor = conexao.execute(
            "SELECT id, nome FROM usuarios WHERE email = ? AND senha = ?",
            (email, hash_senha(senha))
        )
        usuario = cursor.fetchone()

    if usuario:
        usuario_id, nome = usuario
        print(f"✅ Bem-vindo, {nome}!")
        menu_logado(nome, usuario_id)
    else:
        print("❌ E-mail ou senha incorretos!")

# ==============================================================
# ALTERAÇÃO 10: Login agora compara o hash da senha digitada
# com o hash salvo no banco, e retorna também o id do usuário.
# O id é essencial para as operações de UPDATE e DELETE.
# ==============================================================

def _buscar_id_por_email(email: str):
    """Auxiliar interno: retorna o id do usuário pelo e-mail."""
    with get_conexao() as conexao:
        cursor = conexao.execute(
            "SELECT id FROM usuarios WHERE email = ?", (email,)
        )
        resultado = cursor.fetchone()
    return resultado[0] if resultado else None

def listar_usuarios():
    """Exibe todos os usuários cadastrados (sem mostrar a senha)."""
    system("cls")
    print(Fore.GREEN + "\n==========================\n  🍃 EcoVolt Analytics\n==========================")
    print(Fore.YELLOW + "\n=== USUÁRIOS CADASTRADOS ===")
    with get_conexao() as conexao:
        cursor = conexao.execute("SELECT id, nome, email FROM usuarios")
        usuarios = cursor.fetchall()

    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for u in usuarios:
        print(f"ID: {u[0]} | Nome: {u[1]} | Email: {u[2]}")

# ==============================================================
# ALTERAÇÃO 11: listar_usuarios() — Read completo.
# Antes o Read só existia de forma implícita dentro do login.
# Agora temos uma função dedicada que exibe todos os registros,
# nunca expondo o campo senha (nem o hash).
# ==============================================================


# ========================
# UPDATE — Atualização
# ========================

def atualizar_usuario(usuario_id: int):
    system("cls")
    print(Fore.GREEN + "\n==========================\n  🍃 EcoVolt Analytics\n==========================")
    print(Fore.YELLOW + "\n=== ATUALIZAR CADASTRO ===")
    print("(Pressione Enter para manter o valor atual)\n")

    novo_nome  = input("Novo nome: ").strip()
    novo_email = input("Novo e-mail: ").strip()
    nova_senha = input("Nova senha: ").strip()

    if novo_email and not validar_email(novo_email):
        print("❌ Formato de e-mail inválido!")
        return

    campos_alterados = False

    try:
        with get_conexao() as conexao:
            if novo_nome:
                conexao.execute(
                    "UPDATE usuarios SET nome = ? WHERE id = ?",
                    (novo_nome, usuario_id)
                )
                campos_alterados = True

            if novo_email:
                conexao.execute(
                    "UPDATE usuarios SET email = ? WHERE id = ?",
                    (novo_email, usuario_id)
                )
                campos_alterados = True

            if nova_senha:
                conexao.execute(
                    "UPDATE usuarios SET senha = ? WHERE id = ?",
                    (hash_senha(nova_senha), usuario_id)
                )
                campos_alterados = True

        if campos_alterados:
            print("✅ Dados atualizados com sucesso!")
        else:
            print("ℹ️  Nenhum campo alterado.")

    except sqlite3.IntegrityError:
        print("❌ Este e-mail já está em uso por outro usuário!")

# ==============================================================
# ALTERAÇÃO 12: UPDATE implementado (era inexistente).
# Permite atualizar nome, e-mail e/ou senha individualmente.
# Campos deixados em branco não são modificados.
# A nova senha também passa pelo hash antes de ser salva.
# O e-mail novo também é validado antes de tentar o UPDATE.
# ==============================================================


# ========================
# DELETE — Exclusão
# ========================

def deletar_usuario(usuario_id: int):
    system("cls")
    print(Fore.GREEN + "\n==========================\n  🍃 EcoVolt Analytics\n==========================")
    print(Fore.YELLOW + "\n=== DELETAR CONTA ===")
    confirmacao = input("⚠️  Esta ação é irreversível! Digite 'CONFIRMAR' para prosseguir: ").strip()

    if confirmacao != "CONFIRMAR":
        print("❌ Operação cancelada.")
        return

    with get_conexao() as conexao:
        conexao.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id,))

    print("✅ Conta deletada com sucesso!")

# ==============================================================
# ALTERAÇÃO 13: DELETE implementado (era inexistente).
# Exige que o usuário digite "CONFIRMAR" (em vez de apenas s/n)
# para reduzir o risco de exclusão acidental.
# Após a confirmação, remove o registro pelo id — nunca por nome
# ou e-mail, evitando deletar o usuário errado.
# ==============================================================


# ========================
# SIMULADOR SOH
# ========================

def simulador(nome_usuario: str):
    system("cls")
    print(Fore.GREEN + "\n==========================\n  🍃 EcoVolt Analytics\n==========================")
    print(Fore.YELLOW + f"\n=== SIMULADOR SOH ===")
    print(f"Olá, {nome_usuario}!\n")

    try:
        modelo      = input("Modelo do carro: ").strip()
        ciclos      = float(input("Ciclos de carga: "))
        anos        = float(input("Idade (anos): "))
        temperatura = float(input("Temperatura média (°C): "))
        c_rate      = float(input("Taxa de carga (C-Rate): "))

        # Constantes do modelo de degradação
        k1, alpha = 0.02, 0.7
        k2, beta  = 1.5,  1.0
        k3, Ea    = 5000, 50000
        k4, gamma = 2.0,  1.3
        R         = 8.314

        T = temperatura + 273.15

        D_ciclos   = k1 * (ciclos ** alpha)
        D_tempo    = k2 * (anos   ** beta)
        D_temp     = k3 * math.exp(-Ea / (R * T)) * anos
        D_operacao = k4 * (c_rate ** gamma)

        SOH = 100 - (D_ciclos + D_tempo + D_temp + D_operacao)
        SOH = max(0.0, min(100.0, SOH))

        if SOH > 90:
            status = "Excelente 🟢"
        elif SOH > 80:
            status = "Bom 🟡"
        elif SOH > 60:
            status = "Desgastada 🔴"
        else:
            status = "Fim de Vida ⚫"

        system("cls")
        print("\n=== RESULTADO ===")
        print(f"Modelo : {modelo}")
        print(f"SOH    : {SOH:.2f}%")
        print(f"Status : {status}")

    except ValueError:
        print("❌ Erro: insira apenas números válidos!")

# ==============================================================
# ALTERAÇÃO 14: Anotação de tipo nos parâmetros (nome_usuario: str).
# Pequena melhoria de legibilidade — deixa explícito o tipo
# esperado sem adicionar dependências externas.
# O cálculo do SOH não foi alterado.
# ==============================================================


# ========================
# MENU PÓS-LOGIN
# ========================

def menu_logado(nome: str, usuario_id: int):
    """Menu exibido após autenticação bem-sucedida."""

    system("cls")

    opcoes = {
        "1": ("Simulador SOH",      lambda: simulador(nome)),
        "2": ("Atualizar cadastro", lambda: atualizar_usuario(usuario_id)),
        "3": ("Deletar minha conta",lambda: _deletar_e_sair(usuario_id)),
        "4": ("Listar usuários",    listar_usuarios),
        "5": ("Sair da conta",      None),
    }

    while True:
        system("cls")
        print(Fore.GREEN + "\n==========================\n  🍃 EcoVolt Analytics\n==========================")
        print(Fore.YELLOW + f"\n===== MENU ({nome}) =====")
        for chave, (descricao, _) in opcoes.items():
            print(f"({chave}) {descricao}")

        escolha = input("Escolha: ").strip()

        if escolha not in opcoes:
            print("❌ Opção inválida!")
            continue

        descricao, acao = opcoes[escolha]

        if acao is None:          # opção "Sair da conta"
            print("👋 Sessão encerrada.")
            break

        acao()

        if escolha == "3":        # conta foi deletada
            break

# ==============================================================
# ALTERAÇÃO 15: Menu pós-login separado do menu principal.
# Antes, após o login/cadastro o programa ia direto ao simulador
# e encerrava. Agora existe um menu com todas as operações CRUD
# disponíveis enquanto o usuário está autenticado.
# O usuário_id é mantido na sessão para uso em UPDATE e DELETE.
# ==============================================================

def _deletar_e_sair(usuario_id: int):
    """Deleta a conta e sinaliza saída do menu_logado."""
    deletar_usuario(usuario_id)

# ========================
# MENU PRINCIPAL
# ========================

def menu():
    while True:
        
        system("cls")
        print(Fore.GREEN + "\n==========================\n  🍃 EcoVolt Analytics\n==========================")
        print(Fore.YELLOW + "\n===== MENU PRINCIPAL =====")
        print("(1) Login")
        print("(2) Cadastro")
        print("(3) Sair")

        escolha = input("Escolha: ").strip()

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