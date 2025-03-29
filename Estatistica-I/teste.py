from matplotlib.pylab import sample
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./dados/iris.csv')

print(df.head().to_markdown())

print(df.columns)

mean = np.mean(df["sepal width"])
std = np.std(df['sepal width'])

print(mean.round(2))
print(std.round(2))

print(df[["sepal width", "class"]].head().to_markdown())

""" plt.boxplot(df['sepal width'])
sns.boxplot(data=df["sepal width"], color="red") 
plt.show()"""

""" plt.hist(df["sepal width"])
plt.show()

print(df.columns)
plt.hist(df["sepal length"])
plt.show() """

""" x = sample(10)
print(np.mean(x))
plt.hist(x)
plt.show()

y = sample(100)
print(np.mean(y))
plt.hist(y)
plt.show()

z = sample(1000)
print(np.mean(z))
plt.hist(z)
plt.show()

z = sample(10000)
print(np.mean(z))
plt.hist(z)

plt.show() """