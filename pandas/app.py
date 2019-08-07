import pandas as pd
from decimal import Decimal
import decimal


def pd_main():
    print('pd--------------------start')
    df = pd.read_csv('input_df.csv')
    df.to_csv('output_df.csv')

    print('df0---')
    print('「有効データ数」「データ型」「メモリ使用量」などの総合的な情報を表示')
    print(df.info())
    print('縦横の形を調べる')
    print(df.shape)
    print('各カラムの有効データ数を表示')
    print(df.count())
    print('各カラムのデータ型を表示')
    print(df.dtypes)
    print('すべてのカラムに対して、欠損値の数を計算')
    print(len(df) - df.count())

    print('df1---')
    print('フィルタを行う')
    df1_1 =df[df['k'] == 'a']
    df1_2=df[df['k'] == 'b']
    df1_3=df[(df['k'] == 'a') | (df['k'] == 'b')]
    print(df1_1)
    print(df1_2)
    print(df1_3)
    
    print('df2---')
    print('マージ。dropna。')
    df2 = pd.merge(df1_1, df1_2, on='t', how='outer', suffixes=('_1', '_2'))
    print(df2)
    print(df2.dropna(how='any'))
    print(df2.dropna(thresh=3))     # 欠損値ではない要素の数がx個以上含まれている行が残る
    print(df2.dropna(thresh=4))
    print(df2.dropna(subset=['v_1']))
    
    # 複数マージ
    df2_1 = df
    df2_2 = df
    df2_3 = df
    df2_4 = df
    df2_a = pd.merge(df2_1, df2_2, on='t', how='outer', suffixes=('_1', '_2'))
    df2_b = pd.merge(df2_a, df2_3, on='t', how='outer', suffixes=('_2', '_3'))
    df2_c = pd.merge(df2_b, df2_4, on='t', how='outer', suffixes=('_3', '_4'))
    print(df2_c)

    print('df3---')
    print('int変換。')
    df3_1 = df.dropna(how='any')
    df3_2 = df3_1['v'].astype(int)
    print('df3_A')
    print(df3_2)
    df3_1['v_new'] = df3_1['v'].astype(int)
    print('df3_B')
    print(df3_1)

    print('df4---')
    print('null埋め。')
    df4 = df.fillna(df.median())
    print(df4)

    print('df5---')
    print('union。')
    df5 = pd.concat([df1_1, df1_1], ignore_index=True)
    print(df5)

    print('df6---')
    print('decimal')
    df6_1 = df.dropna(how='any')
    df6_2 = df6_1['ex1'].apply(lambda x: decimal.Decimal(x))
    v_raw = df6_2.mean()
    v = decimal.Decimal(str(v_raw)).quantize(Decimal('0.1'), rounding=decimal.ROUND_HALF_UP)
    print(v)

    print('df7---')
    print('append')
    df7 = df
    data = ["2016-04-13T04:00:00", "append", "1", 1]
    tmp_se = pd.Series(data, index=df7.columns)
    df7 = df7.append(tmp_se, ignore_index=True)
    print(df7)

    print('df8---')
    print('df新規')
    col = ['t', 'k', 'v', 'ex1']
    df8 = pd.DataFrame(columns=col)
    print(df8)

    print('df9---')
    print('演算')
    df9_1 = df
    df9_2 = df9_1.dropna(how='any')
    print(df9_2)
    print(df9_2['ex1'].sum())
    print(df9_2['ex1'].max())
    print(df9_2['ex1'].min())
    print(df9_2['ex1'].mean())
    print(len(df9_2))





    print('pd--------------------end')


def main():
    pd_main()

if __name__ == '__main__':
    print('main---start')
    main()
