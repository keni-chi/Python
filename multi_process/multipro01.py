#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Pool
import multiprocessing
from collections import Counter
import time


# ここを並列処理する
def func(n, argument1, argument2):
    # 2倍して5を足す処理
    return n * argument1 + argument2

def wrapper(args):
    # argsは(i, 2, 5)となっている
    return func(*args)

def multi_process(sampleList):
    # プロセス数:8(8個のcpuで並列処理)
    p = Pool(8)
    output = p.map(wrapper, sampleList)
    # プロセスの終了
    p.close()
    return output

if __name__ == "__main__":
    # 100回の処理を並列処理で行う
    num = 100

    # (i, 2, 5)が引数になる
    starttime = time.time()
    sampleList = [(i, 2, 5) for i in range(num)]
    print(sampleList)
    endtime = time.time()
    interval = starttime - endtime
    print(str(interval) + "sampleList秒")

    # sampleListの要素を2倍して5を足す
    starttime = time.time()
    output = multi_process(sampleList)
    print(output)
    endtime = time.time()
    interval = starttime - endtime
    print(str(interval) + "multi_process秒")

    #コア数
    Data1 = multiprocessing.cpu_count()
    print(Data1)
