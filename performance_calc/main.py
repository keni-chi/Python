from peformance_calc import peformance_calc


@peformance_calc
def func1() :
    j=0
    for i in range(1000) :
        j+=i
    print('func1')
    print(j)


@peformance_calc
def func2(x) :
    j=x
    for i in range(2000) :
        j+=i
    print('func2')
    print(j)
    return j


func1()
print(func2(1000))