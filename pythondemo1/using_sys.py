import sys
import iter
import fabonacci

print('命令行参数如下：')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')

print(iter.area(40, 50))

fabonacci.fab(20)
print(fabonacci.fab1(1000))