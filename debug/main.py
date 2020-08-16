def func1():
    print('func1')

def func2():
    print('func2')


def main():
    if not __debug__:
        print('Debug ON (python -O main.pyとすると実行される)')
        func1()
    func2()


if __name__ == '__main__':
    print('main---start')
    main()
