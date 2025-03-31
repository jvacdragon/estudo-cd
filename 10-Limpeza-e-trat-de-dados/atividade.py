import pandas as pd
import statistics as sts

df = pd.read_csv('./dados/tempo.csv', sep=';')
print(df.shape)

print(df.head())

print(df['Aparencia'].isnull().sum())

dfAparencia = df.groupby('Aparencia').size()
print(dfAparencia)

#trocando valores invalidos de aparencia para o valor valido que mais foi utilizado no campo ja
df.loc[~df['Aparencia'].isin(['chuva', 'nublado', 'sol']), 'Vento'] = dfAparencia.idxmax()
print(df.groupby('Aparencia').size())

print(df['Temperatura'].isnull().sum())
print(df['Temperatura'].describe())

print(df['Temperatura'])
df.loc[(df['Temperatura'] > 130) | (df['Temperatura'] < -130), 'Temperatura'] = df['Temperatura'].median().__trunc__()
df['Temperatura'].describe()
print(df['Temperatura'])

print(df['Umidade'].isnull().sum()) #tem um valor NaN
print(df['Umidade'].describe())

df.loc[(df['Umidade']>100) | (df['Umidade'] < 0), 'Umidade'] = sts.median(df['Umidade'])

print(df['Umidade'].describe())

df.fillna({'Umidade': sts.median(df['Umidade'])}, inplace=True)
print(df['Umidade'].isnull().sum())

