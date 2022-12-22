#!/bin/python3.10
from subprocess import call, Popen, PIPE
import shlex
import time

# Create an output file
filename = "locations.txt"
cmd = f"nc -lnvp 5000 >> {filename}"
clear = "clear"

# Let it run indefinitely (use a cron job I recommend)
while True:
# This way the shellcode runs in the background
    Popen(shlex.split(cmd), stderr=PIPE, stdin=PIPE, stdout=PIPE)
# Read the file
    with open(filename, "r") as thefile:
        contents = thefile.read()
# Display contents onscreen
        print(contents)
# Clear the screen every five seconds to keep things from getting too messy
        time.sleep(5)
        call(clear)
        continue
                  
