#lendo arquivo csv(excel)
#biblioteca que le esse tipo de arquivo é o Pandas
import pandas as pd
data = pd.read_csv('datasets/kc_house_data.csv')



#CRIANDO uma nova variavel para colunas
data['aprendendo_data_science'] = "data_science"
data['aluguel'] = 900
#criando uma coluna e inserindo o formato da variavel em datetime
data['dia'] = pd.to_datetime('2023-03-08')

print(data.columns)
print(data[['id', 'aprendendo_data_science', 'aluguel', 'dia']].head(2))
print(data[['id', 'aprendendo_data_science', 'aluguel', 'dia']].dtypes)

#================================================================================================================================================================================================#

#DELETANDO variaveis
print(data.columns)             #antes

#detelatando a lista de variaveis selecionadas. (axis=1 -> é o sentido dado para uma coluna)(axis=0 -> é o sentido dado para uma linha)
data = data.drop(['aprendendo_data_science', 'aluguel', 'dia'], axis=1)

#tambem podemos criar uma variavel contendo a lista de variaveis que queremos deletar
#col = ['aprendendo_data_science', 'aluguel', 'dia']
#data = data.drop(col, axis=1)

print(data.columns)             #depois

#================================================================================================================================================================================================#

#SELECIONANDO variaveis
#selecionar pelo proprio nome da variavel
print(data['price'])
#ou selecionando por uma lista de variaveis 
#lista ['id', 'price', 'date' ]
print(data[['id', 'price', 'date' ]])

#selecionar pelo index de linha e colunas(requer o uso da função 'iloc')
#com essa funcao podemos selecionas as colunas apenas usado index, e tambem podendo pegar listas nas colunas e nas linhas somente pelo index
print(data.iloc[0:10, 0:3])
#para selecionarmos todas as linhas e colunas dess forma basta usar ':'. print(data.iloc[:, :])

#selecionar pelo index de linha e nome das colunas(requer o uso da função 'loc')
print(data.loc[0:10, ['price', 'id']])

#selecionar os indices por valores booleanos
#criar uma variavel que tenha uma lista com as colunas em valores booleanos(são 21 variaveis, portanto te que ter 21 valores booleanos)
#a seleçao deve ser com a funçao 'loc', pois é a unica que aceita valores que não são index
col= [True, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ]
print(data.loc[:, [True, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ]])




