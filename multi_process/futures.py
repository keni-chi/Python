import time
import concurrent.futures


def func1():
    print("func1")
    time.sleep(1)
    return('1_return')


def func2():
    print("func2")
    time.sleep(1)
    return('2_return')


if __name__ == "__main__":
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=2)
    for i in range(3):
        x = executor.submit(func1)
        print('x---')
        print(x)
        print(vars(x))
    for i in range(3):
        y = executor.submit(func2)
        print('y---')
        print(y)
        print(vars(y))


##### 実行例
# multi_process $ python futures.py 
# x---
# <Future at 0x10cb8fe80 state=running>
# {'_condition': <Condition(<unlocked _thread.RLock object owner=0 count=0 at 0x10cb7f3c0>, 0)>, '_state': 'RUNNING', '_result': None, '_exception': None, '_waiters': [], '_done_callbacks': []}
# x---
# <Future at 0x10ce508d0 state=running>
# {'_condition': <Condition(<unlocked _thread.RLock object owner=0 count=0 at 0x10cb7f4b0>, 0)>, '_state': 'RUNNING', '_result': None, '_exception': None, '_waiters': [], '_done_callbacks': []}
# x---
# <Future at 0x10ce50a20 state=pending>
# func1
# {'_condition': <Condition(<unlocked _thread.RLock object owner=0 count=0 at 0x10cb7f4e0>, 0)>, '_state': 'RUNNING', '_result': None, '_exception': None, '_waiters': [], '_done_callbacks': []}
# y---
# <Future at 0x10ce509e8 state=pending>
# {'_condition': <Condition(<unlocked _thread.RLock object owner=0 count=0 at 0x10cb7f240>, 0)>, '_state': 'PENDING', '_result': None, '_exception': None, '_waiters': [], '_done_callbacks': []}
# y---
# <Future at 0x10ce507b8 state=pending>
# func1
# {'_condition': <Condition(<unlocked _thread.RLock object owner=0 count=0 at 0x10cb7f5a0>, 0)>, '_state': 'PENDING', '_result': None, '_exception': None, '_waiters': [], '_done_callbacks': []}
# y---
# <Future at 0x10ce50c50 state=pending>
# {'_condition': <Condition(<unlocked _thread.RLock object owner=0 count=0 at 0x10cb7f5d0>, 0)>, '_state': 'PENDING', '_result': None, '_exception': None, '_waiters': [], '_done_callbacks': []}
# func1
# func2
# func2
# func2
