# -*- coding: utf-8 -*-
from joblib import Parallel, delayed
from time import time

def process(n):
    return sum([i*n for i in range(100000)])


print('並列なし--------------start')
start = time()
total = 0
for i in range(10000):
    total += process(i)
print(total)
print('{}秒かかりました'.format(time() - start))
print('並列なし--------------end')


print('並列あり--------------start')
start = time()
r = Parallel(n_jobs=-1)( [delayed(process)(i) for i in range(10000)] )
print(sum(r))
print('{}秒かかりました'.format(time() - start))
print('並列あり--------------end')
