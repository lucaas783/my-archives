import pandas as pd

# 1. Carregar o seu arquivo CSV
df = pd.read_csv('forms_estatisticaTrabalho_CSV.csv')

# 2. Limpar espaços extras e aspas que costumam poluir os dados
colunas_para_limpar = ['Faculdade', 'Esporte', 'Transporte']
for col in colunas_para_limpar:
    df[col] = df[col].astype(str).str.strip().str.replace('"', '')

# 3. Definir a frequência mínima (ex: se aparecer menos de 5 vezes, vira "Outros")
limite_minimo = 5

for col in colunas_para_limpar:
    # Conta quantas vezes cada categoria aparece
    contagem = df[col].value_counts()
    
    # Mantém apenas o que aparece mais ou igual ao limite
    categorias_principais = contagem[contagem >= limite_minimo].index
    
    # Substitui o restante por 'Outros'
    df[col] = df[col].apply(lambda x: x if x in categorias_principais else 'Outros')

# 4. Salvar o resultado em um novo arquivo CSV
df.to_csv('forms_estatistica_limpo.csv', index=False)
print("Arquivo processado com sucesso!")