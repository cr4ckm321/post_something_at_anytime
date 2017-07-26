#encoding:utf-8

import requests

u = 'http://active.zol.com.cn'

try:
	conn = requests.get(url=u)
	a = conn.content
	print a
except Exception as e:
	print e
