#!/bin/bash
while [ 1 ]
do
for line in $(cat .chan)
do
ffplay -x 960 -y 540 -t 20  $line &
sleep 19
kill -SIGINT $!
done
done
