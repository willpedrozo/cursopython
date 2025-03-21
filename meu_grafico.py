import pandas as pd
import plotly.express as px

#NÃO PODE SALVAR O NOME DO ARQUIVO COM O NOME DA EXTENSÃO

df = pd.read_csv('C:/Users/noturno/Desktop/pythonbasico/Recomeço/base.csv')
print(df.head())

#organizar os dados
df_organizado = pd.melt(df, id_vars = ['Vendas'], value_vars = ['TV', 'Radio', 'Jornal'], var_name = 'Media', value_name = 'Valor')
print(df_organizado.head())

#criar grafico de pizza interativo
fig = px.pie(df_organizado, values ='Vendas', names = 'Media', title = 'Distribuição de vendas', hole = 0.3)

fig.show()






