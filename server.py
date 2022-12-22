#!/bin/bash
while :
do
    nc -lnvp 5000 >> location.txt
    sleep 3
done
