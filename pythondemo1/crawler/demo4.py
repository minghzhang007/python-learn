from urllib import request
import http.cookiejar
import re


def getXsrf(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags=0)
    strlist = cer.findall(data)
    return strlist[0]


def makeMyOpener(head={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    cookie_jar = http.cookiejar.CookieJar()
    opener = request.build_opener(request.HTTPCookieProcessor(cookie_jar))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


opener = makeMyOpener()
uop = opener.open('http://www.zhihu.com', timeout=2)
data = uop.read().decode()
xsrf = getXsrf(data)
print("xsrf:" + xsrf)
