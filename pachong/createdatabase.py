#!/user/bin/python3
# -*- codeing = utf-8 -*-
import sqlite3
sql='''
    create table novel250
    (id integer primary key autoincrement,
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
conns = sqlite3.connect("noveldb")
cours = conns.cursor()
cours.execute(sql)
conns.commit()
conns.close()
print("连接成功")

conn = sqlite3.connect("noveldb")
cur = conn.cursor()

for data in datalist:
    for index in range(len(data)):
        if index == 4 or index == 5:
            continue
        data[index] = '"' + data[index] + '"'
    sql = '''
            insert into movie250(
            info_link,pic_link,cname,ename,score,rated,instroduction,info)
            values(%s)''' % ",".join(data)
    print(sql)
    cur.execute(sql)
    conn.commit()
cur.close()
conn.close()
