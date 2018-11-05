#!/usr/bin/python2
import socket
import sys
import telnetlib

# Create a socket to interact with target and send over commands
target = '192.0.2.0'
port = 24

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print "Socket created successfully"
except socket.error as err:
	print "Socket creation failed. Err: {}".format(err)
	sys.exit()
s.connect((target, port))
t = telnetlib.Telnet()
t.sock = s
t.interact()
