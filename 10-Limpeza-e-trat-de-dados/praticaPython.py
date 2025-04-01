import pandas as pd
import seaborn as srn
import statistics as sts
import matplotlib.pyplot as plt

dataset = pd.read_csv('./dados/Churn.csv', sep=';')
print(dataset.head())
print(dataset.columns)
print(dataset.shape)

dataset.columns = ['id', 'score', 'UF', 'genero',  'idade', 'patrimonio', 'saldo', 'produtos', 'temCartCredito', 'ativo', 'salario', 'saiu']
print(dataset.columns)

dataset['ativo'] = dataset['ativo'].astype('boolean')
dataset['saiu'] = dataset['saiu'].astype('boolean')
dataset['temCartCredito'] = dataset['temCartCredito'].astype('boolean')
print(dataset.head())

print(dataset[dataset.duplicated(['id'], keep=False)])
dataset.drop_duplicates(subset='id', keep='first', inplace=True)
print(dataset[dataset.duplicated(['id'], keep=False)])

groupByEstado = dataset.groupby(['UF']).size()
print(groupByEstado)
dataset.loc[dataset['UF'] == 'RP', 'UF'] = 'PR'
groupByEstado = dataset.groupby(['UF']).size()
print(groupByEstado)

print(groupByEstado.idxmax())
dataset.loc[(dataset['UF'] != 'RS') & (dataset['UF'] != 'SC') & (dataset['UF'] != 'PR'), 'UF'] = groupByEstado.idxmax()
groupByEstado = dataset.groupby(['UF']).size()
print(groupByEstado)

""" groupByEstado.plot.bar()
plt.show() """

groupByGenero = dataset.groupby(['genero']).size()
print(groupByGenero)

dataset['genero'] = dataset['genero'].apply(lambda x: 'Feminino' if (str(x).startswith('F')) & (x != 'Feminino') else x)
dataset['genero'] = dataset['genero'].apply(lambda x: 'Masculino' if (str(x).startswith('M')) & (x != 'Masculino') else x)
groupByGenero = dataset.groupby(['genero']).size()
print(groupByGenero)
""" groupByGenero.plot.bar()
plt.show() """

print(dataset['idade'].describe())

dataset.loc[(dataset['idade'] <= 0) | (dataset['idade'] > 100), 'idade'] = dataset['idade'].mean().__trunc__()
print(dataset['idade'].describe())

groupedScore = dataset.groupby('score').size()
#no boxplot a linha do meio representa a mediana
""" srn.boxplot(dataset['score'])
plt.show()

srn.histplot(dataset['score'])
plt.show() """
print(dataset.isnull().sum())

medianSalario = sts.median(dataset['salario'])
dataset.fillna({'salario': medianSalario}, inplace=True)
print(dataset.isnull().sum())

print(dataset['genero'].describe().__getitem__('top'))
medianSalario = dataset['genero'].describe().__getitem__('top')
dataset.fillna({'genero': medianSalario}, inplace=True)
print(dataset.isna().sum())

#verificando outliers nos salarios com base no desvio padrão
desvioSalario = dataset['salario'].std()
print(dataset.loc[dataset['salario'] > 2*desvioSalario])

dataset.loc[dataset['salario'] > 2*desvioSalario, 'salario'] = dataset['salario'].median()
print(dataset.loc[dataset['salario'] > 2*desvioSalario])
