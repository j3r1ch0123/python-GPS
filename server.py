#!/bin/python3.10
from subprocess import call, Popen, PIPE
import shlex
import time

cmd = "nc -lnvp 5000 >> results.txt"
clear = "clear"

filename = "results.txt"
while True:
    Popen(shlex.split(cmd), stderr=PIPE, stdin=PIPE, stdout=PIPE)
    with open(filename, "r") as thefile:
        contents = thefile.read()
        print(contents)
        time.sleep(5)
        call(clear)
        continue
                  
