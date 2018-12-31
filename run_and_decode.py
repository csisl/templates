  1 #!/usr/bin/python3
  2 import subprocess
  3 import sys
  4 from pathlib import Path    # to make sure the file exists before executing
  5
  6 # This python script will execute another script and save the output
  7 # into a variable for further use
  8
  9 # usage: python run_and_decode.py
 10
 11 # script to be executed
 12 script = ""
 13
 14 # how we are going to execute the script
 15 exc = "./"
 16
 17 # ensure the script exists
 18 # default path is the pwd
 19 path = "./" + script
 20
 21 path_check = Path(path)
 22 if not path_check.is_file():
 23     print("File not found {}".format(path))
 24     sys.exit()
 25
 26 try:
 27     executable = exc + script
 28     # save the output instead of printing directly
 29     output = subprocess.run([executable], stdout=subprocess.PIPE)
 30
 31     # decode the output
 32     decoded_out = output.stdout.decode('utf-8')
 33
 34     print(decoded_out)
 35 except:
 36     print("Unable to execute {}".format(script))
 37     sys.exit()
