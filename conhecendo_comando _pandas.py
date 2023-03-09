#lendo arquivo csv(excel)
#biblioteca que le esse tipo de arquivo é o Pandas
import pandas as pd
data = pd.read_csv('datasets/kc_house_data.csv')
#mostrar as primeiras linhas do conjunto de dados
print(data.head())
#mostrar linhas e colunas do conjunto de dados
print(data.shape)
#mostrar na tela o nome das colunas
print( data.columns)
#mostrar conjunto de dados de uma coluna ordenado price
print(data.sort_values('price'))
#mostrar conjunto de dados das colunas ordenado price e id
print(data[['id', 'price']].sort_values('price'))
#mostrar conjunto de dados das colunas ordenado de forma crescente price e id
print(data[['id', 'price']].sort_values('price', ascending=False))
#mostrar a quantidade de colunas
print(len(data.axes[1]))
#mostrar a quantidade de linhas
print(len(data.axes[0]))