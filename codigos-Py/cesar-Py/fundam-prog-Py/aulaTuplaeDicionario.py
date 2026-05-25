# # Lista -> Mutável []
# # Tupla -> Imutável ()
# # Dicionário -> Chave e valor

# # --- TUPLAS ---
# #
# # Estrutura de dados imutável
# # Permite armazenar múltiplos valores
# # Mais segura e eficiente em alguns casos
# # ACESSO A ELEMENTOS:

# nomes = ("Ana", "Bruno", "Carlos")
# print(nomes[0])
# print([-1])

# # IMUTABILIDADE
# # nomes[0] = "João" DÁ ERRO!!
# # Tuplas não podem ser alteradas

# # Quando usar tuplas?
# # Dados fixos (Coordenadas, CPF e datas);
# # Segurança (Evitar alteração acidental);
# # Melhor desempenho em leitura.

# # Exemplo prático:

# coordenada = (3, 7)
# print(f"Eixo X: {coordenada[0]}")
# print(f"Eixo Y: {coordenada[-1]}")

# # Imagine que uma loja deseja armazenar
# # informações fixas de um produto:

# # Nome
# # Preço
# # QUantidade em estoque
# # Código do produto

# # Como essas informações não devem ser alteradas
# # facilmente, podemos usar em uma tupla.

# # Exemplo prático 2:

# produto = ("Notebook", 3500.00, 8, 1025)
# print("Nome do produto:", produto[0])
# print("Preço: R$", produto[1])
# print("Quantidade em estoque:", produto[2])
# print("Código:", produto[3])

# # Exemplo prático 3:

# # Cada aluno será representado por uma tupla
# # contendo:

# # Nome
# # Nota 1
# # Nota 2
# # Frequência
# # O programa deverá:
# # Exibir os dados dos alunos;
# # Calcular a média;
# # Informar se está aprovado ou reprovado

# # --- DICIONÁRIOS ---

# # Criação de dicionário

# aluno = {
#     "nome": "Maria",
#     "idade": 20,
#     "curso": "Python"
# }

# # ACESSANDO DADOS:

# print(aluno["nome"])
# print(aluno["idade"])
# print(aluno["curso"])

# # "nome", "idade", "curso" 
# # são valores de índice.

# # ADICIONANDO VALORES

# aluno["nota"] = 9.5
# print(aluno["nota"])

# # "nota" vai ser adicionado
# # ao final do dicionário.

# # PERCORRENDO DICIONÁRIO

# for chave, valor in aluno.items():
#     print(chave, ":", valor)

# # Exemplo de aplicação:

# produto = {
#     "nome": "Notebook",
#     "preco": 3500.00,
#     "estoque": 10
# }

# for chave, valor in produto.items():
#     produto["estoque"]
#     print(produto, ":",)

# # ATIVIDADE 1

# cores = ("vermelho", "azul", "verde")

# print(cores[0])
# print(cores[-1])

# # ATIVIDADE 2

# cadastro = {
#     "nome": "João",
#     "idade": 25,
#     "cidade": "Recife"
# }

# print(f"Seu nome: {cadastro["nome"]}")

# # ATIVIDADE 3

# dados = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }

# for chave, valor in dados.items():
#     print(chave, valor)

# # ATIVIDADE 7

# alunos = [
#     {"nome": "Ana", "nota": 8},
#     {"nome": "Bruno", "nota": 6}
# ]

# for dicionarios in alunos:
#     if dicionarios["nota"] >= 7:
#         print(dicionarios["nome"], "aprovado")
#     else:
#         print(dicionarios["nome"], "reprovado")

dicionario = {
    "nome": "banana"
}

nome = dicionario["nome"]
print(nome.isalpha())