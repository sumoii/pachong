#!/user/bin/python3
# -*- codeing = utf-8 -*-
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup
import xlwt
import sqlite3

def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getdata(baseurl)
    savepath = ".\\豆瓣TOP250.xls"
    savedata(datalist,savepath)
    dbpath = "movie.db"
    saveData2DB(datalist,dbpath)



#影片的链接
findlink =re.compile(r'<a href="(.*?)">')
#影片的图片
findimg =re.compile(r'<img.*src="(.*?)"',re.S)
#影片名
findtitle = re.compile(r'<span class="title">(.*)</span>')
#影片评分
findpro =re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#影片评价人数
findnum =re.compile(r'<span>(\d.*)人评价</span>')
#影片概况
findinq=re.compile(r'<span class="inq">(.*?)</span>')
#影片相关内容
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)
#爬取单个网页的内容

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

def getdata(baseurl):
    datalist = []
    for i in range(0,10):
        url = baseurl + str(i*25)
        html = askURL(url)

        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div', class_='item'):
            data = []
            item = str(item)
            link = re.findall(findlink,item)[0]
            data.append(link)

            img = re.findall(findimg,item)[0]
            data.append(img)

            titles = re.findall(findtitle,item)
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/"," ")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append('')

            pro = re.findall(findpro,item)[0]
            data.append(pro)
            num = re.findall(findnum,item)[0]
            data.append(num)
            inq =re.findall(findinq,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")
                data.append(inq)
            else:

                data.append(" ")

            Bd =re.findall(findBd,item)[0]
            Bd =re.sub('<br(\s+)?/>(s+)?',"",Bd)
            Bd =re.sub('/','',Bd)
            data.append(Bd.strip())
            datalist.append(data)
    print(datalist)

    return datalist

def savedata(datalist,savepath):
    print("save...")
    workbook = xlwt.Workbook(encoding='utf -8')
    worksheet = workbook.add_sheet("豆瓣电影TOP2500",cell_overwrite_ok = True)
    col =("电影链接","图片链接","中文名","英文名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        worksheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条"%(i+1))
        data=datalist[i]
        for j in range (0,8):
            worksheet.write(i+1,j,data[j])
    workbook.save(savepath)

def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist :
        for index in range(len(data)):
            if index ==4 or index ==5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
                insert into movie250(
                info_link,pic_link,cname,ename,score,rated,instroduction,info)
                values(%s)'''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

def init_db(dbpath):
    sql='''
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric ,
        rated numeric ,
        instroduction text,
        info text
        );
    '''
    conn = sqlite3.connect(dbpath)
    couser =conn.cursor()
    couser.execute(sql)
    conn.commit()
    conn.close()



if __name__ == "__main__":
 # 调用函数
    main()
    print("爬取完成")
