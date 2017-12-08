def test1():
    while True:
        try:
            x = int(input("please enter a number:"))
            print('i got the number:', x)
            break
        except ValueError:
            print("Oops! That was no valid number.Try again ")


import sys


def test2():
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
        print(i)
    except OSError as err:
        print("OS error:{0}".format(err))
    except ValueError:
        print("cannot convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise  # raise语句抛出一个异常
    else:
        print("天下大吉！")
        f.close()


def getIntNumber():
    while True:
        x = input('guess a number between 0 and 100:')
        try:
            x = int(x)
        except:
            print('please input an integer.')
        else:
            break
    return x


from random import randint


def guess():
    target = randint(0, 100)
    x = getIntNumber()
    times = 1
    while target != x:
        if x < target:
            print("太小了")
        elif x > target:
            print("太大了")
        times += 1
        x = getIntNumber()
    else:
        print("you win...you get the number in", times, 'steps!')


def testRaise():
    try:
        raise NameError("HiThere")
    except NameError:
        print('An exception flew by!')
        raise


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def testdefinederror():
    try:
        raise MyError(2 * 2)
    except MyError as e:
        print('My Exception occured,value:', e.value)
    finally:
        print("good bye!")


def clean():
    with open('myfile.txt') as f:
        for line in f:
            print(line, end='')


clean()
