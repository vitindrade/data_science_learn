import pandas as pd
import plotly.express as px
import numpy as np

data = pd.read_csv('datasets/kc_house_data.csv')

print(data.columns)
print(data.dtypes)

print('Criar uma nova coluna house_age. Acima de 2014-01-01 - new_house, se abaixo de 2014-01-01 - old_house')

#convertendo os dados de string para datetime e especificando o formato para ser comparado corretamente
data['date'] = pd.to_datetime(data['date'], format= '%Y-%m-%d')
#criando uma nova coluna 'house_age' selecionando a coluna 'date' para aplicar a funcao apply
# funcao apply - usado para ir de linha a linha da coluna selecionada atribuindo valores com uma condicao
# vai linha a linha seguindo o criterio de: adicionar 'new_house' (na condicao verdadeira) se x(no caso a data) for maior que 2014-01-01 indicando corretamente o formato de data, caso contrario adicionar 'old_house '
data['house_age'] = data['date'].apply( lambda x: 'new_house' if x > pd.to_datetime('2014-01-01', format= '%Y-%m-%d') else 'old_house' )

print(data.loc[:, ['id', 'date', 'house_age']].sort_values('date', ascending=True))

#================================================================================================================================================================================================#

print('Criar uma nova coluna dormitory. Bedrooms igual a 1 - studio, igual a 2 - apartament e maior que 2 - house ')

#crio uma nova coluna dormitory
data['dormitory'] = data['bedrooms'].apply( lambda x: 'studio' if x ==1 else
                                                      'apartament' if x ==2 else
                                                      'house' if x > 2 else 'NA')

print(data.loc[:, ['bedrooms', 'dormitory']].head())

#================================================================================================================================================================================================#

print('Criar uma nova coluna condition_type. Condition menor ou igual a 2 - bad, entre 3 e 4 - regular e igual a 5 - good ')

data['condition_type'] = data['condition'].apply( lambda x: 'bad' if x <=2 else
                                                            'regular' if (x==3)|(x==4) else
                                                            'good' if x == 5 else 'NA')

print(data.loc[:, ['condition', 'condition_type']])

#================================================================================================================================================================================================#

print('Modifique o Tipo da coluna condition para string')

data['condition'] = data['condition'].astype(str)

print(data['condition'].dtypes)

#================================================================================================================================================================================================#

print('Deletar as colunas sqft_living15 e sqft_lot15')

data = data.drop(['sqft_living15', 'sqft_lot15'], axis=1)

print(data.columns)

#================================================================================================================================================================================================#

print('Modifique o Tipo da coluna yr_built e yr_renovated para datetime')

data['yr_built'] = pd.to_datetime(data['yr_built'], format = '%Y')

#nesta situacao o yr_renovated tem valores em 0, portanto vamos converter eles em dataas fixas como 1970 para podermos modificar de tring para datatime

data['yr_renovated'] = data['yr_renovated'].apply(lambda x: pd.to_datetime('1900-01-01', format = '%Y-%m-%d') if x == 0 else pd.to_datetime(x, format='%Y') )


print(data[['yr_built', 'yr_renovated']].dtypes)

#================================================================================================================================================================================================#

print('Qual a data mais antiga de construcao de imovel?')

data['yr_built'] = pd.to_datetime(data['yr_built'], format = '%Y-%m-%d')

const = data[['yr_built']].sort_values('yr_built', ascending=True).reset_index(drop=True)

print('     R: a data mais antiga de construcao é:', const.loc[0, 'yr_built'])

#================================================================================================================================================================================================#

print('Qual a data mais antiga de renovacao de imovel?')

data['yr_renovated'] = pd.to_datetime(data['yr_renovated'], format = '%Y-%m-%d')

#procuro a data mais antiga descosiderando a data que tinha dado 0 na formatacao da tabela(ou seja, acima de 1900)
ren = data.loc[data['yr_renovated'] > pd.to_datetime('1900-01-01', format = '%Y-%m-%d'), 'yr_renovated']

print('     R: a data mais antiga de renovacao é:', ren.min())

#================================================================================================================================================================================================#

print('Quantos imoveis tem 2 andares?')

