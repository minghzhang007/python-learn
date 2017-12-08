#!/usr/bin/python3

import sys


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)


def area(width, height):
    return width * height


def name(xing, name):
    print(xing, name)


print(area(4, 5))
print(area(height=6, width=4))
name(name='minghua', xing='zhang')


def printInfo(arg1, *vartuple):
    print("输出：", arg1)
    for x in vartuple:
        print(x)
    return


printInfo(10)
printInfo(10, 29, 345, 67)

sum1 = lambda arg1, arg2: arg1 + arg2
print("和：", sum1(10, 20))
print("和：", sum1(40, 20))


def sum2(arg1, arg2):
    total = arg1 + arg2
    print("total:", total)
    return total


print("结果：", sum2(10, 50))

num = 1


def fun1():
    num = 2
    print(num)
    num = 123
    print(num)


fun1()
print(num)

print("===========")


def outer():
    num = 10

    def inner():
        nonlocal num
        num = 100
        print(num)

    inner()
    print(num)


outer()
print(num)

list = ['java', 'python', 'go']
list.append('scale')
print(list)
list1 = ['c', 'c++']
list.extend(list1)
print(list)

print(list.count('java'))
list.sort()
print(list)
