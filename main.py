import pandas as pd
import plotly.express as px

# Importando a base de dados
tabela = pd.read_csv("cancelamentos.csv")
print(tabela)

# Excluindo colunas que não serão úteis para a análise
tabela = tabela.drop(columns="CustomerID") # "informações que não ajudam atrapalham"
print(tabela)

# Procurando possíveis erros na base de dados
print(tabela.info()) # Encontrado: colunas vazias!

# Excluindo linhas vazias para melhorar a acurácia da análise
tabela = tabela.dropna()
print(tabela.info())

# Mostrando a porcentagem de cancelamentos
print(tabela["cancelou"].value_counts(normalize=True))

# Para cada coluna na lista de colunas da tabela
for coluna in tabela.columns:
    graficoCancelamentos = px.histogram(tabela, x=coluna, color="cancelou") # o grafico de cancelamentos será um histograma, com highlight nos cancelamentos
    graficoCancelamentos.show()


# É possível ver que os clientes com planos mensais, clientes com mais de 4 ligações ao call center e clientes com mais de 20 dias de atraso irão cancelar o plano.

# Criando uma tabela com os filtros para descobrir o número de cancelamentos
tabelaCancelamentos = tabela.query("duracao_contrato != 'Monthly' and ligacoes_callcenter <= 4 and dias_atraso <= 20")

print(tabelaCancelamentos["cancelou"].value_counts(normalize=True)) # 81,6% dos clientes nessas condições cancelaram o plano

# A partir dessa análise é possível visualizar motivos de cancelamento e sugerir melhorias  para aumentar a retenção de clientes. 