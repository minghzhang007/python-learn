from urllib import request

from bs4 import BeautifulSoup

url = "http://www.jianshu.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

page = request.Request(url, headers=headers)
# 打开Url,获取HttpResponse返回对象并读取其ResponseBody
urlopen = request.urlopen(page)
page_info = urlopen.read().decode('utf-8')
print(type(urlopen))

# 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
soup = BeautifulSoup(page_info, 'html.parser')
# 以格式化的形式打印html
# print(soup.prettify())
# 查找所有a标签中class='title'的语句
titles = soup.find_all('a', 'title')
#
with open(r'E:\code\github_workspace\python-learn\pythondemo1\crawler\articles.txt', 'w') as file:
    for title in titles:
        file.write(title.string + "\n")
        file.write("http://www.jianshu.com" + title.get('href') + "\n\n")
