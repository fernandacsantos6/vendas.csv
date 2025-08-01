import pandas as pd
import plotly.express as px

df = pd.read_csv('vendas.csv')

df_regiao = df.groupby('Região')['Receita'].sum().reset_index()

fig = px.bar(df_regiao, x='Região', y='Receita', title='Receita por Região')
fig.show()