from numpy import int64
#lendo arquivo csv(excel)
#biblioteca que le esse tipo de arquivo é o Pandas
import pandas as pd
data = pd.read_csv('datasets/kc_house_data.csv')


print(data.dtypes)
print(data.head(2))

#converter os dados da tabela date para o formato data (string -> datetime)
data['date'] = pd.to_datetime(data['date'])

print(data.dtypes)
print(data.head(2))

#================================================================================================================================================================================================#

#Converter de inteiro(int)->Float(float)

print(data[['id','bedrooms']].head(2))             #antes
print(data[['id','bedrooms']].dtypes)

#convertendo o dado para FLOAT
data['bedrooms'] = data['bedrooms'].astype(float)

print(data[['id','bedrooms']].head(2))             #depois
print(data[['id','bedrooms']].dtypes)

#================================================================================================================================================================================================#

#Converter de inteiro(int)->String(object)
print(data[['id','bedrooms']].head(2))             #antes
print(data[['id','bedrooms']].dtypes)

#voltando o valor anterior para INT
#tomar cuidado na hora de mudar o tipo de dado, todos devem estar com o mesmo valor em bit(temos que especificar que queremos int64 e trazer a biblioteca)
data['bedrooms'] = data['bedrooms'].astype(int64)
#convertendo para STRING
data['bedrooms'] = data['bedrooms'].astype(str)

print(data[['id','bedrooms']].head(2))             #depois
print(data[['id','bedrooms']].dtypes)

#================================================================================================================================================================================================#

#Converter de String(object)->Inteiro(int)

print(data[['id','bedrooms']].head(2))             #antes
print(data[['id','bedrooms']].dtypes)

#retornando o dado para INT
data['bedrooms'] = data['bedrooms'].astype(int)

print(data[['id','bedrooms']].head(2))             #depois
print(data[['id','bedrooms']].dtypes)

#================================================================================================================================================================================================#
