import pandas as pd
import plotly.express as px

df = pd.read_csv('vendas.csv')

df_data = df.groupby('Data')['Receita'].sum().reset_index()

fig = px.line(df_data, x='Data', y='Receita', title='Receita ao Longo do Tempo')
fig.show()