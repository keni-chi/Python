import pandas as pd
import numpy as np


dict1={
    'Row1': [True, True, False, False],
    'Row2': [True, False, True, False],
    'Row3': [False, False, True, True],
    'Row4': [True, True, False, False],
    'Row5': [1, 2, 3, 4],
    'Row6': [10, 20, 30, 40],
    'Row7': [100, 200, 300, 400],
}
df = pd.DataFrame(data=dict1)
print(df)

df['new1'] = df['Row1'] & df['Row2']
df['new2'] = df['Row1'] | df['Row2']
print(df)

# 新たな列名、元となる列、フィルタ列、置き換え対象列
df['new3'] = df['Row6'].where(df['Row1'] == True, df['Row5'])
print(df)

# Row7が250以上なら、Row7を採用。
# Row7が250未満かつRow6が15以上なら、Row6を採用
# どちらもあてはまらなければ、0埋め

# 250以上なら、元の列のまま
df['new4'] = df['Row7'].where(df['Row7'] >= 250, 0)
print(df['Row7'] >= 250)
print(df)

# 250以上または15以上ならば、元の列のまま
df['new4'] = df['new4'].where((df['Row7'] >= 250)|(df['Row6'] >= 15), df['Row6'])
print((df['Row7'] >= 250)|(df['Row6'] >= 15))
print(df)
