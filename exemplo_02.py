import pandas as pd
data = pd.read_csv('datasets/kc_house_data.csv')

print(data.columns)

print('- Qual a data do imóvel mais antigo?')
#converter a coluna 'date' para valores 'datetime'
data['date'] = pd.to_datetime(data['date'])
#organizar a tabela de forma ascendente e pegar a maior data, resetar o index(para que seja feita a nova organização) e mostrar o primeiro valor
antigo = data[['id', 'date']].sort_values('date', ascending=True).reset_index(drop=True)
print('     R: a data imovel mais antigo é:', antigo.loc[0, 'date'])

#================================================================================================================================================================================================#

print('- Quantos imóveis possuem o numero máximo de andares?')
#ordenar a lista por ordem decrescente e resetendo o index
max_andares = data[['id', 'floors']].sort_values('floors', ascending= False).reset_index(drop=True)
#pegando o maior numero de andares na tabela 
max = max_andares.loc[0, 'floors']
#mostrando quantos andares tem essa quantidade de andares
print('     R: o imovel com mais andares é:', len(data.loc[data['floors'] == max]))

#================================================================================================================================================================================================#

print('- Criar uma classificação para imóveis, separando em baixo e alto padrão de acordo com o preço')

#criar uma nova coluna 'level' onde vai carregar a informacao standard
data['level'] = 'standard'
#dando filtrando valores acima de 540000 como 'high_level'
data.loc[data['price'] > 540000, 'level'] = 'high_standard'
#dando filtrando valores abaixo de 540000 como 'low_level'
data.loc[data['price'] < 540000, 'level'] = 'low_standard'

#================================================================================================================================================================================================#

print('- Criar um relatório ordenado pelo preço contendo as informações: id, quartos, data, tamanho total,preco, level')
#criando uma variavel que contem a tabela com os valores desejados e ordenados pelo preco
relatorio = data.loc[:, ['id', 'bedrooms', 'date', 'sqft_living', 'price', 'level']].sort_values('price', ascending=False)
print(relatorio)
#Criando um arquivo contendo somente a tabela com as variaveis que selecionamos, deixando o 'index' ordenado pelo preco
relatorio.to_csv('datasets/relatorio_aula02.csv', index= False)

#================================================================================================================================================================================================#

print('- Criar um Mapa indicando onde estão as casas')

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
                    color_discrete_sequence = ['fuchsia'],
#zoom - como o proprio nome diz, é o zoom que o mapa vai apresentar
                    zoom = 3,
#height - o tamanho que o mapa vai ter
                    height = 300)

#usando uma funcao para escolher o layout do mapa
mapa.update_layout( mapbox_style = 'open-street-map')
#usando uma funcao para definir a estrutura do layout do mapa
mapa.update_layout( height = 600, margin ={'r':0, 't':0, 'l':0, 'b':0})
#ira apresentar o mapa no navegador
mapa.show()
mapa.write_html('datasets/mapa_ex02.html')

