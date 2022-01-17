import pandas as pd

df = pd.read_excel('settings.xlsx', sheet_name='Sheet1')
print(df.head())

v1 = df[df['key'] == 'key1']['value'].values[0]
print(type(v1))
print(v1)

v2 = df[df['key'] == 'key2']['value'].values[0]
print(type(v2))
print(v2)

v3 = df[df['key'] == 'key3']['value'].values[0].split(',')
v3 = [int(x) for x in v3]
print(type(v3))
print(v3)

v4 = df[df['key'] == 'key4']['value'].values[0]
print(type(v4))
print(v4)
