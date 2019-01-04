#!/bin/bash

# for
for VAR in $LIST
do
    echo "$VAR"
done

# 生成序列
echo {1..50}
echo {a..z}
echo {A..z}

# one line
for i in {a..z}; do echo $i; done;

# C Style
for((i=0;i<10;i++));
do
    echo $i
done

# while
while condition
do
    echo true;
done

# until
x=0;
until [ $x -eq 9 ];
do
    (( x++ )); echo $x;
done

