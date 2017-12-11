from urllib import request
from bs4 import BeautifulSoup

url = 'http://guofeng.yuedu.163.com/yc/category/4'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
Request = request.Request(url, headers=headers)
http_response = request.urlopen(Request)
page = http_response.read().decode('utf-8')
print(page)

soup = BeautifulSoup(page, 'html.parser')
allSources = soup.find_all('a')

with open(r'E:\code\github_workspace\python-learn\pythondemo1\crawler\novels.txt', 'w') as file:
    for x in allSources:
        if x is None:
            pass
        else:
            if x.string is not None and x.get("href") is not None:
                file.write(x.string + "\n")
                file.write("http://guofeng.yuedu.163.com" + x.get("href") + "\n\n")
