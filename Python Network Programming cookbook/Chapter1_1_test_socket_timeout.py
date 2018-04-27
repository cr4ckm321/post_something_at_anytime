#!/usr/bin/env python
#-*-coding:utf-8-*-
#author:ch3rry

import socket

def test_socket_timeout():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print "Defalut socket timeout : %s" %s.gettimeout()
	s.settimeout(100)
	print "Current socket timeout : %s" %s.gettimeout()

if __name__ == '__main__':
	test_socket_timeout()