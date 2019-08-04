import pandas as pd

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
    df1_1 =df[df['k'] == 'a']
    df1_2=df[df['k'] == 'b']
    print(df1_1)
    print(df1_2)
    
    df2 = pd.merge(df1_1, df1_2, on='t', how='outer', suffixes=('_1', '_2'))
    print('df2---')
    print(df2)
    print(df2.dropna(how='any'))
    print(df2.dropna(thresh=3))     # 欠損値ではない要素の数がx個以上含まれている行が残る
    print(df2.dropna(thresh=4))
    print(df2.dropna(subset=['v_1']))

    print('df3---')
    df3_1 = df.dropna(how='any')
    df3_2 = df3_1['v'].astype(int)
    print('df3_A')
    print(df3_2)
    df3_1['v_new'] = df3_1['v'].astype(int)
    print('df3_B')
    print(df3_1)

    print('df4---')
    df4 = df.fillna(df.median())
    print(df4)

    print('pd--------------------end')


def main():
    pd_main()

if __name__ == '__main__':
    print('main---start')
    main()
