#!/bin/bash
./watch.py
sleep 3
while [ 1 ]
do
for line in $(cat .chan)
do
ffplay -loglevel error -x 960 -y 540 -fs $line &
sleep 15
kill -SIGINT $!
done
done
