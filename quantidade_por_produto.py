import pandas as pd
import plotly.express as px

df = pd.read_csv('vendas.csv')

df_produto = df.groupby('Produto')['Quantidade'].sum().reset_index()

fig = px.pie(df_produto, values='Quantidade', names='Produto', title='Quantidade Vendida por Produto')
fig.show()