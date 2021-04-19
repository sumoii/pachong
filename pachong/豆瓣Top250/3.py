#!/user/bin/python3
# -*- codeing = utf-8 -*-
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import re


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getdata(baseurl)
    savepath = ".\\豆瓣Top250.xls"
    saveData(savepath)


findlink = re.compile(r'<a href="(.*?)">')


def getdata(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)

        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            item = str(item)
            link = re.findall(findlink,item)[0]
            print(link)
    return datalist


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
    }

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def saveData(savepath):
    print("Save.....")


if __name__ == "__main__":
    # 调用函数
    main()
