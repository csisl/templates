#!/usr/bin/python2
import subprocess

# usage: python subp.py
# This program will execute the script specified and check the output for a certain keyword

# script to be executed
script = ""

# check the ouput for certain keywords
output = subprocess.check_output("./{}".format(script), shell=False)

# keyword to check for 
keyword = ""

if keyword in output:
	# the output we are looking for was found
	print("keyword found: {}".format(keyword))
