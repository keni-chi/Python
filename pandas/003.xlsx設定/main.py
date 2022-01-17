import pandas as pd


df = pd.read_excel('settings.xlsx', sheet_name='Sheet1')
print(df.head())
