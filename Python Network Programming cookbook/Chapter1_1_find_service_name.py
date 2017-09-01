#!/usr/bin/env python
#-*-coding:utf-8-*-
#author:ch3rry

import socket

def find_service_name():
	for port in [80, 25 , 22, 20, 445,139,1080]:
		print "Port : %s  => service name : %s" %(port, socket.getservbyport(port))
	print "Port : %s => service name : %s" %(53, socket.getservbyport(53,'udp'))

if __name__ == '__main__':
	find_service_name()