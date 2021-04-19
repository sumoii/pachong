#---codeing = utf -8---
# import urllib.request
# #获取一个 get请求
# # response = urllib.request.urlopen("http://httpbin.org/")
# # print(response.read().decode('utf-8'))
# # data = bytes(urllib.parse.urlencode({"holle":"wrold"}),encoding='utf-8')
# # response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# # print(response.read().decode('utf-8'))
# import urllib.parse
# url = "https://movie.douban.com/top250"
# headers ={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({"holle":"wrold"}),encoding='utf-8')
# req = urllib.request.Request(url=url,data=data,headers=headers)
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))
import urllib.parse
import urllib.request
import re
from bs4 import BeautifulSoup
#得到指定一个URL的网页内容

def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getdata(baseurl)
    savepath = ".\\豆瓣电影Top250.xls"
    saveData(savepath)

findlink = re.compile(r'<a href="(.*?)">')

def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
    }

    request = urllib.request.Request(url,headers=head)
    html= ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        print(html)
    eurllib.error.URLError as e:xcept
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        return html

# def getdata(baseurl):
#     datalist = []
#     for i in range(0,10):
#         url = baseurl + str(i*25)
#         html = askURL(url)
#
#         soup = BeautifulSoup(html,"html.parser")
#         for item in soup.find.all('div',class_="item"):
#             item = str(item)
#
#             link = re.findall(findlink,item)[0]
#             print(link)
#     return datalist
#
# def saveData(savepath):
#     print("save...")

