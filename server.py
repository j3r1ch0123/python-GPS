#!/bin/python3.9
import socket
import sys

s = socket.socket()
s.bind(("127.0.0.1",9000)) #Change these
print("Listening...")
s.listen(10)

while True:
    sc, address = s.accept()
    print("Location received from " + address)
    f = open('location.txt','ab+') #open in binary
    l = 1
    while(l):
        l = sc.recv(1024)
        while (l):
            f.write(l)
            l = sc.recv(1024)
        f.close()

    sc.close()

s.close()