andares_2 = data.loc[data['floors'] == 2]

print('     R: a quantidade de imoveis com 2 andares é:', len(andares_2))

#================================================================================================================================================================================================#

print('Quantos imoveis tem a condicao regular?')

reg = data.loc[data['condition_type'] == 'regular']

print('     R: a quantidade de imoveis na condicao regular é:', len(reg))

#================================================================================================================================================================================================#

print('Quantos imoveis tem a condicao bad e vista para o mar?')

bad_mar = data.loc[(data['condition_type'] == 'bad') & (data['waterfront'] == True)]

print('     R: a quantidade de imoveis que tem a condicao bad e vista para o mar é:', len(bad_mar))

#================================================================================================================================================================================================#

print('Quantos imoveis tem a condicao good e sao new_house?')

g_new = data.loc[(data['condition_type'] == 'good') & (data['house_age'] == 'new_house')]

print('     R: a quantidade de imoveis tem a condicao good e sao new_house é:', len(g_new) )

#================================================================================================================================================================================================#

print('Qual o valor do imovel mais caro do tipo studio?')


high_studio = data.loc[data['dormitory'] == 'studio'].sort_values('price', ascending=False).reset_index(drop=True)

print('     R: o valor mais caro de imovel studio é:', high_studio.loc[0, 'price'] )

#================================================================================================================================================================================================#

print('Quantos imoveis do tipo apartament foram renovados em 2015?')

data['yr_renovated'] = pd.to_datetime(data['yr_renovated'])

apart_2015 = data.loc[(data['yr_renovated'] == pd.to_datetime('2015-01-01')) & (data['dormitory'] == 'apartament' )]

print('     R: a quantidade de imoveis do tipo apartament foram renovados em 2015 é:', len(apart_2015) )

#================================================================================================================================================================================================#

print('Quantos imoveis new_house foram renovados em 2014?')

new_2014 = data.loc[(data['house_age'] == 'new_house')&((data['yr_renovated'] >= '2014-01-01') & (data['yr_renovated'] <= '2014-12-30'))]

print('     R: a quantidade de imoveis new_house que foram renovados em 2014 é:', len(new_2014) )

#================================================================================================================================================================================================#

print('Selecione as colunas id, date, price, floors e zipcode pelo metodo: nome de colunas, apenas indices, indices e nomes e boolenaos')

print(data[['id', 'date', 'price', 'floors', 'zipcode']])

print(data.iloc[:, [0, 1, 2, 7 , 16]])

print(data.loc[:, ['id', 'date', 'price', 'floors', 'zipcode']])

print(data.loc[:,[True, True, True, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False ]])

#================================================================================================================================================================================================#

print('Salve um arquivo .csv do exercicio 10 ao 17')

exerc = data.loc[:, ['condition_type', 'dormitory', 'house_age']]

exerc.to_csv('datasets/atividade_02.csv', index=False)

#================================================================================================================================================================================================#

#importando a biblioteca que contem a funcao que apresenta o mapa
import plotly.express as px

#criando uma variavel contendo os dados que vamos usar
data_mapa = data[['id', 'lat', 'long', 'price', 'date']]

#chamando a funcao que dentro da biblioteca que ira conter a variavel e os dados que ira precisar para criar o mapa
mapa = px.scatter_mapbox(data_mapa, lat = 'lat', lon = 'long',
#hover_name - variavel que ao passar o mouse por cima ira apresentar o mapa
                    hover_name = 'id',
#hover_data - variavel que sera apresentada junto com o mapa
                    hover_data = ['price'],
#color_discrete_sequence - variavel que representa a cor do ponto no mapa
                    color_discrete_sequence = ['#00CC96'],
#zoom - como o proprio nome diz, é o zoom que o mapa vai apresentar
                    zoom = 3,
#height - o tamanho que o mapa vai ter
                    height = 300)

#usando uma funcao para escolher o layout do mapa
mapa.update_layout( mapbox_style = 'open-street-map')
#usando uma funcao para definir a estrutura do layout do mapa
mapa.update_layout( height = 600, margin ={'r':0, 't':0, 'l':0, 'b':0})
#ira apresentar o mapa no navegador
# mapa.show()



