#!/bin/python3.9
import socket
import sys

s = socket.socket()
s.bind(("139.162.117.110",9000)) #Change these
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
            l = sc.recv(1024)
        f.close()
        with open('location.txt', 'r') as thefile:
            contents = thefile.read()
            print(contents)

    sc.close()

s.close()
