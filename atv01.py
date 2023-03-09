#lendo arquivo csv(excel)
#biblioteca que le esse tipo de arquivo é o Pandas
import pandas as pd
data = pd.read_csv('datasets/kc_house_data.csv')



print("- Quantas casas estão disponiveis para compra?")
#seleciona a coluna id e faz a contagem de quantos valores há
linha = len(data['id'].unique())
print("     R: estão disponiveis",linha,"casas")

#================================================================================================================================================================================================#

print("- Quantos atributos as casas possuem?")
#conta a quantidade de colunas 
#tenho que desconsiderar as colunas id e date 
coluna = len(data.drop(['id', 'date'], axis=1).columns)
print("     R: As casas possuem", coluna,"atributos")

#================================================================================================================================================================================================#

print("- Quais são os atributos das casas?")
print("     R: os atributos são:", list(data.columns))

#================================================================================================================================================================================================#

print("- Qual casa mais cara?")
#organizo o valor do maior pro menor pelo preço
#passo para uma variavel com um novo index(renumerando as linhas para que seja uma nova tebela)
maior = data[['id', 'price']].sort_values('price', ascending=False).reset_index(drop=True)
print("     R: a casa mais cara é o id:", maior['id'][0])

#================================================================================================================================================================================================#

print("- Qual casa com maior numero de quartos?")
#organizo o valor do maior pro menor pelo numero de quartos 
#passo para uma variavel com um novo index(renumerando as linhas para que seja uma nova tebela)
quartos = data[['id', 'bedrooms']].sort_values('bedrooms', ascending=False).reset_index(drop=True)
print("     R: o quarto com maior numero de quartos é:", quartos['bedrooms'][0])

#================================================================================================================================================================================================#

print("- Qual a soma total dos conjuntos de quartos?")
#fazer a somatorio da quantidade de todos os quartos 
soma_quartos = data['bedrooms'].sum()
print("     R: a soma total de quartos é:", soma_quartos)

#================================================================================================================================================================================================#

print("- Quantas casas possuem 2 banheiros?")
#precisamos filtrar para a quantidade de casas com 2 banheiros e contar quantas casas(linhas)
banheiros = len(data.loc[data['bathrooms']==2, ['id', 'bathrooms']])
print("     R: o total de casas com 2 banheiros é:", banheiros)

#================================================================================================================================================================================================#

print("- Qual o preço medio das casas?")
#calcular a media de precos da casa
medio = data['price'].mean()
print("     R: o preço medio das casas é:", medio)

#================================================================================================================================================================================================#

print("- Qual o preço medio das casas de 3 quartos?")
#filtrar para casas com apenas 2 banheiros e fazer a media desses valores
medio_quartos = data.loc[data['bedrooms']==3, ['price', 'bedrooms']]
print("     R: o preço medio das casas com quartos é:", medio_quartos['price'].mean())

#================================================================================================================================================================================================#

print("- Qual o preço minimo das casas com 2 banheiros?")
#filtro para casas com 2 banheiros e pego a casa de menor valor
minimo_quartos = data.loc[data['bathrooms']==2, 'price'].min()
print("     R: o preço minimo de com 2 banheiros é:", minimo_quartos)

#================================================================================================================================================================================================#

print("- Quantas casas possuem mais de 300 metros quadrados?")
# temos que converter o valor de pés em metros e apos isso ver qual a quantidade de casas com essa medida
mt_quadrados = len(data.loc[data['sqft_living'] > 3333])
print("     R: o numero de casas com mais de 300(3333,33 pés) metros quadrados é:", mt_quadrados)

#================================================================================================================================================================================================#

print("- Quantas casas tem mais de 2 andares?")
#filtrar pela quantidade de casa com mais de dois andares e contar quantaas casas tem
andares = len(data.loc[data['floors'] > 2])
print("     R: o numeros de casa com mais de 2 andares é:", andares)

#================================================================================================================================================================================================#

print("- Quantas casas tem vista para o mar?")
#filtrar a quantidade de casas com vista para o mar e mostrar a quantidade com essa informação
mar = len(data.loc[data['waterfront'] ==1])
print("     R: o numeros de casa com vista para o mar é:", mar)

#================================================================================================================================================================================================#

print("- Das casas com vista para o mar quantas tem 3 quartos?")
#filtrar a quantidade de casas com vista para o mar que TAMBEM tenham 3 quartos
mar_quartos = len(data.loc[(data['waterfront'] ==1) & (data["bedrooms"] == 3)])
print("     R: o numeros de casa com vista para o mar com tres quartos é:", mar_quartos)

#================================================================================================================================================================================================#

print("- Das casas com 300 metros quadrados, quantas tem 2 banheiros?")
#filtrar a quantidade de casas com 300 metros quadrados e TAMBEM com 2 banheiros
mt_quadrados_quartos = len(data.loc[(data['sqft_living'] > 3333) & (data['bathrooms'] == 2)])
print("     R: o numero de casas com mais de 300(3333,33 pés) metros quadrados e com 2 banheiros é:", mt_quadrados_quartos)