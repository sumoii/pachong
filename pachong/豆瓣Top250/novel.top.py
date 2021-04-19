#!/user/bin/python3
# -*- codeing = utf-8 -*-
import urllib.requests
import urllib.parse
import re
from bs4 import BeautifulSoup
import xlwt
import sqlite3
def main():
    http="https://book.douban.com/top250?start="
    datalist=getdata(http)
    savepath=".\\novel.top.xlwt"
def askURL(url):
    head = {
     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"
    }
    html = ""
    try:
        req = urllib.request.Request(url,headers=head)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

def getdata():
    for i in range(0:10):
