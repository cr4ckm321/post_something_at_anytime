#!/usr/bin/env python
#-*-coding:utf-8-*-
#Python Network Programmong cookbook -- Chapter - 1
#author : ch3rry

import socket
import sys

def get_remote_machine_info(host):
	remote_host = host
	try:
		print "Ip address of %s : %s" % (host,socket.gethostbyname(remote_host))
	except socket.error, err_msg:
		print "%s: %s" % (remote_host, err_msg)


if __name__ == '__main__':
	get_remote_machine_info(sys.argv[1])