#coding:utf-8
#author : ch3rry

import base64
import requests
import urllib

url = 'http://ctf5.shiyanbar.com/web/10/10.php'

a=base64.b64decode(requests.get(url).headers['FLAG']).split(":")[1]
print a

#b = "{'key':%s}" %a
b = {'key':a}

print b

r1 = requests.post(url,data=b)

print r1.text