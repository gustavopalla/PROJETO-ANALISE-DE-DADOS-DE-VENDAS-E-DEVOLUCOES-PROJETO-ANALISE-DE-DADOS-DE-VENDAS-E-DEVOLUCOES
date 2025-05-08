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

tabela_total['Faturamento'] =  tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_total['Custo Unitario'] = tabela_total['Preco Unitario'] * 0.6
tabela_total['Lucro'] = tabela_total['Faturamento'] - (tabela_total['Quantidade Vendida'] * tabela_total['Custo Unitario'])

#Produtos mais vendidos
tabela_produtos = tabela_total.groupby('Produto').sum(numeric_only=True)
tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)

print("\n Produto mais vendido: ")
print(tabela_produtos)

#Faturamento por Cidade
tabela_faturamento = tabela_total.groupby('Produto').sum(numeric_only=True)
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)

print("\n Faturamento")
print(tabela_faturamento)

#Lucro
tabela_lucro = tabela_total.groupby('Produto').sum(numeric_only=True)
tabela_lucro = tabela_lucro[['Lucro']].sort_values(by='Lucro', ascending=False)

print("\n Lucro")
print(tabela_lucro)

#Faturamento Por Loja/Cidade
tabela_loja = tabela_total.groupby('Loja').sum(numeric_only=True)
tabela_loja = tabela_loja[['Faturamento']]

print("\n Faturamento por loja")
print(tabela_loja)

#Quantidade de Devoluções
tabela_devolucao = tabela_total.groupby('Produto').sum(numeric_only=True)
tabela_devolucao = tabela_devolucao[['Quantidade Devolvida']].sort_values(by='Quantidade Devolvida', ascending=False)

print('\n Quantidade Devolvida')
print(tabela_devolucao)

#Faturamento Por Mês/Ano
tabela_total['Data'] = pd.to_datetime(tabela_total['Data'])
tabela_faturamento_mensal = tabela_total.groupby(pd.Grouper(key='Data', freq='M')).sum(numeric_only=True)

print('\n Agrupamento Por Mês')
print(tabela_faturamento_mensal)

#Quantidade Devolvida Por Mês
tabela_total['Data'] = pd.to_datetime(tabela_total['Data'])
tabela_devolvidos_mes = tabela_total.groupby(pd.Grouper(key='Data', freq='M')).sum(numeric_only=True)

print('\n Devolvidos Por Mês')
print(tabela_devolvidos_mes)

#Criação dos Gráficos
grafico_faturamento_loja = px.bar(tabela_loja, x=tabela_loja.index, y="Faturamento", title="Faturamento por loja") 
grafico_produtos_vendidos = px.bar(tabela_produtos, x=tabela_produtos.index, y="Quantidade Vendida", title="Produtos Mais Vendidos")
grafico_produtos_devolvidos = px.bar(tabela_devolucao, x=tabela_devolucao.index, y="Quantidade Devolvida", title="Quantidade de Produtos Devolvidos") 
grafico_lucro_empresa = px.bar(tabela_lucro, x=tabela_lucro.index, y='Lucro', title="Lucro")
grafico_agrupamento_data = px.bar(tabela_faturamento_mensal, x=tabela_faturamento_mensal.index, y='Faturamento', title="Faturamento Mensal")
grafico_devolvidos_mes = px.bar(tabela_devolvidos_mes, x=tabela_devolvidos_mes.index, y='Quantidade Devolvida', title='Quantidade Devolvida Mensal')

#Print nos Gráficos
grafico_faturamento_loja.show()
grafico_produtos_devolvidos.show()
grafico_produtos_vendidos.show()
grafico_lucro_empresa.show()
grafico_agrupamento_data.show()
grafico_devolvidos_mes.show()
