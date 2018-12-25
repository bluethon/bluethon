#!/bin/bash

line="root:x:0:0:System Administrator:/var/root:/bin/sh"
oldIFS=$IFS;
IFS=":"
count=0
for item in $line;
do
    [ $count -eq 0 ] && user=$item;
    [ $count -eq 6 ] && shell=$item;
    (( count++ ))
done;
IFS=$oldIFS;
echo "$user"\'s shell is "$shell";
