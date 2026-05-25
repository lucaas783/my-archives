arquivo = open("testedados.txt", "w", encoding="utf-8")

arquivo.write("Hello World!")

arquivo.close()

arquivo = open("testedados.txt", "r", encoding="utf-8")

for linha in arquivo:
    print(linha)

arquivo.close()

# Boa Prática:
# o 'with' é uma boa pratica e nao precia usar a function .close() porque o with ja faz isso

try:
    with open("testedados.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print("O arquivo não foi encontrado.")


# aplicações praticas:

# 1. cadastro de alunos
# 2. controle de estoque
# 3. lista de tarefas
# 4. Sistema de login
# 5. registro de notas