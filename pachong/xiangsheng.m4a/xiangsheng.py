#!/user/bin/python3
# -*- codeing = utf-8 -*-
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup
import requests
findtitle = re.compile(r'<span class="title lF_">(.*?)</span>')
findhref = re.compile(r'.*href="(.*?)".*')
head = {
         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"
        }
def main():
    baseurl = 'https://www.ximalaya.com/xiangsheng/35105051/'
    getdata(baseurl)

def askurl(url):

    html = ""
    try:
        req = urllib.request.Request(url,headers=head)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return(html)

def getdata(baseurl):
    for i in range(1,):
        url = baseurl +f"p{i}"
        html= askurl(url)

        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div',class_="text lF_"):
            datatitle=[]
            item = str(item)
            title = re.findall(findtitle,item)[0]
            title = title +".m4a"
            href = re.findall(findhref,item)[0]
            m4a_id = href.split('/')[-1]

            json_url=f'https://www.ximalaya.com/revision/play/v1/audio?id={m4a_id}&ptype=1'
            print(json_url)
            data_jion = requests.get(url=json_url,headers= head).json()
            m4a_url=data_jion['data']['src']
            data_m4a=requests.get(url=m4a_url, headers =head).content
            with open('xiangsheng.m4a\\' + title ,mode='wb' )as f :
                f.write(data_m4a)
                print('下载完成：',title)




if __name__ == "__main__":
 # 调用函数
    main()
    print("爬取完成")
