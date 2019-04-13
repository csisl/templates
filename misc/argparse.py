#!/usr/bin/python3
import argparse

if __name__ == "__main__":
	global debug
	debug = False

	parser = argparse.ArgumentParser(description="Description of project")

	# required argument
	parser.add_argument("foo",
			help="Help message for foo")

	# optional argument
	parser.add_argument("-d", "--debug", action="store_true",
			help="Debug mode")

	args = parser.parse_args()

	print("Required arguemnt: {}".format(args.foo))

	if args.debug:
		debug = True
