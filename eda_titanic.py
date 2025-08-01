import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega dados
df = pd.read_csv('dataset_titanic.csv')

# Informações gerais
print(df.info())
print(df.describe())

# Contagem de sobreviventes
sns.countplot(x='Survived', data=df)
plt.title('Sobreviventes (0 = Não, 1 = Sim)')
plt.show()

# Sobrevivência por sexo
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Taxa de Sobrevivência por Sexo')
plt.show()

# Sobrevivência por classe
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Taxa de Sobrevivência por Classe')
plt.show()