#!/usr/bin/python3
import subprocess
import sys
from pathlib import Path        # to make sure the file exists before executing

# This python script will execute another script and save the output
# into a variable for further use

# usage: python run_and_decode.py

# script to be executed
script = ""

# how we are going to execute the script
exc = "./"

# ensure the script exists
# default path is the pwd
path = "./" + script

path_check = Path(path)
if not path_check.is_file():
        print("File not found {}".format(path))
        sys.exit()

try:
        executable = exc + script
        # save the output instead of printing directly
        output = subprocess.run([executable], stdout=subprocess.PIPE)

        # decode the output
        decoded_out = output.stdout.decode('utf-8')

        print(decoded_out)
except:
        print("Unable to execute {}".format(script))
        sys.exit()
