import matplotlib.pyplot as plt
import pandas as pd


def line_read():
    line_df= pd.read_csv("input/line.csv")
    line_np = line_df.values
    x = line_np[:,0]
    y = line_np[:,1]
    return x, y


def line1(x, y):
    # プロット
    plt.plot(x, y, label="data1")
    # 凡例の表示
    plt.legend()
    # プロット表示(設定の反映)
    plt.show()


def line2(x, y):
    fig = plt.figure(figsize=(12, 8))
    # Figure内にAxesを追加()
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="data1")
    plt.legend()
    plt.show()


def scatter1(x, y):
    print(x[0:2])
    print(x[2:4])
    plt.scatter(x[0:2], y[0:2],
                color='red', marker='o', label='a')
    plt.scatter(x[2:4], y[2:4],
                color='blue', marker='x', label='b')
    plt.xlabel('xlabel')
    plt.ylabel('ylabel')
    plt.legend(loc='upper left')
    plt.savefig('scatter1.png', dpi=300)
    plt.show()


def main():
    # x, y = line_read()
    # line1(x, y)
    # line2(x, y)

    x, y = line_read()
    scatter1(x, y)




if __name__ == '__main__':
    main()
