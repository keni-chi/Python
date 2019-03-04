from sample import func1 #とか
import sample #とかすることで、　(ただし、func2は使えません。)

if __name__ == "__main__":
    print('-------start')
    x, y = sample.func1(5)
    print(x)
    print(y)

    sample.func3()

    print('-------end')
