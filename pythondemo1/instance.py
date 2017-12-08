def getnumber():
    while True:
        try:
            x = input("input a number.")
            return float(x)
        except:
            print("must input a number.")


def testSum():
    x = getnumber()
    y = getnumber()
    sum = float(x) + float(y)
    print("数字{0}和{1}之和为：{2}".format(x, y, sum))


import cmath


def testSqrt():
    num = getnumber()
    if num < 0:
        num_sqrt = cmath.sqrt(num)
        print('{0}的平方根为：{1:0.3f}+{2:0.3f}'.format(num, num_sqrt.real, num_sqrt.imag))
    else:
        num_sqrt = num ** 0.5
        print("%0.4f的平方根为：%0.6f" % (num, num_sqrt))


def testdoubleequation():
    a = getnumber()
    b = getnumber()
    c = getnumber()
    d = (b ** 2) - (4 * a * c)
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    print("result is {0}和{1}".format(sol1, sol2))
    print("result is %s和%s" % (sol1, sol2))


testdoubleequation()
