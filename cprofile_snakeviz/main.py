import time


def func1():
    print('func1')
    time.sleep(1)

def func2():
    print('func2')
    time.sleep(2)



def main():
    for i in range(3):
        func1()
    for i in range(3):
        func2()


if __name__ == '__main__':
    print('main---start')
    main()

