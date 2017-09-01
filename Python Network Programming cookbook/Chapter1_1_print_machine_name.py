#!/usr/bin/env python
#-*-coding:utf-8-*-
#author:ch3rry
#Python Network Programming Cookbook --Chapter -1

import socket

def print_machine_info():
	host_name = socket.gethostname()
	ip_adddress = socket.gethostbyname(host_name)
	print "Host name : %s" % host_name
	print "Ip address : %s" % ip_adddress


if __name__ == '__main__':
	print_machine_info()