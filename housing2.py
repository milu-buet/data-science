# 5 points, 2 for effort. Maximum attempts: 1.


import pandas
df = pandas.read_csv('data/cali_housing.csv')

a = df.groupby('ocean_proximity')['ocean_proximity'].count().count()
a = len(df.ocean_proximity.unique())
#a = df.ocean_proximity.value_counts().count()

print(a)