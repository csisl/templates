#!/usr/bin/python3
import subprocess
import sys
from pathlib import Path    # to make sure the file exists before executing

# template for executing another script with a python program using subprocess.call

# usage: python sub_call.py

# script to be executed
script = ""

# how we want to execute the other script; default is ./
exc = "./"

# ensure the script exists before continuing
# default path is the pwd
path = "./" + script

path_check = Path(path)
if not path_check.is_file():
    print("File not found {}".format(path))
    sys.exit()
    
try:
    executable = exc + script
    # attempt to execute the script
    subprocess.call([executable])
except:
    print("Unable to execute {}".format(script))
