# -*- coding: utf-8 -*-
from numba import jit
from numpy import arange
import pandas as pd
import numpy as np
import time


a = arange(100000000).reshape(10000, 10000)
# a = arange(1000000).reshape(1000, 1000)
# a = arange(9).reshape(3, 3)
print(type(a))
# ndarrayのデータ型を変換
a = a.astype(np.int64)
print(type(a))
# print(a)


def sum2d(arr):
    M, N = arr.shape
    result = 0.0
    for i in range(M):
        for j in range(N):
            result += arr[i, j]
    return result


@jit
def sum2d_numba(arr):
    M, N = arr.shape
    result = 0.0
    for i in range(M):
        for j in range(N):
            result += arr[i, j]
    return result


def run_for_loop():
    print('run_for_loop---------start')
    start = time.time()
    print(sum2d(a))
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")


def run_numba():
    print('run_numba---------start')
    start = time.time()
    print(sum2d_numba(a))
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")


def run_pandas():
    print('run_pandas---------start')
    df = pd.DataFrame(a)
    start = time.time()
    print(df.sum().sum())
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")


def run_numpy():
    print('run_numpy---------start')
    start = time.time()
    print(a.sum())
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")


def main():
    run_for_loop()
    run_numba()
    run_pandas()
    run_numpy()


if __name__ == '__main__':
    main()


# 実行例
# <class 'numpy.ndarray'>
# <class 'numpy.ndarray'>
# run_for_loop---------start
# 4999999950000000.0
# elapsed_time:31.523563861846924[sec]
# run_numba---------start
# 4999999950000000.0
# elapsed_time:0.5785479545593262[sec]
# run_pandas---------start
# 4999999950000000
# elapsed_time:0.4902811050415039[sec]
# run_numpy---------start
# 4999999950000000
# elapsed_time:0.07905387878417969[sec]
