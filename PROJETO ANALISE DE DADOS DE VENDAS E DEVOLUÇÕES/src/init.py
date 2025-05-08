import os
import pandas as pd
import plotly.express as px

caminho_pasta = r"C:\Users\palla\OneDrive\Desktop\all\Desenvolvimento\PROJETOS\PROJETO ANALISE DE DADOS DE VENDAS E DEVOLUCOES\PROJETO ANALISE DE DADOS DE VENDAS E DEVOLUÇÕES\Vendas"

lista_arquivos = os.listdir(caminho_pasta)
tabela_total = pd.DataFrame()

for arquivo in lista_arquivos:
    if "Vendas" in arquivo or "Devolucoes" in arquivo:
        tabela = pd.read_csv(os.path.join(caminho_pasta, arquivo))
        tabela_total = pd.concat([tabela_total, tabela], ignore_index=True)
print(tabela_total)

tabela_total['Faturamento'] =  tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

tabela_produtos = tabela_total.groupby('Produto').sum(numeric_only=True)
tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)

print("\n Produto mais vendido: ")
print(tabela_produtos)

tabela_faturamento = tabela_total.groupby('Produto').sum(numeric_only=True)
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)

print("\n Faturamento")
print(tabela_faturamento)

tabela_loja = tabela_total.groupby('Loja').sum(numeric_only=True)
tabela_loja = tabela_loja[['Faturamento']]

print("\n Faturamento por loja")
print(tabela_loja)

tabela_devolucao = tabela_total.groupby('Produto').sum(numeric_only=True)
tabela_devolucao = tabela_devolucao[['Quantidade Devolvida']].sort_values(by='Quantidade Devolvida', ascending=False)

print('\n Quantidade Devolvida')
print(tabela_devolucao)

grafico_faturamento_loja = px.bar(tabela_loja, x=tabela_loja.index, y="Faturamento", title="Faturamento por loja") 
grafico_produtos_vendidos = px.bar(tabela_produtos, x=tabela_produtos.index, y="Quantidade Vendida", title="Produtos Mais Vendidos")
grafico_produtos_devolvidos = px.bar(tabela_devolucao, x=tabela_devolucao.index, y="Quantidade Devolvida", title="Quantidade de Produtos Devolvidos") 

grafico_faturamento_loja.show()
grafico_produtos_devolvidos.show()
grafico_produtos_vendidos.show()