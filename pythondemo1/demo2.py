#!/usr/bin/python3

a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a + b

print('==================')
print('==================')

n = 100
summ = 0
index = 1
while index <= n:
    summ += index
    index += 1

print("1 到 %d 之和为：%d" % (n, summ))

count = 0
while count < 5:
    print(count, " 小于5")
    count += 1
else:
    print(count, "大于或者等于5")

languages = ['c', 'c++', 'Perl', 'java', 'paython']
for x in languages:
    if x == 'java':
        print(x)
        break
else:
    print('语音没有数据')

for i in range(5):
    print(i)

print("============")
print("============")
for i in range(5, 9):
    print(i)

print("============")
for i in range(0, 10, 3):
    print(i)

print("============")
a = ['google', 'baidu', 'runoob', 'taobao', 'qq']
for i in range(len(a)):
    print(i, a[i])
print("==================")
for i in range(2, 2):
    print(i)
print("=================")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '=', '*', n // x)
            break
    else:
        print(n, '是质数')

score = int(input("请输入成绩："))
if score < 60:
    print("不及格")
elif score < 70:
    print("及格")
elif score < 80:
    print("合格")
elif score < 90:
    print("良好")
elif score <= 100:
    print("优秀")
else:
    print("输入非法")

input("点击enter键退出")
