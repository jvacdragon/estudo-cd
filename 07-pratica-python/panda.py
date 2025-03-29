import pandas as pd

data = pd.read_csv('./dados/Credit.csv')

print(data)

print(data.describe())

print(data.shape)

print(data.columns)

print(data.head())

print(data.tail())

print(data[['duration', 'credit_history']])

print(data.loc[10:15])

print(data.loc[data['purpose'] == 'radio/tv'])

dataCreditMean = data['credit_amount'].mean()
print(dataCreditMean)
moreThanAverageCredit = data.loc[data['credit_amount'] > dataCreditMean]
print(moreThanAverageCredit)

print(moreThanAverageCredit.shape)

data.rename(columns={'duration': 'duracao', 'purpose': 'purpose'}, inplace=True)

#para excluir uma coluna, mas sem saber se ela existe, use errors='ignore' para que nao dê erro tentando excluir algo que nao existe
data.drop('duracao', axis=1, inplace=True, errors='ignore')

print(data.isnull().sum())

print(data.isna().sum())

#excluindon notAnumber
data.dropna()

data.fillna(0, inplace=True)


