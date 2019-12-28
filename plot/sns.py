import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def read_sns():
    df = pd.read_csv("input/sns.csv")
    return df


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


def missing():
    print('missing--------------start')
    df = pd.read_csv("input/input_df.csv") 
    hm = sns.heatmap(df.isnull(), cbar=False)
    plt.tight_layout()
    plt.savefig('missing.png', dpi=300)
    plt.show()


def main():
    df_sns = read_sns()
    sns_pairplot(df_sns)
    sns_heatmap(df_sns)

    missing()


if __name__ == '__main__':
    main()
