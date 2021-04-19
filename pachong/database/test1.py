#!/user/bin/python3
# -*- codeing = utf-8 -*-
import sqlite3
sql='''
        create table noveltop
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
conn = sqlite3.connect("test1.db")
cousor=conn.cursor()
cousor.execute(sql)
conn.commit()
conn.close()