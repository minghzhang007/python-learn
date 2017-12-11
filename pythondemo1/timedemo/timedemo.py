import time

timetoken = time.time()
print('当前时间戳：', timetoken)

localtime = time.localtime(time.time())
print("本地时间：", localtime)

format_time = time.asctime(time.localtime(time.time()))
print("格式化后的本地时间：", format_time)

# 格式化为2017-12-11 10:17:39的形式
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

# 格式化为 Sat Mar 28 22:23:24 2017形式
print(time.strftime('%a %b %d %H:%M:%S %Y', time.localtime()))

# 将格式字符串转换为时间戳
a = "Mon Dec 11 10:19:36 2017"
print(time.mktime(time.strptime(a, '%a %b %d %H:%M:%S %Y')))

import calendar

cal = calendar.month(2017, 12)
print("2017年12月日历：")
print(cal)

calendar_calendar = calendar.calendar(2017, w=2, l=1, c=6)
# print(calendar_calendar)

print(calendar.isleap(2017))

print(calendar.leapdays(1989, 1991))

month = calendar.month(2017, 12, w=2, l=1)
print(month)
