import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import pandas as pd
import numpy as np
from datetime import datetime


def read_line():
    line_df= pd.read_csv("input/line.csv")
    line_np = line_df.values
    x = line_np[:,0]
    y = line_np[:,1]
    return x, y


def read_scatter():
    scatter_df = pd.read_csv("input/scatter.csv")
    df_x = scatter_df['x']
    df_y = scatter_df['y']
    return df_x, df_y


def read_datetime():
    df = pd.read_csv("input/datetime.csv")
    df['timestamp'] = df['timestamp'].apply(lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ'))
    return df


def read_sns():
    df = pd.read_csv("input/sns.csv")
    return df


def line1(x, y):
    plt.plot(x, y, label="data1")
    plt.legend()
    plt.show()


def line2(x, y):
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="data1", marker='o', linestyle='--', linewidth=3)
    plt.axvline(2, label="a", color="red", linestyle="--") 
    plt.axhline(20, label="b", color="green", linestyle="--") 
    plt.legend()
    plt.show()


def scatter1(x, y):
    plt.scatter(x[0:2], y[0:2], color='red', marker='o', label='data1')
    plt.scatter(x[2:4], y[2:4], color='blue', marker='x', label='data2')
    plt.grid()
    plt.tight_layout() # グラフの位置やサイズが自動で調整
    plt.xlabel('xlabel')
    plt.ylabel('ylabel')
    plt.legend(loc='upper left')
    plt.show()


def scatter2(x, y):
    colors = ['r', 'b', 'g']
    markers = ['s', 'x', 'o']

    for l, c, m in zip(np.unique(y), colors, markers):
        plt.scatter(x[y==l], y[y==l], c=c, label=l, marker=m)

    plt.xlabel('xlabel')
    plt.ylabel('ylabel')
    plt.legend(loc='lower left')
    plt.tight_layout()
    plt.show()


def bar1(x, y):
    plt.title('bar titile')
    plt.bar(x, y, align='center')
    plt.xticks(x, y, rotation=90)
    # plt.xlim([0.5, x.shape[0]+0.5]) # x軸の範囲を指定したい時
    plt.tight_layout()
    plt.show()


def multi_line(x, y):
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(7, 3))
    ax[0].plot(x, y, label="data1")
    ax[0].legend()
    ax[1].plot(x, y, label="data2")
    ax[1].legend()
    ax[0].set_xlabel('xlabel')
    ax[0].set_ylabel('ylabel')
    ax[1].set_xlabel('xlabel')
    ax[1].set_ylabel('ylabel')
    plt.tight_layout()
    plt.show()


def datetime_line(df):
    ax = plt.subplot()
    # 15分間隔で目盛り
    ax.xaxis.set_major_locator(mdates.MinuteLocator([0,15,30,45]))
    # 時間のフォーマット
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %H:%M"))
    df.plot(x='timestamp', y='value', ax=ax)
    plt.show()


def sns_pairplot(df):
    df.head()
    cols = ['x1', 'x2', 'x3', 'x4', 'x5']
    sns.pairplot(df[cols], height=2.5)
    plt.tight_layout()
    plt.savefig('sns_pairplot.png', dpi=300)
    plt.show()


def sns_heatmap(df):
    cols1 = df.columns
    cols2 = ['y1', 'y2', 'y3', 'y4', 'y5']
    hm = sns.heatmap(df,
                     cbar=True,
                     annot=True,
                     square=True,
                     fmt='.2f',
                     annot_kws={'size': 15},
                     yticklabels=cols2,
                     xticklabels=cols1)
    plt.tight_layout()
    plt.savefig('sns_heatmap.png', dpi=300)
    plt.show()


def main():
    # データ読み込み
    x, y = read_line()
    df_x, df_y = read_scatter()
    df_dt = read_datetime()
    df_sns = read_sns()

    # グラフ作成
    # line1(x, y)
    # line2(x, y)
    # multi_line(x, y)
    # scatter1(x, y)
    # scatter2(df_x, df_y)
    # bar1(x, y)
    # datetime_line(df_dt)
    sns_pairplot(df_sns)
    sns_heatmap(df_sns)


if __name__ == '__main__':
    main()
