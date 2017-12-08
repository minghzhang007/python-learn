import pickle, pprint
from urllib import request

s = 'Hello,Runoob'
str1 = str(s)
repr1 = repr(s)
print(str1)
print(repr1)


class Animal:
    age = 10
    name = "animal"

    def __init__(self, age, name):
        self.age = age
        self.name = name
        print(self)
        print(self.__class__)


class People:
    name = ''
    age = 0
    _weight = 0

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self._weight = weight

    def speak(self):
        print("%s 说：我%d岁,体重：%d千克" % (self.name, self.age, self._weight))

    def __str__(self):
        return '姓名:%s,年龄:%d,体重:%d' % (self.name, self.age, self._weight)


p = People('lewis', 26, 60)
print(p)


class student(People):
    grade = ''

    def __init__(self, name, age, weight, grade):
        People.__init__(self, name, age, weight)
        self.grade = grade

    def speak(self):
        print("%s说：我%d岁了，在读%d年级" % (self.name, self.age, self.grade))


class speaker():
    topic = ''
    name = ''

    def __init__(self, name, topic):
        self.name = name
        self.topic = topic

    def speak(self):
        print("我叫%s,我是一个演说家，我演讲的主题是%s" % (self.name, self.topic))


class sample(speaker, student):
    a = ''

    def __init__(self, name, age, weight, grade, topic):
        student.__init__(self, name, age, weight, grade)
        speaker.__init__(self, name, topic)


test = sample('tim', 25, 80, 4, 'python')
test.speak()
print(test)


class parent:
    def my(self):
        print('invoke parent\' my method')


class child(parent):
    def my(self):
        print('invoke child\' my method')


c = child()
c.my()


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公共变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)


class Site:
    def __init__(self, name, url):
        self.name = name
        self.__url = url

    def who(self):
        print('name:', self.name)
        print('url:', self.__url)

    def __foo(self):
        print('this is a private method !')

    def foo(self):
        print('this is a public method!')
        self.__foo()


x = Site('菜鸟教程', 'www.runoob.com')
x.who()
x.foo()

x = 10 * 3.25
y = 200 * 200
s = 'x的值为：' + repr(x) + ',y的值为：' + repr(y) + '...'
print(s)
s = 'x的值为：' + str(x) + ',y的值为：' + str(y) + '...'
print(s)

hello = 'hello,runoob\n'
hellos = repr(hello)
print(hello)
print(hellos)

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    print(repr(x * x * x).rjust(4))

print("============================")
for x in range(1, 11):
    print('{0:5d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

print('{name}网址：{site}'.format(name='菜鸟教程', site='www.runoob.com'))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

# f = open('./foo.txt', mode='a+', encoding='utf-8')
# f.write('python 是一个非常好的语言。\n是的，的确非常好！\n')
# f.close()
f = open('./foo.txt', mode='r', encoding='utf-8')
string = f.read()
print(string)
f.close()
print('=============')
f = open('./foo.txt', mode='r', encoding='utf-8')
f1 = open('./foocopy.txt', mode='w', encoding='utf-8')
for x in f:
    print(x, end=' ')
    f1.write(x)

f1.close()
f.close()

a = {1, 2, 3}
e = {1, 2, 3}
b = {2, 1, 3}
print(id(a))
print(id(e))
print(id(b))
print(a == b)
print(a == e)

print(a is b)

c = (1, 2, 3)
d = (2, 1, 3)
print(c == d)
print(c is d)

data = {'a': [1, 2.0, 3, 4 + 6j],
        'b': ('string', u'Unicode string'),
        'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
output = open('data.pk1', 'wb')
pickle.dump(data, output)

pickle.dump(selfref_list, output, -1)

output.close()

pk1_file = open('data.pk1', 'rb')
data = pickle.load(pk1_file)
pprint.pprint(data)

load = pickle.load(pk1_file)
pprint.pprint(load)
pk1_file.close()

response = request.urlopen("http://www.baidu.com")
file = open('project.txt', 'w')
read = response.read()
file.write(str(read))
file.close()
