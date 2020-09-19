import pandas as pd
from decimal import Decimal
import decimal
import datetime as dt


def pd_main():
    print('pd--------------------start')
    df = pd.read_csv('input_df.csv')
    print(df.head())
    df1 = df[['k', 't', 'v']]
    print(df1.head())
    del df1['v']
    print(df1.head())


def main():
    pd_main()


if __name__ == '__main__':
    print('main---start')
    main()
