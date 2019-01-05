#!/usr/bin/python3 
import sys

if len(sys.argv) < 2:
	print ("Usage: -filename")
	sys.exit()
	
def readFile(filename):
	try:
		f = open(filename, 'r')
	except IOError:
		print ("Error opening file {}".format(filename))
		sys.exit()
	while True:
		line = f.readline()
		print (line.strip('\n'))
		if line == "":
			# EOF
			break
		line = line.rstrip('\n')
	f.close

if __name__ == "__main__":
	filename = sys.argv[1]
	readFile(filename)
	
	
