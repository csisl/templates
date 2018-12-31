  1 #!/usr/bin/python3
  2 import subprocess
  3 import sys
  4 from pathlib import Path    # to make sure the file exists before executing
  5
  6 # script to be executed
  7 script = ""
  8
  9 # how to execute the script; default is ./
 10 exc = "./"
 11
 12 # ensure the script file exists
 13 # default path is the pwd
 14 path = "./" + script
 15
 16 path_check = Path(path)
 17 if not path_check.is_file():
 18     print("File not found {}".format(path))
 19     sys.exit()
 20
 21 try:
 22     executable = exc + script
 23     # attempt to execute the script
 24     subprocess.call([executable])
 25 except:
 26     print("Unable to execute {}".format(script))
