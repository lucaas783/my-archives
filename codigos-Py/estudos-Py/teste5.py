age = 0
name = None
email = None
senha = None

contador = 0
cadastro = {}

while contador == 0:
    try:
        name = str(input("Digite seu nome: "))
        if name.isalpha() == False:
            raise ValueError("O nome só pode conter letras.")
        cadastro["nome"] = name
        email = str(input("Digite seu email: "))
        if "@" not in email or "." not in email:
            raise ValueError("O email não é válido.")
        cadastro["email"] = email
        senha = str(input("Digite sua senha: "))
        if len(senha) < 8:
            raise ValueError("A senha deve conter pelo menos 8 caracteres.")
        cadastro["senha"] = senha
        print("Cadastro realizado com sucesso!")
        print(cadastro)
        contador += 1
        break
    except ValueError as error:
        print(error)